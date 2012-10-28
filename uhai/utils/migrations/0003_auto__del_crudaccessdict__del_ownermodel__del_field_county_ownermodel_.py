# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'CRUDAccessDict'
        db.delete_table('core_crudaccessdict')

        # Deleting model 'OwnerModel'
        db.delete_table('core_ownermodel')

        # Deleting field 'County.ownermodel_ptr'
        db.delete_column('core_county', 'ownermodel_ptr_id')

        # Adding field 'County.id'
        db.add_column('core_county', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=5, primary_key=True),
                      keep_default=False)

        # Adding field 'County.access_control_list'
        db.add_column('core_county', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Deleting field 'Province.ownermodel_ptr'
        db.delete_column('core_province', 'ownermodel_ptr_id')

        # Adding field 'Province.id'
        db.add_column('core_province', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=6, primary_key=True),
                      keep_default=False)

        # Adding field 'Province.access_control_list'
        db.add_column('core_province', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Deleting field 'Country.ownermodel_ptr'
        db.delete_column('core_country', 'ownermodel_ptr_id')

        # Adding field 'Country.id'
        db.add_column('core_country', 'id',
                      self.gf('django.db.models.fields.AutoField')(default=67, primary_key=True),
                      keep_default=False)

        # Adding field 'Country.access_control_list'
        db.add_column('core_country', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'CRUDAccessDict'
        db.create_table('core_crudaccessdict', (
            ('value', self.gf('django.db.models.fields.CharField')(max_length=240, db_index=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.OwnerModel'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=240, db_index=True)),
        ))
        db.send_create_signal('core', ['CRUDAccessDict'])

        # Adding model 'OwnerModel'
        db.create_table('core_ownermodel', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('core', ['OwnerModel'])

        # Adding field 'County.ownermodel_ptr'
        db.add_column('core_county', 'ownermodel_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=datetime.datetime(2012, 9, 17, 0, 0), to=orm['core.OwnerModel'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'County.id'
        db.delete_column('core_county', 'id')

        # Deleting field 'County.access_control_list'
        db.delete_column('core_county', 'access_control_list')


        # User chose to not deal with backwards NULL issues for 'Province.ownermodel_ptr'
        raise RuntimeError("Cannot reverse this migration. 'Province.ownermodel_ptr' and its values cannot be restored.")
        # Deleting field 'Province.id'
        db.delete_column('core_province', 'id')

        # Deleting field 'Province.access_control_list'
        db.delete_column('core_province', 'access_control_list')

        # Adding field 'Country.ownermodel_ptr'
        db.add_column('core_country', 'ownermodel_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['core.OwnerModel'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Country.id'
        db.delete_column('core_country', 'id')

        # Deleting field 'Country.access_control_list'
        db.delete_column('core_country', 'access_control_list')


    models = {
        'utils.country': {
            'Meta': {'object_name': 'Country'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'utils.county': {
            'Meta': {'object_name': 'County'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'province': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['utils.Province']"})
        },
        'utils.province': {
            'Meta': {'object_name': 'Province'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['utils.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['core']