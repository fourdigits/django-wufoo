About
=====

Django app that synchronizes Wufoo forms (one-Way) to your database. Syncronization of forms, fields, subfields and entries are supported.

Requirements
------------

- Python 2.7
- Django (1.6)
- [pyfoo](https://github.com/wufoo/pyfoo), or use [this fork](https://github.com/amites/pyfoo) which has pip support

Usage
=====

 1. Update your `settings.py`:
 
        # Add `django_wufoo` to `INSTALLED_APPS`
        INSTALLED_APPS = (
            ...
            'django_wufoo',
            )
 
 2. Run `python manage.py syncdb` to create the django-wufoo tables.

 3. Run `python manage.py sync_formdata` to fetch all forms and associated data. Use a cronjob (or perhaps a [Webhook](http://help.wufoo.com/articles/en_US/SurveyMonkeyArticleType/Webhooks)) to keep the database synchronized.

Notes
-----

 1. Wufoo is the authoritative datasource, and during a sync all forms, fields and entries not known to Wufoo will be destroyed. (So, don't bother adding things either..)
 2. django-wufoo synchronizes basic data from Wufoo, as we don't need more for now. For example, it only stores the name of a form, and skips fields like `Description`, `Redirect Message` etc. Feel free to extend it.