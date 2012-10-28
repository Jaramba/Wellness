# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'OwnerModel.owner'
        db.delete_column('core_ownermodel', 'owner_id')

        # Adding field 'OwnerModel.username'
        db.add_column('core_ownermodel', 'username',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'OwnerModel.owner'
        db.add_column('core_ownermodel', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'OwnerModel.username'
        db.delete_column('core_ownermodel', 'username')


    models = {
        'core.country': {
            'Meta': {'object_name': 'Country', '_ormbases': ['core.OwnerModel']},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'})
        },
        'core.county': {
            'Meta': {'object_name': 'County', '_ormbases': ['core.OwnerModel']},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['utils.Province']"})
        },
        'core.crudaccessdict': {
            'Meta': {'object_name': 'CRUDAccessDict'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.OwnerModel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '240', 'db_index': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '240', 'db_index': 'True'})
        },
        'core.ownermodel': {
            'Meta': {'object_name': 'OwnerModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'core.province': {
            'Meta': {'object_name': 'Province', '_ormbases': ['core.OwnerModel']},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['utils.Country']"}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']