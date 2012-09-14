# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SpecialityCategory'
        db.create_table('providers_specialitycategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('providers', ['SpecialityCategory'])

        # Adding model 'Speciality'
        db.create_table('providers_speciality', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['providers.SpecialityCategory'], null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('providers', ['Speciality'])

        # Adding model 'HealthCareFacility'
        db.create_table('providers_healthcarefacility', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('official_hospital_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal('providers', ['HealthCareFacility'])

        # Adding M2M table for field speciality on 'HealthCareFacility'
        db.create_table('providers_healthcarefacility_speciality', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('healthcarefacility', models.ForeignKey(orm['providers.healthcarefacility'], null=False)),
            ('speciality', models.ForeignKey(orm['providers.speciality'], null=False))
        ))
        db.create_unique('providers_healthcarefacility_speciality', ['healthcarefacility_id', 'speciality_id'])

        # Adding model 'HealthWorker'
        db.create_table('providers_healthworker', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_contact_person', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['providers.HealthCareFacility'])),
            ('practice_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal('providers', ['HealthWorker'])

        # Adding M2M table for field speciality on 'HealthWorker'
        db.create_table('providers_healthworker_speciality', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('healthworker', models.ForeignKey(orm['providers.healthworker'], null=False)),
            ('speciality', models.ForeignKey(orm['providers.speciality'], null=False))
        ))
        db.create_unique('providers_healthworker_speciality', ['healthworker_id', 'speciality_id'])

        # Adding model 'PatientProvider'
        db.create_table('providers_patientprovider', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Patient'])),
            ('provider', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['providers.HealthWorker'])),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('providers', ['PatientProvider'])


    def backwards(self, orm):
        # Deleting model 'SpecialityCategory'
        db.delete_table('providers_specialitycategory')

        # Deleting model 'Speciality'
        db.delete_table('providers_speciality')

        # Deleting model 'HealthCareFacility'
        db.delete_table('providers_healthcarefacility')

        # Removing M2M table for field speciality on 'HealthCareFacility'
        db.delete_table('providers_healthcarefacility_speciality')

        # Deleting model 'HealthWorker'
        db.delete_table('providers_healthworker')

        # Removing M2M table for field speciality on 'HealthWorker'
        db.delete_table('providers_healthworker_speciality')

        # Deleting model 'PatientProvider'
        db.delete_table('providers_patientprovider')


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
        'insurance.employercompany': {
            'Meta': {'object_name': 'EmployerCompany'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'contact_person_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_providers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['insurance.HealthInsuranceProvider']", 'symmetrical': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'insurance.healthinsuranceprovider': {
            'Meta': {'object_name': 'HealthInsuranceProvider'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'insurance.insurance': {
            'Meta': {'object_name': 'Insurance'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'plan_id': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'plan_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'policy_provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['insurance.HealthInsuranceProvider']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['insurance.InsuranceType']"})
        },
        'insurance.insurancetype': {
            'Meta': {'object_name': 'InsuranceType'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'insurance.patientinsurance': {
            'Meta': {'object_name': 'PatientInsurance'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'coverage_end_date': ('django.db.models.fields.DateField', [], {}),
            'coverage_start_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['insurance.Insurance']"}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'subscriber_policy_id': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'patients.patient': {
            'Meta': {'object_name': 'Patient'},
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['insurance.EmployerCompany']", 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '7', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['insurance.Insurance']", 'through': "orm['insurance.PatientInsurance']", 'symmetrical': 'False'}),
            'providers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['providers.HealthWorker']", 'through': "orm['providers.PatientProvider']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '5', 'null': 'True'})
        },
        'providers.healthcarefacility': {
            'Meta': {'object_name': 'HealthCareFacility'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'official_hospital_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
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
        'providers.patientprovider': {
            'Meta': {'object_name': 'PatientProvider'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['providers.HealthWorker']"})
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
        }
    }

    complete_apps = ['providers']