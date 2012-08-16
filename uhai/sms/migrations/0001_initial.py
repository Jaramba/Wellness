# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Message'
        db.create_table('sms_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('to', self.gf('django.db.models.fields.CharField')(max_length=14)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('queued_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('sent_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('gateway_response', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('sms', ['Message'])


    def backwards(self, orm):
        
        # Deleting model 'Message'
        db.delete_table('sms_message')


    models = {
        'sms.message': {
            'Meta': {'object_name': 'Message'},
            'gateway_response': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'queued_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sent_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'to': ('django.db.models.fields.CharField', [], {'max_length': '14'})
        }
    }

    complete_apps = ['sms']
