# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SmsMessageInbox'
        db.create_table('sms_smsmessageinbox', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_control_list', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=480)),
            ('queued_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('sms', ['SmsMessageInbox'])

        # Adding model 'SmsMessageOutbox'
        db.create_table('sms_smsmessageoutbox', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('access_control_list', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=480)),
            ('queued_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('destination', self.gf('django.db.models.fields.CharField')(max_length=48)),
            ('gateway_response', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('sms', ['SmsMessageOutbox'])


    def backwards(self, orm):
        # Deleting model 'SmsMessageInbox'
        db.delete_table('sms_smsmessageinbox')

        # Deleting model 'SmsMessageOutbox'
        db.delete_table('sms_smsmessageoutbox')


    models = {
        'sms.smsmessageinbox': {
            'Meta': {'object_name': 'SmsMessageInbox'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'queued_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '480'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'sms.smsmessageoutbox': {
            'Meta': {'object_name': 'SmsMessageOutbox'},
            'access_control_list': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'destination': ('django.db.models.fields.CharField', [], {'max_length': '48'}),
            'gateway_response': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'queued_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '480'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sms']