# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(null=True, upload_to=b'uploads/files', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hydrology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('length', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('size', models.IntegerField(null=True, blank=True)),
                ('map_sheet', models.CharField(max_length=50, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
            options={
                'verbose_name': 'LGRP Hydrology',
                'verbose_name_plural': 'LGRP Hydrology',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'uploads/images', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Occurrence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('basis_of_record', models.CharField(blank=True, max_length=50, verbose_name=b'Basis of Record', choices=[(b'Collection', b'Collection'), (b'Observation', b'Observation')])),
                ('item_type', models.CharField(blank=True, max_length=255, verbose_name=b'Item Type', choices=[(b'Artifactual', b'Artifactual'), (b'Faunal', b'Faunal'), (b'Floral', b'Floral'), (b'Geological', b'Geological')])),
                ('collection_code', models.CharField(max_length=20, null=True, verbose_name=b'Collection Code', blank=True)),
                ('locality_number', models.IntegerField(null=True, verbose_name=b'Locality', blank=True)),
                ('item_number', models.CharField(max_length=10, null=True, verbose_name=b'Item #', blank=True)),
                ('item_part', models.CharField(max_length=10, null=True, verbose_name=b'Item Part', blank=True)),
                ('remarks', models.TextField(max_length=2500, null=True, verbose_name=b'Remarks', blank=True)),
                ('item_scientific_name', models.CharField(max_length=255, null=True, verbose_name=b'Sci Name', blank=True)),
                ('item_description', models.CharField(max_length=255, null=True, verbose_name=b'Description', blank=True)),
                ('georeference_remarks', models.TextField(max_length=50, null=True, blank=True)),
                ('collecting_method', models.CharField(max_length=50, null=True, choices=[(b'Survey', b'Survey'), (b'Wet Screen', b'Wet Screen'), (b'Crawl survey', b'Crawl survey'), (b'Transect survey', b'Transect survey'), (b'Dry Screen', b'Dry Screen'), (b'Excavation', b'Excavation')])),
                ('related_catalog_items', models.CharField(max_length=50, null=True, verbose_name=b'Related Catalog Items', blank=True)),
                ('field_number', models.CharField(max_length=50, null=True, blank=True)),
                ('collector', models.CharField(blank=True, max_length=50, null=True, choices=[(b'LGRP Team', b'LGRP Team'), (b'K.E. Reed', b'K.E. Reed'), (b'S. Oestmo', b'S. Oestmo'), (b'L. Werdelin', b'L. Werdelin'), (b'C.J. Campisano', b'C.J. Campisano'), (b'D.R. Braun', b'D.R. Braun'), (b'Tomas', b'Tomas'), (b'J. Rowan', b'J. Rowan'), (b'B. Villamoare', b'B. Villamoare'), (b'C. Seyoum', b'C. Seyoum'), (b'E. Scott', b'E. Scott'), (b'E. Locke', b'E. Locke'), (b'J. Harris', b'J. Harris'), (b'I. Lazagabaster', b'I. Lazagabaster'), (b'I. Smail', b'I. Smail'), (b'D. Garello', b'D. Garello'), (b'E.N. DiMaggio', b'E.N. DiMaggio'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'J. Robinson', b'J. Robinson'), (b'M. Bamford', b'M. Bamford'), (b'Zinash', b'Zinash'), (b'D. Feary', b'D. Feary'), (b'D. I. Garello', b'D. I. Garello')])),
                ('finder', models.CharField(max_length=50, null=True, blank=True)),
                ('disposition', models.CharField(max_length=255, null=True, blank=True)),
                ('collection_remarks', models.TextField(max_length=255, null=True, verbose_name=b'Remarks', blank=True)),
                ('date_recorded', models.DateTimeField(null=True, blank=True)),
                ('year_collected', models.IntegerField(null=True, blank=True)),
                ('individual_count', models.IntegerField(default=1, null=True, blank=True)),
                ('preparation_status', models.CharField(max_length=50, null=True, blank=True)),
                ('stratigraphic_marker_upper', models.CharField(max_length=255, null=True, blank=True)),
                ('distance_from_upper', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('stratigraphic_marker_lower', models.CharField(max_length=255, null=True, blank=True)),
                ('distance_from_lower', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('stratigraphic_marker_found', models.CharField(max_length=255, null=True, blank=True)),
                ('distance_from_found', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('stratigraphic_marker_likely', models.CharField(max_length=255, null=True, blank=True)),
                ('distance_from_likely', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('stratigraphic_formation', models.CharField(max_length=255, null=True, blank=True)),
                ('stratigraphic_member', models.CharField(max_length=255, null=True, blank=True)),
                ('analytical_unit', models.CharField(max_length=255, null=True, blank=True)),
                ('analytical_unit_2', models.CharField(max_length=255, null=True, blank=True)),
                ('analytical_unit_3', models.CharField(max_length=255, null=True, blank=True)),
                ('analytical_unit_found', models.CharField(max_length=255, null=True, blank=True)),
                ('analytical_unit_likely', models.CharField(max_length=255, null=True, blank=True)),
                ('analytical_unit_simplified', models.CharField(max_length=255, null=True, blank=True)),
                ('in_situ', models.BooleanField(default=False)),
                ('ranked', models.BooleanField(default=False)),
                ('image', models.FileField(max_length=255, null=True, upload_to=b'uploads/images/lgrp', blank=True)),
                ('weathering', models.SmallIntegerField(null=True, blank=True)),
                ('surface_modification', models.CharField(max_length=255, null=True, blank=True)),
                ('problem', models.BooleanField(default=False)),
                ('problem_comment', models.TextField(max_length=255, null=True, blank=True)),
                ('barcode', models.IntegerField(null=True, verbose_name=b'Barcode', blank=True)),
                ('date_last_modified', models.DateTimeField(auto_now=True, verbose_name=b'Date Last Modified')),
                ('drainage_region', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'ordering': ['collection_code', 'item_number', 'item_part'],
                'verbose_name': 'LGRP Occurrence',
                'verbose_name_plural': 'LGRP Occurrences',
            },
        ),
        migrations.CreateModel(
            name='Archaeology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lgrp.Occurrence')),
                ('find_type', models.CharField(max_length=255, null=True, blank=True)),
                ('length_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('width_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
            ],
            options={
                'verbose_name': 'LGRP Archaeology',
                'verbose_name_plural': 'LGRP Archaeology',
            },
            bases=('lgrp.occurrence',),
        ),
        migrations.CreateModel(
            name='Biology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lgrp.Occurrence')),
                ('verbatim_taxon', models.CharField(max_length=1024, null=True, blank=True)),
                ('verbatim_identification_qualifier', models.CharField(max_length=255, null=True, blank=True)),
                ('identified_by', models.CharField(max_length=100, null=True, blank=True)),
                ('year_identified', models.IntegerField(null=True, blank=True)),
                ('type_status', models.CharField(max_length=50, null=True, blank=True)),
                ('sex', models.CharField(max_length=50, null=True, blank=True)),
                ('life_stage', models.CharField(max_length=50, null=True, blank=True)),
                ('preparations', models.CharField(max_length=50, null=True, blank=True)),
                ('morphobank_number', models.IntegerField(null=True, blank=True)),
                ('side', models.CharField(max_length=50, null=True, blank=True)),
                ('attributes', models.CharField(max_length=50, null=True, blank=True)),
                ('fauna_notes', models.TextField(max_length=64000, null=True, blank=True)),
                ('tooth_upper_or_lower', models.CharField(max_length=50, null=True, blank=True)),
                ('tooth_number', models.CharField(max_length=50, null=True, blank=True)),
                ('tooth_type', models.CharField(max_length=50, null=True, blank=True)),
                ('um_tooth_row_length_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('um_1_length_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('um_1_width_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('um_2_length_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('um_2_width_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('um_3_length_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('um_3_width_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('lm_tooth_row_length_mm', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('lm_1_length', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('lm_1_width', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('lm_2_length', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('lm_2_width', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('lm_3_length', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('lm_3_width', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('element', models.CharField(max_length=50, null=True, blank=True)),
                ('element_modifier', models.CharField(max_length=50, null=True, blank=True)),
                ('uli1', models.BooleanField(default=False)),
                ('uli2', models.BooleanField(default=False)),
                ('uli3', models.BooleanField(default=False)),
                ('uli4', models.BooleanField(default=False)),
                ('uli5', models.BooleanField(default=False)),
                ('uri1', models.BooleanField(default=False)),
                ('uri2', models.BooleanField(default=False)),
                ('uri3', models.BooleanField(default=False)),
                ('uri4', models.BooleanField(default=False)),
                ('uri5', models.BooleanField(default=False)),
                ('ulc', models.BooleanField(default=False)),
                ('urc', models.BooleanField(default=False)),
                ('ulp1', models.BooleanField(default=False)),
                ('ulp2', models.BooleanField(default=False)),
                ('ulp3', models.BooleanField(default=False)),
                ('ulp4', models.BooleanField(default=False)),
                ('urp1', models.BooleanField(default=False)),
                ('urp2', models.BooleanField(default=False)),
                ('urp3', models.BooleanField(default=False)),
                ('urp4', models.BooleanField(default=False)),
                ('ulm1', models.BooleanField(default=False)),
                ('ulm2', models.BooleanField(default=False)),
                ('ulm3', models.BooleanField(default=False)),
                ('urm1', models.BooleanField(default=False)),
                ('urm2', models.BooleanField(default=False)),
                ('urm3', models.BooleanField(default=False)),
                ('lli1', models.BooleanField(default=False)),
                ('lli2', models.BooleanField(default=False)),
                ('lli3', models.BooleanField(default=False)),
                ('lli4', models.BooleanField(default=False)),
                ('lli5', models.BooleanField(default=False)),
                ('lri1', models.BooleanField(default=False)),
                ('lri2', models.BooleanField(default=False)),
                ('lri3', models.BooleanField(default=False)),
                ('lri4', models.BooleanField(default=False)),
                ('lri5', models.BooleanField(default=False)),
                ('llc', models.BooleanField(default=False)),
                ('lrc', models.BooleanField(default=False)),
                ('llp1', models.BooleanField(default=False)),
                ('llp2', models.BooleanField(default=False)),
                ('llp3', models.BooleanField(default=False)),
                ('llp4', models.BooleanField(default=False)),
                ('lrp1', models.BooleanField(default=False)),
                ('lrp2', models.BooleanField(default=False)),
                ('lrp3', models.BooleanField(default=False)),
                ('lrp4', models.BooleanField(default=False)),
                ('llm1', models.BooleanField(default=False)),
                ('llm2', models.BooleanField(default=False)),
                ('llm3', models.BooleanField(default=False)),
                ('lrm1', models.BooleanField(default=False)),
                ('lrm2', models.BooleanField(default=False)),
                ('lrm3', models.BooleanField(default=False)),
                ('indet_incisor', models.BooleanField(default=False)),
                ('indet_canine', models.BooleanField(default=False)),
                ('indet_premolar', models.BooleanField(default=False)),
                ('indet_molar', models.BooleanField(default=False)),
                ('indet_tooth', models.BooleanField(default=False)),
                ('deciduous', models.BooleanField(default=False)),
                ('identification_qualifier', models.ForeignKey(related_name='lgrp_id_qualifier_bio_occurrences', blank=True, to='taxonomy.IdentificationQualifier', null=True)),
                ('qualifier_taxon', models.ForeignKey(related_name='lgrp_qualifier_taxon_bio_occurrences', blank=True, to='taxonomy.Taxon', null=True)),
                ('taxon', models.ForeignKey(related_name='lgrp_taxon_bio_occurrences', blank=True, to='taxonomy.Taxon', null=True)),
            ],
            options={
                'verbose_name': 'LGRP Biology',
                'verbose_name_plural': 'LGRP Biology',
            },
            bases=('lgrp.occurrence',),
        ),
        migrations.CreateModel(
            name='Geology',
            fields=[
                ('occurrence_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='lgrp.Occurrence')),
                ('find_type', models.CharField(max_length=255, null=True, blank=True)),
                ('dip', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('strike', models.DecimalField(null=True, max_digits=38, decimal_places=8, blank=True)),
                ('color', models.CharField(max_length=255, null=True, blank=True)),
                ('texture', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'LGRP Geology',
                'verbose_name_plural': 'LGRP Geology',
            },
            bases=('lgrp.occurrence',),
        ),
        migrations.AddField(
            model_name='image',
            name='occurrence',
            field=models.ForeignKey(related_name='lgrp_occurrences', to='lgrp.Occurrence'),
        ),
        migrations.AddField(
            model_name='file',
            name='occurrence',
            field=models.ForeignKey(to='lgrp.Occurrence'),
        ),
    ]
