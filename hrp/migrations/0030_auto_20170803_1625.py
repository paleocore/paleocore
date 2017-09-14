# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hrp', '0029_auto_20170803_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(max_length=256, null=True, verbose_name=b'Last Name', blank=True)),
                ('first_name', models.CharField(max_length=256, null=True, verbose_name=b'First Name', blank=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'verbose_name': 'HRP Person',
                'verbose_name_plural': 'HRP People',
            },
        ),
        migrations.AlterField(
            model_name='biology',
            name='element',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Element', choices=[(b'astragalus', b'astragalus'), (b'bacculum', b'bacculum'), (b'bone (indet.)', b'bone (indet.)'), (b'calcaneus', b'calcaneus'), (b'canine', b'canine'), (b'capitate', b'capitate'), (b'carapace', b'carapace'), (b'carpal (indet.)', b'carpal (indet.)'), (b'carpal/tarsal', b'carpal/tarsal'), (b'carpometacarpus', b'carpometacarpus'), (b'carpus', b'carpus'), (b'chela', b'chela'), (b'clavicle', b'clavicle'), (b'coccyx', b'coccyx'), (b'coprolite', b'coprolite'), (b'cranium', b'cranium'), (b'cranium w/horn core', b'cranium w/horn core'), (b'cuboid', b'cuboid'), (b'cubonavicular', b'cubonavicular'), (b'cuneiform', b'cuneiform'), (b'dermal plate', b'dermal plate'), (b'egg shell', b'egg shell'), (b'endocast', b'endocast'), (b'ethmoid', b'ethmoid'), (b'femur', b'femur'), (b'fibula', b'fibula'), (b'frontal', b'frontal'), (b'hamate', b'hamate'), (b'horn core', b'horn core'), (b'humerus', b'humerus'), (b'hyoid', b'hyoid'), (b'Ilium', b'Ilium'), (b'incisor', b'incisor'), (b'innominate', b'innominate'), (b'ischium', b'ischium'), (b'lacrimal', b'lacrimal'), (b'long bone ', b'long bone '), (b'lunate', b'lunate'), (b'mandible', b'mandible'), (b'manus', b'manus'), (b'maxilla', b'maxilla'), (b'metacarpal', b'metacarpal'), (b'metapodial', b'metapodial'), (b'metatarsal', b'metatarsal'), (b'molar', b'molar'), (b'nasal', b'nasal'), (b'navicular', b'navicular'), (b'naviculocuboid', b'naviculocuboid'), (b'occipital', b'occipital'), (b'ossicone', b'ossicone'), (b'parietal', b'parietal'), (b'patella', b'patella'), (b'pes', b'pes'), (b'phalanx', b'phalanx'), (b'pisiform', b'pisiform'), (b'plastron', b'plastron'), (b'premaxilla', b'premaxilla'), (b'premolar', b'premolar'), (b'pubis', b'pubis'), (b'radioulna', b'radioulna'), (b'radius', b'radius'), (b'rib', b'rib'), (b'sacrum', b'sacrum'), (b'scaphoid', b'scaphoid'), (b'scapholunar', b'scapholunar'), (b'scapula', b'scapula'), (b'scute', b'scute'), (b'sesamoid', b'sesamoid'), (b'shell', b'shell'), (b'skeleton', b'skeleton'), (b'skull', b'skull'), (b'sphenoid', b'sphenoid'), (b'sternum', b'sternum'), (b'talon', b'talon'), (b'talus', b'talus'), (b'tarsal (indet.)', b'tarsal (indet.)'), (b'tarsometatarsus', b'tarsometatarsus'), (b'tarsus', b'tarsus'), (b'temporal', b'temporal'), (b'tibia', b'tibia'), (b'tibiotarsus', b'tibiotarsus'), (b'tooth (indet.)', b'tooth (indet.)'), (b'trapezium', b'trapezium'), (b'trapezoid', b'trapezoid'), (b'triquetrum', b'triquetrum'), (b'ulna', b'ulna'), (b'vertebra', b'vertebra'), (b'vomer', b'vomer'), (b'zygomatic', b'zygomatic'), (b'pharyngeal teeth', b'pharyngeal teeth'), (b'molars', b'molars'), (b'tusk', b'tusk'), (b'horn corn', b'horn corn'), (b'spine', b'spine'), (b'silicified wood', b'silicified wood'), (b'dentary', b'dentary'), (b'cleithrum', b'cleithrum'), (b'skull plate', b'skull plate'), (b'basicranium', b'basicranium'), (b'angulararticular', b'angulararticular'), (b'ribs', b'ribs'), (b'lateral ethmoid', b'lateral ethmoid'), (b'pterotic', b'pterotic'), (b'tooth roots', b'tooth roots'), (b'shells', b'shells'), (b'pharyngeal tooth', b'pharyngeal tooth'), (b'ilium', b'ilium'), (b'hemimandible', b'hemimandible'), (b'pectoral spine', b'pectoral spine'), (b'palate', b'palate'), (b'pelvis', b'pelvis'), (b'long bone', b'long bone'), (b'axis', b'axis'), (b'acetabulum', b'acetabulum'), (b'magnum', b'magnum'), (b'hemi-mandible', b'hemi-mandible'), (b'weberian', b'weberian'), (b'supraoccipital', b'supraoccipital'), (b'anguloarticular', b'anguloarticular')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element_modifier',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Element Mod', choices=[(b'articulated', b'articulated'), (b'caudal', b'caudal'), (b'cervical', b'cervical'), (b'coccygeal', b'coccygeal'), (b'distal', b'distal'), (b'intermediate', b'intermediate'), (b'lower', b'lower'), (b'lumbar', b'lumbar'), (b'manual', b'manual'), (b'manual distal', b'manual distal'), (b'manual intermediate', b'manual intermediate'), (b'manual proximal', b'manual proximal'), (b'medial', b'medial'), (b'pedal', b'pedal'), (b'pedal distal', b'pedal distal'), (b'pedal intermediate', b'pedal intermediate'), (b'pedal proximal', b'pedal proximal'), (b'proximal', b'proximal'), (b'sacral', b'sacral'), (b'thoracic', b'thoracic'), (b'upper', b'upper'), (b'indeterminate', b'indeterminate')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='element_portion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Element Portion', choices=[(b'almost complete', b'almost complete'), (b'anterior', b'anterior'), (b'basal', b'basal'), (b'caudal', b'caudal'), (b'complete', b'complete'), (b'cranial', b'cranial'), (b'diaphysis', b'diaphysis'), (b'diaphysis+distal', b'diaphysis+distal'), (b'diaphysis+proximal', b'diaphysis+proximal'), (b'distal', b'distal'), (b'dorsal', b'dorsal'), (b'epiphysis', b'epiphysis'), (b'fragment', b'fragment'), (b'fragments', b'fragments'), (b'indeterminate', b'indeterminate'), (b'lateral', b'lateral'), (b'medial', b'medial'), (b'midsection', b'midsection'), (b'midsection+basal', b'midsection+basal'), (b'midsection+distal', b'midsection+distal'), (b'posterior', b'posterior'), (b'proximal', b'proximal'), (b'symphysis', b'symphysis'), (b'ventral', b'ventral')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='life_stage',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Life Stage', choices=[(b'infant', b'infant'), (b'juvenile', b'juvenile')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='sex',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Sex', blank=True),
        ),
        migrations.AlterField(
            model_name='biology',
            name='side',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Side', choices=[('L', 'L'), ('R', 'R'), ('Indeterminate', 'Indeterminate'), ('L+R', 'L+R')]),
        ),
        migrations.AlterField(
            model_name='biology',
            name='size_class',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Size Class', choices=[(b'indeterminate', b'indeterminate'), (b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collecting_method',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Collecting Method', choices=[(b'Survey', b'Survey'), (b'dryscreen5mm', b'dryscreen5mm'), (b'wetscreen1mm', b'wetscreen1mm')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='collector',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Collector', choices=[(b'C.J. Campisano', b'C.J. Campisano'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'T.K. Nalley', b'T.K. Nalley'), (b'D.N. Reed', b'D.N. Reed'), (b'K.E. Reed', b'K.E. Reed'), (b'B.J. Schoville', b'B.J. Schoville'), (b'A.E. Shapiro', b'A.E. Shapiro'), (b'HFS Student', b'HFS Student'), (b'HRP Team', b'HRP Team'), (b'Afar Team', b'Afar Team')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='date_recorded',
            field=models.DateTimeField(null=True, verbose_name=b'Date Recorded', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='disposition',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Disposition', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='drainage_region',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Drainage Region', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='field_number',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Field Number', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='finder',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name=b'Finder', choices=[(b'C.J. Campisano', b'C.J. Campisano'), (b'W.H. Kimbel', b'W.H. Kimbel'), (b'T.K. Nalley', b'T.K. Nalley'), (b'D.N. Reed', b'D.N. Reed'), (b'K.E. Reed', b'K.E. Reed'), (b'B.J. Schoville', b'B.J. Schoville'), (b'A.E. Shapiro', b'A.E. Shapiro'), (b'HFS Student', b'HFS Student'), (b'HRP Team', b'HRP Team'), (b'Afar Team', b'Afar Team')]),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='geology_remarks',
            field=models.TextField(max_length=500, null=True, verbose_name=b'Geol Remarks', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, verbose_name=b'Location', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='georeference_remarks',
            field=models.TextField(max_length=50, null=True, verbose_name=b'Georef Remarks', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='item_count',
            field=models.IntegerField(default=1, null=True, verbose_name=b'Item Count', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='preparation_status',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Prep Status', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='problem',
            field=models.BooleanField(default=False, verbose_name=b'Problem'),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='problem_comment',
            field=models.TextField(max_length=255, null=True, verbose_name=b'Problem Comment', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='surface_modification',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Surface Mod', blank=True),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='year_collected',
            field=models.IntegerField(null=True, verbose_name=b'Year Collected', blank=True),
        ),
    ]