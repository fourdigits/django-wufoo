# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WufooField.choices'
        db.add_column(u'django_wufoo_wufoofield', 'choices',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WufooField.choices'
        db.delete_column(u'django_wufoo_wufoofield', 'choices')


    models = {
        u'django_wufoo.wufooentry': {
            'Meta': {'object_name': 'WufooEntry'},
            'entry_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooForm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'django_wufoo.wufoofield': {
            'Meta': {'ordering': "['id']", 'object_name': 'WufooField'},
            'choices': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooForm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wufoo_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'django_wufoo.wufoofieldentry': {
            'Meta': {'ordering': "['field', 'subfield']", 'object_name': 'WufooFieldEntry'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subfield': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooSubField']", 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {}),
            'wufoo_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooEntry']"})
        },
        u'django_wufoo.wufooform': {
            'Meta': {'ordering': "['id']", 'object_name': 'WufooForm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'django_wufoo.wufoosubfield': {
            'Meta': {'ordering': "['id']", 'object_name': 'WufooSubField'},
            'default_val': ('django.db.models.fields.TextField', [], {}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wufoo_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['django_wufoo']