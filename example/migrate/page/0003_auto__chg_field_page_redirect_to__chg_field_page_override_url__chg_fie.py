# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.redirect_to'
        db.alter_column(u'page_page', 'redirect_to', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Page.override_url'
        db.alter_column(u'page_page', 'override_url', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Page._cached_url'
        db.alter_column(u'page_page', '_cached_url', self.gf('django.db.models.fields.CharField')(max_length=255))
        # Deleting field 'MediaFileContent.position'
        db.delete_column('page_page_mediafilecontent', 'position')

        # Adding field 'MediaFileContent.type'
        db.add_column(u'page_page_mediafilecontent', 'type',
                      self.gf('django.db.models.fields.CharField')(default='default', max_length=20),
                      keep_default=False)


        # Changing field 'MediaFileContent.mediafile'
        db.alter_column(u'page_page_mediafilecontent', 'mediafile_id', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(to=orm['medialibrary.MediaFile']))

    def backwards(self, orm):

        # Changing field 'Page.redirect_to'
        db.alter_column(u'page_page', 'redirect_to', self.gf('django.db.models.fields.CharField')(max_length=300))

        # Changing field 'Page.override_url'
        db.alter_column(u'page_page', 'override_url', self.gf('django.db.models.fields.CharField')(max_length=300))

        # Changing field 'Page._cached_url'
        db.alter_column(u'page_page', '_cached_url', self.gf('django.db.models.fields.CharField')(max_length=300))
        # Adding field 'MediaFileContent.position'
        db.add_column('page_page_mediafilecontent', 'position',
                      self.gf('django.db.models.fields.CharField')(default='block', max_length=10),
                      keep_default=False)

        # Deleting field 'MediaFileContent.type'
        db.delete_column(u'page_page_mediafilecontent', 'type')


        # Changing field 'MediaFileContent.mediafile'
        db.alter_column(u'page_page_mediafilecontent', 'mediafile_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medialibrary.MediaFile']))

    models = {
        'articles.category': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Category'},
            'access_groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'local_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order_by': ('django.db.models.fields.CharField', [], {'default': "'-publication_date'", 'max_length': '30'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['articles.Category']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'medialibrary.category': {
            'Meta': {'ordering': "['parent__title', 'title']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'medialibrary.mediafile': {
            'Meta': {'ordering': "['-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'page.applicationcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'ApplicationContent', 'db_table': "u'page_page_applicationcontent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parameters': ('feincms.contrib.fields.JSONField', [], {'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applicationcontent_set'", 'to': u"orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'urlconf_path': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'page.articlecategorylist': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'ArticleCategoryList', 'db_table': "u'page_page_articlecategorylist'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['articles.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'layout': ('django.db.models.fields.CharField', [], {'default': "'left'", 'max_length': '10'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'articlecategorylist_set'", 'to': u"orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'page.imagecontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'ImageContent', 'db_table': "u'page_page_imagecontent'"},
            'alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imagecontent_set'", 'to': u"orm['page.Page']"}),
            'position': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '10'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'page.mediafilecontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'MediaFileContent', 'db_table': "u'page_page_mediafilecontent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'related_name': "'+'", 'to': u"orm['medialibrary.MediaFile']"}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mediafilecontent_set'", 'to': u"orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'})
        },
        u'page.page': {
            'Meta': {'ordering': "['tree_id', 'lft']", 'object_name': 'Page'},
            '_cached_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'db_index': 'True', 'blank': 'True'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'navigation_extension': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'override_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['page.Page']"}),
            'redirect_to': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'template_key': ('django.db.models.fields.CharField', [], {'default': "'base'", 'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        u'page.rawcontent': {
            'Meta': {'ordering': "['ordering']", 'object_name': 'RawContent', 'db_table': "u'page_page_rawcontent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rawcontent_set'", 'to': u"orm['page.Page']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['page']