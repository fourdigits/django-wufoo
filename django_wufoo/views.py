from django.conf import settings
from django.shortcuts import render
from django_wufoo.models import *
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Define system fields
WUFOO_SYSTEM_FIELDS = getattr(settings, 'WUFOO_SYSTEM_FIELDS', ['IP', 'CompleteSubmission', 'LastPage', 'DateUpdated'])

def get_form_by_name(name):
    try:
        return WufooForm.objects.get(name=name)
    except WufooForm.DoesNotExist:
        return False

def sync_forms(wufoo_forms):
    exclusion_forms = [] # keep track of which forms Wufoo knows
    for wufoo_form in wufoo_forms:
        form, created = WufooForm.objects.get_or_create(name=wufoo_form.Name)
        exclusion_forms.append(form)
    
    # Wufoo is the Grand Data Maester. We delete all forms that Wufoo does not know of, all forms, fields and entries will be destroyed!
    remove_forms = WufooForm.objects.all().exclude(id__in=[form.id for form in exclusion_forms] )
    remove_forms.delete()
    
def sync_fields(wufoo_form):
    form = get_form_by_name(wufoo_form.Name)
    if not form:
        raise Exception("sync_fields:: no form with name: %s, try to run sync_form first" % wufoo_form.Name)
    
    exclusion_fields = [] # keep track of which fields Wufoo knows
    exclusion_subfields = [] # keep track of which subfields Wufoo knows
    
    for wufoo_field in wufoo_form.fields:
        if wufoo_field.SubFields:
            field, created = WufooField.objects.get_or_create(title=wufoo_field.Title, form=form, wufoo_id="NO_ID", field_type="subfields")
            exclusion_fields.append(field)
            
            for wufoo_subfield in wufoo_field.SubFields:
                subfield, created = WufooSubField.objects.get_or_create(label=wufoo_subfield.Label, field=field, wufoo_id=wufoo_subfield.ID, default_val=wufoo_subfield.DefaultVal)
                exclusion_subfields.append(subfield)
        elif wufoo_field.ID:
            field, created = WufooField.objects.get_or_create(title=wufoo_field.Title, form=form, wufoo_id=wufoo_field.ID)
            exclusion_fields.append(field)
            
            # update fieldattributes if they have changed
            if wufoo_field.Type and wufoo_field.Type != field.field_type:
                field.field_type = wufoo_field.Type
                field.save()
        else:
            logging.warning( "sync_fields:: no wufoo_field.ID - wufoo_field.Title:%s, wufoo_field.ID:%s, wufoo_field.Type:%s, wufoo_field.Choices:%s, wufoo_field.SubFields:%s" % (wufoo_field.Title, wufoo_field.ID, wufoo_field.Type, wufoo_field.Choices, wufoo_field.SubFields) )
    
    # remove fields not known by Wufoo
    remove_fields = WufooField.objects.filter(form=form).exclude(id__in=[field.id for field in exclusion_fields] )
    remove_fields.delete()
    
    # remove subfields not known by Wufoo
    remove_subfields = WufooSubField.objects.filter(field__form=form).exclude(id__in=[subfield.id for subfield in exclusion_subfields] )
    remove_subfields.delete()
    
def sync_entries(wufoo_form):
    form = get_form_by_name(wufoo_form.Name)
    if not form:
        raise Exception("sync_entries:: no form with name: %s, try to run sync_form first" % wufoo_form.Name)
    
    exclusion_entries = [] # keep track of which entries Wufoo knows
    exclusion_fieldentries = [] # keep track of which fieldentries Wufoo knows
    
    for w_entry in wufoo_form.get_entries():
        entry, created = WufooEntry.objects.get_or_create(entry_id=w_entry.get('EntryId', False), form=form)
        exclusion_entries.append(entry)
        
        for key, value in w_entry.iteritems():
            try:
                if value and key not in WUFOO_SYSTEM_FIELDS: # discard fields without a value, and skip system fields
                    field = WufooField.objects.get(wufoo_id=key, form=form)
                    fieldentry, created = WufooFieldEntry.objects.get_or_create(wufoo_entry=entry, field=field, value=value)
                    exclusion_fieldentries.append(fieldentry)
            except WufooField.DoesNotExist:
                # the dict contains entries for both fields and subfields, if there is no field for the key, try to find a subfield for it
                try:
                    subfield = WufooSubField.objects.get(wufoo_id=key, field__form=form)
                    fieldentry, created = WufooFieldEntry.objects.get_or_create(wufoo_entry=entry, field=subfield.field, subfield=subfield, value=value)
                    exclusion_fieldentries.append(fieldentry)
                except WufooSubField.DoesNotExist:
                    logging.warning( "sync_entries:: no field or subfield with id: %s, form:%s" % (key, form) )
        
    # remove entries not known by Wufoo
    remove_entries = WufooEntry.objects.filter(form=form).exclude(id__in=[entry.id for entry in exclusion_entries] )
    remove_entries.delete()
    
    # remove fieldentries not known by Wufoo
    remove_fieldentries = WufooFieldEntry.objects.filter(field__form=form).exclude(id__in=[fieldentry.id for fieldentry in exclusion_fieldentries] )
    remove_fieldentries.delete()