# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('core_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('core', ['Country'])

        # Adding model 'Province'
        db.create_table('core_province', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Country'])),
        ))
        db.send_create_signal('core', ['Province'])

        # Adding model 'County'
        db.create_table('core_county', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Province'])),
        ))
        db.send_create_signal('core', ['County'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('core_country')

        # Deleting model 'Province'
        db.delete_table('core_province')

        # Deleting model 'County'
        db.delete_table('core_county')


    models = {
        'core.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'core.county': {
            'Meta': {'object_name': 'County'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Province']"})
        },
        'core.province': {
            'Meta': {'object_name': 'Province'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['core']