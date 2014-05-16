# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    depends_on = (
        ('accounts', "0001_initial"),
    )

    def forwards(self, orm):
        # Adding model 'MercenaryProfile'
        db.create_table(u'board_mercenaryprofile', (
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('annoying.fields.AutoOneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'board', ['MercenaryProfile'])

        # Adding model 'ClientProfile'
        db.create_table(u'board_clientprofile', (
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('annoying.fields.AutoOneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'board', ['ClientProfile'])


    def backwards(self, orm):
        # Deleting model 'MercenaryProfile'
        db.delete_table(u'board_mercenaryprofile')

        # Deleting model 'ClientProfile'
        db.delete_table(u'board_clientprofile')


    models = {
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'board.clientprofile': {
            'Meta': {'object_name': 'ClientProfile'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('annoying.fields.AutoOneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'board.mercenaryprofile': {
            'Meta': {'object_name': 'MercenaryProfile'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modified_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('annoying.fields.AutoOneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['board']