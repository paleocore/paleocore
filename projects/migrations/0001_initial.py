# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('base', '0001_initial'),
        #('standard', '0003_term_term_ordering'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_name', models.CharField(unique=True, max_length=50)),
                ('full_name', models.CharField(unique=True, max_length=300, db_index=True)),
                ('paleocore_appname', models.CharField(max_length=200, null=True, choices=[(b'mptt', b'mptt'), (b'compressor', b'compressor'), (b'easy_thumbnails', b'easy_thumbnails'), (b'fiber', b'fiber'), (b'API', b'API'), (b'tastypie', b'tastypie'), (b'login', b'login'), (b'base', b'base'), (b'standard', b'standard'), (b'efossils', b'efossils'), (b'paleosites', b'paleosites'), (b'olwidget', b'olwidget'), (b'origins', b'origins'), (b'mlp', b'mlp'), (b'drp', b'drp'), (b'hrp', b'hrp'), (b'lgrp', b'lgrp'), (b'turkana', b'turkana'), (b'cc', b'cc'), (b'fc', b'fc'), (b'gdb', b'gdb'), (b'west_turkana', b'west_turkana'), (b'san_francisco', b'san_francisco'), (b'omo_mursi', b'omo_mursi'), (b'projects', b'projects'), (b'taxonomy', b'taxonomy'), (b'leaflet', b'leaflet'), (b'djgeojson', b'djgeojson'), (b'proyecto', b'proyecto')])),
                ('abstract', models.TextField(help_text=b'A  description of the project, its importance, etc.', max_length=4000, null=True, blank=True)),
                ('is_standard', models.BooleanField(default=False)),
                ('attribution', models.TextField(help_text=b'A description of the people / institutions responsible for collecting the data.', max_length=1000, null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('geographic', models.CharField(max_length=255, null=True, blank=True)),
                ('temporal', models.CharField(max_length=255, null=True, blank=True)),
                ('graphic', models.FileField(max_length=255, null=True, upload_to=b'uploads/images/projects', blank=True)),
                ('occurrence_table_name', models.CharField(help_text=b'The name of the main occurrence table in the models.py file of the associated app', max_length=255, null=True, blank=True)),
                ('is_public', models.BooleanField(default=False, help_text=b'Is the raw data to be made publicly viewable?')),
                ('display_summary_info', models.BooleanField(default=True, help_text=b'Should project summary data be published? Only uncheck this in extreme circumstances')),
                ('display_fields', models.TextField(default=b"['id',]", max_length=2000, null=True, help_text=b"A list of fields to display in the public view of the data, first entry should be 'id'", blank=True)),
                ('display_filter_fields', models.TextField(default=b'[]', max_length=2000, null=True, help_text=b'A list of fields to filter on in the public view of the data, can be empty list []', blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('default_app_model', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ['short_name'],
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('native', models.BooleanField(default=False, help_text=b'If true, this term is native to the project or standard, otherwise the term is being reused by the project or standard.')),
                ('mapping', models.CharField(help_text=b'If this term is being reused from another standard or project, the mapping field is used to provide the name of the field in this project or standard as opposed to the name in the project or standard from which it is being reused.', max_length=255, null=True, blank=True)),
                ('project', models.ForeignKey(to='projects.Project')),
                ('term', models.ForeignKey(to='standard.Term')),
            ],
            options={
                'db_table': 'projects_project_term',
                'verbose_name': 'Project Term',
                'verbose_name_plural': 'Project Terms',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='terms',
            field=models.ManyToManyField(to='standard.Term', through='projects.ProjectTerm', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(to='base.PaleocoreUser', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='projectterm',
            unique_together=set([('project', 'term')]),
        ),
    ]
