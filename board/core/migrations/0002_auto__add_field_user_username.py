# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.username'
        db.add_column(u'core_user', 'username',
                      self.gf('django.db.models.fields.CharField')(default='username', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.username'
        db.delete_column(u'core_user', 'username')


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
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['core']