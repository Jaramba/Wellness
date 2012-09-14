# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Program'
        db.create_table('programs_program', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('concept_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('expected_outcome_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('programs', ['Program'])

        # Adding M2M table for field problems on 'Program'
        db.create_table('programs_program_problems', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('program', models.ForeignKey(orm['programs.program'], null=False)),
            ('problem', models.ForeignKey(orm['records.problem'], null=False))
        ))
        db.create_unique('programs_program_problems', ['program_id', 'problem_id'])

        # Adding model 'EnrolledProgram'
        db.create_table('programs_enrolledprogram', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Program'])),
            ('enrollee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='enrollee', to=orm['patients.Patient'])),
            ('enroller', self.gf('django.db.models.fields.related.ForeignKey')(related_name='enroller', to=orm['auth.User'])),
            ('date_enrolled', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('date_completed', self.gf('django.db.models.fields.DateField')()),
            ('outcome_notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('programs', ['EnrolledProgram'])

        # Adding model 'ProgramWorkflow'
        db.create_table('programs_programworkflow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Program'])),
            ('concept_notes', self.gf('django.db.models.fields.TextField')()),
            ('continued', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('days', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal('programs', ['ProgramWorkflow'])

        # Adding model 'ProgramWorkflowState'
        db.create_table('programs_programworkflowstate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('program_workflow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.ProgramWorkflow'])),
            ('weight', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('initial', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('terminal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('concept_notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('programs', ['ProgramWorkflowState'])

        # Adding model 'Questionnaire'
        db.create_table('programs_questionnaire', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100)),
            ('intro', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('button_text', self.gf('django.db.models.fields.CharField')(default=u'Submit', max_length=50)),
            ('response', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('login_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('programs', ['Questionnaire'])

        # Adding M2M table for field sites on 'Questionnaire'
        db.create_table('programs_questionnaire_sites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('questionnaire', models.ForeignKey(orm['programs.questionnaire'], null=False)),
            ('site', models.ForeignKey(orm['sites.site'], null=False))
        ))
        db.create_unique('programs_questionnaire_sites', ['questionnaire_id', 'site_id'])

        # Adding model 'ProgramQuestionnaire'
        db.create_table('programs_programquestionnaire', (
            ('questionnaire_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['programs.Questionnaire'], unique=True, primary_key=True)),
            ('send_email', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_from', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('email_copies', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email_subject', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('email_message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('program', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Program'])),
        ))
        db.send_create_signal('programs', ['ProgramQuestionnaire'])

        # Adding model 'VitalsQuestionnaire'
        db.create_table('programs_vitalsquestionnaire', (
            ('questionnaire_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['programs.Questionnaire'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('programs', ['VitalsQuestionnaire'])

        # Adding model 'DiagnosisQuestionnaire'
        db.create_table('programs_diagnosisquestionnaire', (
            ('questionnaire_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['programs.Questionnaire'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('programs', ['DiagnosisQuestionnaire'])

        # Adding model 'Field'
        db.create_table('programs_field', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=100, blank=True)),
            ('field_type', self.gf('django.db.models.fields.IntegerField')()),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('choices', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('default', self.gf('django.db.models.fields.CharField')(max_length=2000, blank=True)),
            ('placeholder_text', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('help_text', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['programs.Questionnaire'])),
            ('order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('programs', ['Field'])

        # Adding model 'QuestionnaireResponseEntry'
        db.create_table('programs_questionnaireresponseentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('questionnaire', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entries', to=orm['programs.Questionnaire'])),
        ))
        db.send_create_signal('programs', ['QuestionnaireResponseEntry'])

        # Adding model 'QuestionnaireFieldResponseEntry'
        db.create_table('programs_questionnairefieldresponseentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Field'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fields', to=orm['programs.QuestionnaireResponseEntry'])),
        ))
        db.send_create_signal('programs', ['QuestionnaireFieldResponseEntry'])


    def backwards(self, orm):
        # Deleting model 'Program'
        db.delete_table('programs_program')

        # Removing M2M table for field problems on 'Program'
        db.delete_table('programs_program_problems')

        # Deleting model 'EnrolledProgram'
        db.delete_table('programs_enrolledprogram')

        # Deleting model 'ProgramWorkflow'
        db.delete_table('programs_programworkflow')

        # Deleting model 'ProgramWorkflowState'
        db.delete_table('programs_programworkflowstate')

        # Deleting model 'Questionnaire'
        db.delete_table('programs_questionnaire')

        # Removing M2M table for field sites on 'Questionnaire'
        db.delete_table('programs_questionnaire_sites')

        # Deleting model 'ProgramQuestionnaire'
        db.delete_table('programs_programquestionnaire')

        # Deleting model 'VitalsQuestionnaire'
        db.delete_table('programs_vitalsquestionnaire')

        # Deleting model 'DiagnosisQuestionnaire'
        db.delete_table('programs_diagnosisquestionnaire')

        # Deleting model 'Field'
        db.delete_table('programs_field')

        # Deleting model 'QuestionnaireResponseEntry'
        db.delete_table('programs_questionnaireresponseentry')

        # Deleting model 'QuestionnaireFieldResponseEntry'
        db.delete_table('programs_questionnairefieldresponseentry')


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
            'contact_person_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_providers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['insurance.HealthInsuranceProvider']", 'symmetrical': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'insurance.healthinsuranceprovider': {
            'Meta': {'object_name': 'HealthInsuranceProvider'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'insurance.insurance': {
            'Meta': {'object_name': 'Insurance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
            'coverage_end_date': ('django.db.models.fields.DateField', [], {}),
            'coverage_start_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['insurance.Insurance']"}),
            'notes': ('django.db.models.fields.TextField', [], {}),
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
        'programs.diagnosisquestionnaire': {
            'Meta': {'object_name': 'DiagnosisQuestionnaire', '_ormbases': ['programs.Questionnaire']},
            'questionnaire_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['programs.Questionnaire']", 'unique': 'True', 'primary_key': 'True'})
        },
        'programs.enrolledprogram': {
            'Meta': {'object_name': 'EnrolledProgram'},
            'date_completed': ('django.db.models.fields.DateField', [], {}),
            'date_enrolled': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'enrollee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'enrollee'", 'to': "orm['patients.Patient']"}),
            'enroller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'enroller'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outcome_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.Program']"})
        },
        'programs.field': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Field'},
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.IntegerField', [], {}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'placeholder_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['programs.Questionnaire']"}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'programs.program': {
            'Meta': {'object_name': 'Program'},
            'concept_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expected_outcome_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'problems': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['records.Problem']", 'symmetrical': 'False'})
        },
        'programs.programquestionnaire': {
            'Meta': {'object_name': 'ProgramQuestionnaire', '_ormbases': ['programs.Questionnaire']},
            'email_copies': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.Program']"}),
            'questionnaire_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['programs.Questionnaire']", 'unique': 'True', 'primary_key': 'True'}),
            'send_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'programs.programworkflow': {
            'Meta': {'object_name': 'ProgramWorkflow'},
            'concept_notes': ('django.db.models.fields.TextField', [], {}),
            'continued': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'days': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.Program']"})
        },
        'programs.programworkflowstate': {
            'Meta': {'object_name': 'ProgramWorkflowState'},
            'concept_notes': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'program_workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.ProgramWorkflow']"}),
            'terminal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'programs.questionnaire': {
            'Meta': {'object_name': 'Questionnaire'},
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'programs.questionnairefieldresponseentry': {
            'Meta': {'object_name': 'QuestionnaireFieldResponseEntry'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['programs.QuestionnaireResponseEntry']"}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.Field']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'})
        },
        'programs.questionnaireresponseentry': {
            'Meta': {'object_name': 'QuestionnaireResponseEntry'},
            'entry_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['programs.Questionnaire']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'programs.vitalsquestionnaire': {
            'Meta': {'object_name': 'VitalsQuestionnaire', '_ormbases': ['programs.Questionnaire']},
            'questionnaire_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['programs.Questionnaire']", 'unique': 'True', 'primary_key': 'True'})
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
        },
        'records.icd10block': {
            'Meta': {'object_name': 'ICD10Block'},
            'chapter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.ICD10Chapter']"}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'min_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'records.icd10chapter': {
            'Meta': {'object_name': 'ICD10Chapter'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'records.problem': {
            'Meta': {'object_name': 'Problem'},
            'cause': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'icd10_block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.ICD10Block']", 'null': 'True'}),
            'icd10_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['records.ProblemType']", 'null': 'True'})
        },
        'records.problemtype': {
            'Meta': {'object_name': 'ProblemType'},
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['programs']