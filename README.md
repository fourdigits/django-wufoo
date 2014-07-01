About
=====

Django app that synchronizes Wufoo forms (one-Way) to your database. Syncronization of forms, fields, subfields and entries are supported.

Requirements
------------

- Python 2.7
- Django (1.6)
- [pyfoo](https://github.com/wufoo/pyfoo), or use [this fork](https://github.com/stetelepta/pyfoo) which has pip support

Usage
=====

 1. Update your `settings.py`:
 
        # Add `django_wufoo` to `INSTALLED_APPS`
        INSTALLED_APPS = (
            ...
            'django_wufoo',
            )
        ..
        # Add Wufoo credentials
        WUFOO_USER = 'your_account_name'
        WUFOO_API_KEY = 'your_api_key'

 2. Run `python manage.py syncdb` to create the django-wufoo tables.

 3. Run `python manage.py sync_formdata` to fetch all forms and associated data. Use a cronjob (or perhaps a [Webhook](http://help.wufoo.com/articles/en_US/SurveyMonkeyArticleType/Webhooks)) to keep the database synchronized.

 4. Now you are ready to use the django-wufoo models:
        
        >>> from django_wufoo.models import WufooForm
        
        # get a Wufoo form
        >>> form = WufooForm.objects.first()
        
        # get all fields definitions
        >>> fields = form.wufoofield_set.all()

        # get all user entries for this form
        >>> entries = form.wufooentry_set.all()
        
Notes
-----

 1. Wufoo is the authoritative datasource, and during a sync all forms, fields and entries not known to Wufoo will be destroyed. (So, don't bother adding things either..)
 2. django-wufoo synchronizes basic data from Wufoo, as we don't need more for now. For example, it only stores the name of a form, and skips fields like `Description`, `Redirect Message` etc. Feel free to extend it.