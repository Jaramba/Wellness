# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'VitalsQuestionnaire'
        db.delete_table('programs_vitalsquestionnaire')

        # Adding model 'FieldLevel'
        db.create_table('programs_fieldlevel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now=True, blank=True)),
            ('date_changed', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, auto_now_add=True, blank=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['programs.Field'])),
            ('range', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('access_control_list', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
        ))
        db.send_create_signal('programs', ['FieldLevel'])

        # Adding field 'ProgramWorkflowState.owner'
        db.add_column('programs_programworkflowstate', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'ProgramWorkflowState.access_control_list'
        db.add_column('programs_programworkflowstate', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'QuestionnaireFieldResponseEntry.owner'
        db.add_column('programs_questionnairefieldresponseentry', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'QuestionnaireFieldResponseEntry.access_control_list'
        db.add_column('programs_questionnairefieldresponseentry', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'Field.owner'
        db.add_column('programs_field', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'Field.access_control_list'
        db.add_column('programs_field', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'EnrolledProgram.owner'
        db.add_column('programs_enrolledprogram', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'EnrolledProgram.access_control_list'
        db.add_column('programs_enrolledprogram', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Deleting field 'Program.owner'
        db.delete_column('programs_program', 'owner_id')

        # Adding field 'Program.user'
        db.add_column('programs_program', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'Program.access_control_list'
        db.add_column('programs_program', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'QuestionnaireResponseEntry.owner'
        db.add_column('programs_questionnaireresponseentry', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'QuestionnaireResponseEntry.access_control_list'
        db.add_column('programs_questionnaireresponseentry', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'ProgramWorkflow.owner'
        db.add_column('programs_programworkflow', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'ProgramWorkflow.access_control_list'
        db.add_column('programs_programworkflow', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)

        # Adding field 'Questionnaire.owner'
        db.add_column('programs_questionnaire', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Adding field 'Questionnaire.access_control_list'
        db.add_column('programs_questionnaire', 'access_control_list',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'VitalsQuestionnaire'
        db.create_table('programs_vitalsquestionnaire', (
            ('questionnaire_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['programs.Questionnaire'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('programs', ['VitalsQuestionnaire'])

        # Deleting model 'FieldLevel'
        db.delete_table('programs_fieldlevel')

        # Deleting field 'ProgramWorkflowState.owner'
        db.delete_column('programs_programworkflowstate', 'owner_id')

        # Deleting field 'ProgramWorkflowState.access_control_list'
        db.delete_column('programs_programworkflowstate', 'access_control_list')

        # Deleting field 'QuestionnaireFieldResponseEntry.owner'
        db.delete_column('programs_questionnairefieldresponseentry', 'owner_id')

        # Deleting field 'QuestionnaireFieldResponseEntry.access_control_list'
        db.delete_column('programs_questionnairefieldresponseentry', 'access_control_list')

        # Deleting field 'Field.owner'
        db.delete_column('programs_field', 'owner_id')

        # Deleting field 'Field.access_control_list'
        db.delete_column('programs_field', 'access_control_list')

        # Deleting field 'EnrolledProgram.owner'
        db.delete_column('programs_enrolledprogram', 'owner_id')

        # Deleting field 'EnrolledProgram.access_control_list'
        db.delete_column('programs_enrolledprogram', 'access_control_list')

        # Adding field 'Program.owner'
        db.add_column('programs_program', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True),
                      keep_default=False)

        # Deleting field 'Program.user'
        db.delete_column('programs_program', 'user_id')

        # Deleting field 'Program.access_control_list'
        db.delete_column('programs_program', 'access_control_list')

        # Deleting field 'QuestionnaireResponseEntry.owner'
        db.delete_column('programs_questionnaireresponseentry', 'owner_id')

        # Deleting field 'QuestionnaireResponseEntry.access_control_list'
        db.delete_column('programs_questionnaireresponseentry', 'access_control_list')

        # Deleting field 'ProgramWorkflow.owner'
        db.delete_column('programs_programworkflow', 'owner_id')

        # Deleting field 'ProgramWorkflow.access_control_list'
        db.delete_column('programs_programworkflow', 'access_control_list')

        # Deleting field 'Questionnaire.owner'
        db.delete_column('programs_questionnaire', 'owner_id')

        # Deleting field 'Questionnaire.access_control_list'
        db.delete_column('programs_questionnaire', 'access_control_list')


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
        'programs.diagnosisquestionnaire': {
            'Meta': {'object_name': 'DiagnosisQuestionnaire', '_ormbases': ['programs.Questionnaire']},
            'questionnaire_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['programs.Questionnaire']", 'unique': 'True', 'primary_key': 'True'})
        },
        'programs.enrolledprogram': {
            'Meta': {'object_name': 'EnrolledProgram'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'date_completed': ('django.db.models.fields.DateField', [], {}),
            'date_enrolled': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'enrollee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'enrollee'", 'to': "orm['patients.Patient']"}),
            'enroller': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'enroller'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outcome_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.Program']"})
        },
        'programs.field': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Field'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.IntegerField', [], {}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'placeholder_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['programs.Questionnaire']"}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'programs.fieldlevel': {
            'Meta': {'object_name': 'FieldLevel'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'date_changed': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now_add': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.Field']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'range': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '200'})
        },
        'programs.program': {
            'Meta': {'object_name': 'Program'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'concept_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'expected_outcome_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'problems': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['records.Problem']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
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
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'concept_notes': ('django.db.models.fields.TextField', [], {}),
            'continued': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'days': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'program': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.Program']"})
        },
        'programs.programworkflowstate': {
            'Meta': {'object_name': 'ProgramWorkflowState'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'concept_notes': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'program_workflow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.ProgramWorkflow']"}),
            'terminal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'programs.questionnaire': {
            'Meta': {'object_name': 'Questionnaire'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'programs.questionnairefieldresponseentry': {
            'Meta': {'object_name': 'QuestionnaireFieldResponseEntry'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': "orm['programs.QuestionnaireResponseEntry']"}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['programs.Field']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'})
        },
        'programs.questionnaireresponseentry': {
            'Meta': {'object_name': 'QuestionnaireResponseEntry'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'entry_time': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'}),
            'questionnaire': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': "orm['programs.Questionnaire']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'respondent'", 'to': "orm['auth.User']"})
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