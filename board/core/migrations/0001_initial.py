# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'core_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
        ))
        db.send_create_signal(u'core', ['User'])

        # Adding model 'Mercenary'
        db.create_table(u'core_mercenary', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Mercenary'])

        # Adding model 'Client'
        db.create_table(u'core_client', (
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['core.User'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Client'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'core_user')

        # Deleting model 'Mercenary'
        db.delete_table(u'core_mercenary')

        # Deleting model 'Client'
        db.delete_table(u'core_client')


    models = {
        u'core.client': {
            'Meta': {'object_name': 'Client'},
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.mercenary': {
            'Meta': {'object_name': 'Mercenary'},
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'core.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['core']