from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from pyfoo import *
from django_wufoo.models import *
from django_wufoo.views import sync_forms, sync_fields, sync_entries

class Command(BaseCommand):
    help = 'Fetch all forms, (sub)fields and entries from Wufoo'
    
    def handle(self, *args, **options):
        self.stdout.write("Fetch all forms Wufoo forms")
        
        # get api credentials from settings
        WUFOO_USER = getattr(settings, 'WUFOO_USER', None)
        WUFOO_API_KEY = getattr(settings, 'WUFOO_API_KEY', None)
        
        if not WUFOO_USER or not WUFOO_API_KEY:
            raise Exception("Please add both WUFOO_USER and WUFOO_API_KEY to settings")
        
        # api key for user intosaxion
        api = PyfooAPI(WUFOO_USER, WUFOO_API_KEY)
        
        # synchronize forms
        sync_forms(api.forms)
        
        for form in api.forms:
            # synchronize fields
            sync_fields(form)
            # synchronize entries
            entries = sync_entries(form)