# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Medication'
        db.create_table('medication_medication', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('medication_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('way_taken', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('min_daily_dose', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('max_daily_dose', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('strength', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('strength_unit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('side_effects', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('medication', ['Medication'])

        # Adding model 'Prescription'
        db.create_table('medication_prescription', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reminders.Event'], unique=True, primary_key=True)),
            ('medication', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medication.Medication'])),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('quantity', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal('medication', ['Prescription'])

        # Adding model 'Immunization'
        db.create_table('medication_immunization', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reminders.Event'], unique=True, primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('brand_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('duration_of_protection', self.gf('django.db.models.fields.CharField')(max_length=3, null=True)),
            ('mode_of_delivery', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('follow_up_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True, blank=True)),
        ))
        db.send_create_signal('medication', ['Immunization'])


    def backwards(self, orm):
        # Deleting model 'Medication'
        db.delete_table('medication_medication')

        # Deleting model 'Prescription'
        db.delete_table('medication_prescription')

        # Deleting model 'Immunization'
        db.delete_table('medication_immunization')


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
        'core.ownermodel': {
            'Meta': {'object_name': 'OwnerModel'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'medication.immunization': {
            'Meta': {'object_name': 'Immunization', '_ormbases': ['reminders.Event']},
            'brand_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'duration_of_protection': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reminders.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'follow_up_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'mode_of_delivery': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'})
        },
        'medication.medication': {
            'Meta': {'object_name': 'Medication', '_ormbases': ['core.OwnerModel']},
            'max_daily_dose': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'medication_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'min_daily_dose': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'side_effects': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'strength': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'strength_unit': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'way_taken': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'medication.prescription': {
            'Meta': {'object_name': 'Prescription', '_ormbases': ['reminders.Event']},
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reminders.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'medication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medication.Medication']"}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'quantity': ('django.db.models.fields.SmallIntegerField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'providers.healthcarefacility': {
            'Meta': {'object_name': 'HealthCareFacility'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'official_hospital_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'speciality': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['providers.Speciality']", 'symmetrical': 'False'})
        },
        'providers.healthworker': {
            'Meta': {'object_name': 'HealthWorker'},
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['providers.HealthCareFacility']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_contact_person': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'practice_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'speciality': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['providers.Speciality']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'providers.speciality': {
            'Meta': {'object_name': 'Speciality'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['providers.SpecialityCategory']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'})
        },
        'providers.specialitycategory': {
            'Meta': {'object_name': 'SpecialityCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'reminders.event': {
            'Meta': {'object_name': 'Event', '_ormbases': ['core.OwnerModel']},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['providers.HealthWorker']", 'null': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['medication']