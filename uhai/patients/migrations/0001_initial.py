# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Patient'
        db.create_table('patients_patient', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True)),
            ('blood_group', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(default=0, max_length=5, null=True)),
            ('height', self.gf('django.db.models.fields.CharField')(default=0, max_length=7, null=True)),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['insurance.EmployerCompany'], null=True)),
        ))
        db.send_create_signal('patients', ['Patient'])

        # Adding model 'RelationshipType'
        db.create_table('patients_relationshiptype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('a_is_to_b', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('b_is_to_a', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('preffered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('patients', ['RelationshipType'])

        # Adding model 'Relationship'
        db.create_table('patients_relationship', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('person_a', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person_a', to=orm['auth.User'])),
            ('person_b', self.gf('django.db.models.fields.related.ForeignKey')(related_name='person_b', to=orm['auth.User'])),
            ('next_of_kin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.RelationshipType'])),
        ))
        db.send_create_signal('patients', ['Relationship'])

        # Adding model 'PatientEmergencyContact'
        db.create_table('patients_patientemergencycontact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('next_of_kin', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=72, null=True)),
            ('mobile_phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('home_phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('work_phone', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('national_id', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('date_edited', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('patients', ['PatientEmergencyContact'])


    def backwards(self, orm):
        # Deleting model 'Patient'
        db.delete_table('patients_patient')

        # Deleting model 'RelationshipType'
        db.delete_table('patients_relationshiptype')

        # Deleting model 'Relationship'
        db.delete_table('patients_relationship')

        # Deleting model 'PatientEmergencyContact'
        db.delete_table('patients_patientemergencycontact')


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
        'patients.patientemergencycontact': {
            'Meta': {'object_name': 'PatientEmergencyContact'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '72', 'null': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'national_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'next_of_kin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'patients.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_of_kin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'person_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person_a'", 'to': "orm['auth.User']"}),
            'person_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'person_b'", 'to': "orm['auth.User']"}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.RelationshipType']"})
        },
        'patients.relationshiptype': {
            'Meta': {'object_name': 'RelationshipType'},
            'a_is_to_b': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'b_is_to_a': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preffered': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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

    complete_apps = ['patients']