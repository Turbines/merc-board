# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Posting'
        db.delete_table(u'board_posting')

        # Deleting model 'Mercenary'
        db.delete_table(u'board_mercenary')

        # Deleting model 'Client'
        db.delete_table(u'board_client')

        # Adding model 'ClientProfile'
        db.create_table(u'board_clientprofile', (
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('annoying.fields.AutoOneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'board', ['ClientProfile'])

        # Adding model 'MercenaryProfile'
        db.create_table(u'board_mercenaryprofile', (
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('annoying.fields.AutoOneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'board', ['MercenaryProfile'])


    def backwards(self, orm):
        # Adding model 'Posting'
        db.create_table(u'board_posting', (
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('remote', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(related_name='postings', to=orm['board.Client'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'board', ['Posting'])

        # Adding model 'Mercenary'
        db.create_table(u'board_mercenary', (
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'board', ['Mercenary'])

        # Adding model 'Client'
        db.create_table(u'board_client', (
            ('modified_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'board', ['Client'])

        # Deleting model 'ClientProfile'
        db.delete_table(u'board_clientprofile')

        # Deleting model 'MercenaryProfile'
        db.delete_table(u'board_mercenaryprofile')


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