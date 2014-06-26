from django.contrib import admin
from django_wufoo.models import *

class FieldInline(admin.StackedInline):
    model = WufooField
    readonly_fields = ('id', 'wufoo_id', 'title', 'field_type')
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

class SubFieldInline(admin.StackedInline):
    model = WufooSubField
    readonly_fields = ('id', 'field', 'wufoo_id', 'label', 'default_val')
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

class FieldEntryInline(admin.StackedInline):
    model = WufooFieldEntry
    readonly_fields = ('id', 'field', 'subfield', 'value')
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

class WufooFormAdmin(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [
        FieldInline,
    ]
    
class WufooFieldAdmin(admin.ModelAdmin):
    list_display = ('title', 'wufoo_id', 'field_type', 'form')
    list_filter = ('form', )
    search_fields = ('title', )
    
    inlines = [
        SubFieldInline,
    ]
    
class WufooSubFieldAdmin(admin.ModelAdmin):
    list_display = ('field', 'wufoo_id', 'label', )
    list_filter = ('field__form', )
    search_fields = ('label', 'wufoo_id', 'field__title')

class WufooEntryAdmin(admin.ModelAdmin):
    list_display = ('entry_id', 'form', )
    list_filter = ('form', )
    search_fields = ('entry_id', )
    
    inlines = [
        FieldEntryInline,
    ]

class WufooFieldEntryAdmin(admin.ModelAdmin):
    list_display = ('field', 'subfield', 'value', )
    list_filter = ('field__form', 'wufoo_entry', )
    search_fields = ('field__title', 'value', 'wufoo_entry__entry_id')

admin.site.register(WufooForm, WufooFormAdmin)
admin.site.register(WufooField, WufooFieldAdmin)
#admin.site.register(WufooSubField, WufooSubFieldAdmin)
admin.site.register(WufooEntry, WufooEntryAdmin)
#admin.site.register(WufooFieldEntry, WufooFieldEntryAdmin)