# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WufooForm'
        db.create_table(u'django_wufoo_wufooform', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_wufoo', ['WufooForm'])

        # Adding model 'WufooField'
        db.create_table(u'django_wufoo_wufoofield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wufoo_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('field_type', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_wufoo.WufooForm'])),
        ))
        db.send_create_signal(u'django_wufoo', ['WufooField'])

        # Adding model 'WufooSubField'
        db.create_table(u'django_wufoo_wufoosubfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wufoo_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('default_val', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_wufoo.WufooField'])),
        ))
        db.send_create_signal(u'django_wufoo', ['WufooSubField'])

        # Adding model 'WufooEntry'
        db.create_table(u'django_wufoo_wufooentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('form', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_wufoo.WufooForm'])),
        ))
        db.send_create_signal(u'django_wufoo', ['WufooEntry'])

        # Adding model 'WufooFieldEntry'
        db.create_table(u'django_wufoo_wufoofieldentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('wufoo_entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_wufoo.WufooEntry'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_wufoo.WufooField'])),
            ('subfield', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['django_wufoo.WufooSubField'], null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'django_wufoo', ['WufooFieldEntry'])


    def backwards(self, orm):
        # Deleting model 'WufooForm'
        db.delete_table(u'django_wufoo_wufooform')

        # Deleting model 'WufooField'
        db.delete_table(u'django_wufoo_wufoofield')

        # Deleting model 'WufooSubField'
        db.delete_table(u'django_wufoo_wufoosubfield')

        # Deleting model 'WufooEntry'
        db.delete_table(u'django_wufoo_wufooentry')

        # Deleting model 'WufooFieldEntry'
        db.delete_table(u'django_wufoo_wufoofieldentry')


    models = {
        u'django_wufoo.wufooentry': {
            'Meta': {'object_name': 'WufooEntry'},
            'entry_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooForm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'django_wufoo.wufoofield': {
            'Meta': {'ordering': "['id']", 'object_name': 'WufooField'},
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
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wufoo_entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooEntry']"})
        },
        u'django_wufoo.wufooform': {
            'Meta': {'ordering': "['id']", 'object_name': 'WufooForm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'django_wufoo.wufoosubfield': {
            'Meta': {'ordering': "['id']", 'object_name': 'WufooSubField'},
            'default_val': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['django_wufoo.WufooField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'wufoo_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['django_wufoo']