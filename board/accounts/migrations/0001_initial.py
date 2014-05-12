# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'accounts_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'accounts', ['User'])

        # Adding model 'Mercenary'
        db.create_table(u'accounts_mercenary', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'accounts', ['Mercenary'])

        # Adding model 'Client'
        db.create_table(u'accounts_client', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'accounts', ['Client'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'accounts_user')

        # Deleting model 'Mercenary'
        db.delete_table(u'accounts_mercenary')

        # Deleting model 'Client'
        db.delete_table(u'accounts_client')


    models = {
        u'accounts.client': {
            'Meta': {'object_name': 'Client'},
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounts.mercenary': {
            'Meta': {'object_name': 'Mercenary'},
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounts.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['accounts']