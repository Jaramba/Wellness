# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CRUDAccessDict'
        db.create_table('core_crudaccessdict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('container', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.OwnerModel'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=240, db_index=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=240, db_index=True)),
        ))
        db.send_create_signal('core', ['CRUDAccessDict'])

        # Adding model 'OwnerModel'
        db.create_table('core_ownermodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal('core', ['OwnerModel'])

        # Adding model 'Country'
        db.create_table('core_country', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=4)),
        ))
        db.send_create_signal('core', ['Country'])

        # Adding model 'Province'
        db.create_table('core_province', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['utils.Country'])),
        ))
        db.send_create_signal('core', ['Province'])

        # Adding model 'County'
        db.create_table('core_county', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('iso', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('province', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['utils.Province'])),
        ))
        db.send_create_signal('core', ['County'])


    def backwards(self, orm):
        # Deleting model 'CRUDAccessDict'
        db.delete_table('core_crudaccessdict')

        # Deleting model 'OwnerModel'
        db.delete_table('core_ownermodel')

        # Deleting model 'Country'
        db.delete_table('core_country')

        # Deleting model 'Province'
        db.delete_table('core_province')

        # Deleting model 'County'
        db.delete_table('core_county')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'utils.country': {
            'Meta': {'object_name': 'Country', '_ormbases': ['core.OwnerModel']},
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'})
        },
        'utils.county': {
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
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'utils.province': {
            'Meta': {'object_name': 'Province', '_ormbases': ['core.OwnerModel']},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['utils.Country']"}),
            'iso': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['core']