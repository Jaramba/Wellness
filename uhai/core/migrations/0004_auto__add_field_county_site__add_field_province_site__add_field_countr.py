# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'County.site'
        db.add_column('core_county', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_county', null=True, to=orm['sites.Site']),
                      keep_default=False)

        # Adding field 'Province.site'
        db.add_column('core_province', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_province', null=True, to=orm['sites.Site']),
                      keep_default=False)

        # Adding field 'Country.site'
        db.add_column('core_country', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='core_country', null=True, to=orm['sites.Site']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'County.site'
        db.delete_column('core_county', 'site_id')

        # Deleting field 'Province.site'
        db.delete_column('core_province', 'site_id')

        # Deleting field 'Country.site'
        db.delete_column('core_country', 'site_id')


    models = {
        'core.country': {
            'Meta': {'object_name': 'Country'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_country'", 'null': 'True', 'to': "orm['sites.Site']"})
        },
        'core.county': {
            'Meta': {'object_name': 'County'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Province']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_county'", 'null': 'True', 'to': "orm['sites.Site']"})
        },
        'core.province': {
            'Meta': {'object_name': 'Province'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'core_province'", 'null': 'True', 'to': "orm['sites.Site']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']