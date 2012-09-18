# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProblemType'
        db.create_table('records_problemtype', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('records', ['ProblemType'])

        # Adding model 'Problem'
        db.create_table('records_problem', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.ProblemType'], null=True)),
            ('icd10_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('icd10_block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.ICD10Block'], null=True)),
            ('detail', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('cause', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('records', ['Problem'])

        # Adding model 'ICD10Chapter'
        db.create_table('records_icd10chapter', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('records', ['ICD10Chapter'])

        # Adding model 'ICD10Block'
        db.create_table('records_icd10block', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('min_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('max_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('chapter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.ICD10Chapter'])),
        ))
        db.send_create_signal('records', ['ICD10Block'])

        # Adding model 'EncounterType'
        db.create_table('records_encountertype', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('records', ['EncounterType'])

        # Adding model 'Encounter'
        db.create_table('records_encounter', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reminders.Event'], unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.EncounterType'])),
            ('patient_complience', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('observation_notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('records', ['Encounter'])

        # Adding model 'Order'
        db.create_table('records_order', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Encounter'])),
            ('concept_notes', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('instructions', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('discontinued', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('discontinued_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('discontinued_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['providers.HealthWorker'])),
            ('discontinued_reason', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('records', ['Order'])

        # Adding model 'Diagnosis'
        db.create_table('records_diagnosis', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('problem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Problem'])),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Encounter'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('records', ['Diagnosis'])

        # Adding model 'Test'
        db.create_table('records_test', (
            ('ownermodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.OwnerModel'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('expected_outcomes', self.gf('django.db.models.fields.TextField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('records', ['Test'])

        # Adding model 'ProblemTest'
        db.create_table('records_problemtest', (
            ('test_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['records.Test'], unique=True, primary_key=True)),
            ('problem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Problem'])),
        ))
        db.send_create_signal('records', ['ProblemTest'])

        # Adding model 'EncounterTest'
        db.create_table('records_encountertest', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reminders.Event'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.Test'])),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('records', ['EncounterTest'])

        # Adding model 'EncounterTestResult'
        db.create_table('records_encountertestresult', (
            ('event_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['reminders.Event'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('encounter_test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['records.EncounterTest'])),
            ('inference', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('records', ['EncounterTestResult'])


    def backwards(self, orm):
        # Deleting model 'ProblemType'
        db.delete_table('records_problemtype')

        # Deleting model 'Problem'
        db.delete_table('records_problem')

        # Deleting model 'ICD10Chapter'
        db.delete_table('records_icd10chapter')

        # Deleting model 'ICD10Block'
        db.delete_table('records_icd10block')

        # Deleting model 'EncounterType'
        db.delete_table('records_encountertype')

        # Deleting model 'Encounter'
        db.delete_table('records_encounter')

        # Deleting model 'Order'
        db.delete_table('records_order')

        # Deleting model 'Diagnosis'
        db.delete_table('records_diagnosis')

        # Deleting model 'Test'
        db.delete_table('records_test')

        # Deleting model 'ProblemTest'
        db.delete_table('records_problemtest')

        # Deleting model 'EncounterTest'
        db.delete_table('records_encountertest')

        # Deleting model 'EncounterTestResult'
        db.delete_table('records_encountertestresult')


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
        'records.diagnosis': {
            'Meta': {'object_name': 'Diagnosis', '_ormbases': ['core.OwnerModel']},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Encounter']"}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Problem']"})
        },
        'records.encounter': {
            'Meta': {'object_name': 'Encounter', '_ormbases': ['reminders.Event']},
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reminders.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'observation_notes': ('django.db.models.fields.TextField', [], {}),
            'patient_complience': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.EncounterType']"})
        },
        'records.encountertest': {
            'Meta': {'object_name': 'EncounterTest', '_ormbases': ['reminders.Event']},
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reminders.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Test']"})
        },
        'records.encountertestresult': {
            'Meta': {'object_name': 'EncounterTestResult', '_ormbases': ['reminders.Event']},
            'encounter_test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.EncounterTest']"}),
            'event_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['reminders.Event']", 'unique': 'True', 'primary_key': 'True'}),
            'inference': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'records.encountertype': {
            'Meta': {'object_name': 'EncounterType'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'records.icd10block': {
            'Meta': {'object_name': 'ICD10Block'},
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.ICD10Chapter']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'max_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'min_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'records.icd10chapter': {
            'Meta': {'object_name': 'ICD10Chapter'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'records.order': {
            'Meta': {'object_name': 'Order', '_ormbases': ['core.OwnerModel']},
            'concept_notes': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'discontinued': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'discontinued_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['providers.HealthWorker']"}),
            'discontinued_date': ('django.db.models.fields.DateTimeField', [], {}),
            'discontinued_reason': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Encounter']"}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'})
        },
        'records.problem': {
            'Meta': {'object_name': 'Problem', '_ormbases': ['core.OwnerModel']},
            'cause': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'icd10_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.ICD10Block']", 'null': 'True'}),
            'icd10_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.ProblemType']", 'null': 'True'})
        },
        'records.problemtest': {
            'Meta': {'object_name': 'ProblemTest', '_ormbases': ['records.Test']},
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.Problem']"}),
            'test_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['records.Test']", 'unique': 'True', 'primary_key': 'True'})
        },
        'records.problemtype': {
            'Meta': {'object_name': 'ProblemType'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'records.test': {
            'Meta': {'object_name': 'Test'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expected_outcomes': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'ownermodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.OwnerModel']", 'unique': 'True', 'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
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

    complete_apps = ['records']