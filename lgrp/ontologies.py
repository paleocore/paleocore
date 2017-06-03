import sqlite3
from lgrp.models import *


def find_unmatched_values(field_name):
    lgrp_bio = Biology.objects.all()
    values = list(set([getattr(bio, field_name) for bio in lgrp_bio]))
    field = Biology._meta.get_field_by_name(field_name)[0]
    choices = [i[0] for i in field.choices]
    result = [v for v in values if v not in choices]
    if (not result) or result == [None]:
        return (False, None, None)
    else:
        return (True, len(result), result)


LGRP_BASIS_OF_RECORD_VOCABULARY = (("Collection", "Collection"), ("Observation", "Observation"))

LGRP_COLLECTING_METHOD_VOCABULARY = (
    ("Survey", "Survey"),
    ("Wet Screen", "Wet Screen"),
    ("Crawl Survey", "Crawl Survey"),
    ("Transect Survey", "Transect Survey"),
    ("Dry Screen", "Dry Screen"),
    ("Excavation", "Excavation"),
)

LGRP_COLLECTOR_CHOICES = (
    ("LGRP Team", "LGRP Team"),
    ("K.E. Reed", "K.E. Reed"),
    ("S. Oestmo", "S. Oestmo"),
    ("L. Werdelin", "L. Werdelin"),
    ("C.J. Campisano", "C.J. Campisano"),
    ("D.R. Braun", "D.R. Braun"),
    ("Tomas", "Tomas"),
    ("J. Rowan", "J. Rowan"),
    ("B. Villamoare", "B. Villamoare"),
    ("C. Seyoum", "C. Seyoum"),
    ("E. Scott", "E. Scott"),
    ("E. Locke", "E. Locke"),
    ("J. Harris", "J. Harris"),
    ("I. Lazagabaster", "I. Lazagabaster"),
    ("I. Smail", "I. Smail"),
    ("D. Garello", "D. Garello"),
    ("E.N. DiMaggio", "E.N. DiMaggio"),
    ("W.H. Kimbel", "W.H. Kimbel"),
    ("J. Robinson", "J. Robinson"),
    ("M. Bamford", "M. Bamford"),
    ("Zinash", "Zinash"),
    ("D. Feary", "D. Feary"),
    ("D. I. Garello", "D. I. Garello"),
)

LGRP_FINDER_CHOICES = LGRP_COLLECTOR_CHOICES + (
    ("Afar", "Afar"),
)

LGRP_IDENTIFIER_CHOICES = (
    ('I. Lazagabaster', 'I. Lazagabaster'),
    ('K.E. Reed','K.E. Reed'),
    ('C. Seyoum', 'C. Seyoum'),
    ('B. Villamoare','B. Villamoare'),
    ('J. Robinson','J. Robinson'),
    ('I. Smail', 'I. Smail'),
    ('L.A. Werdelin', 'L.A. Werdelin'),
    ('E. Scott', 'E. Scott'),
    ('J. Rowan', 'J. Rowan'),
    ('W.H. Kimbel', 'W.H. Kimbel'),
    ('J.A. Harris', 'J.A. Harris'),
    ('E. Locke', 'E. Locke')
)

OLD_LGRP_IDENTIFIER_CHOICES=(
    (u'D. Braun', u'D. Braun'),
    (u'J. Thompson', u'J. Thompson'),
    (u'E. Scott', u'E. Scott'),
    (u'E. Locke', u'E. Locke'),
    (u'A.E. Shapiro', u'A.E. Shapiro'),
    (u'A.W. Gentry', u'A.W. Gentry'),
    (u'B.J. Schoville', u'B.J. Schoville'),
    (u'B.M. Latimer', u'B.M. Latimer'),
    (u'C. Denys', u'C. Denys'),
    (u'C.A. Lockwood', u'C.A. Lockwood'),
    (u'D. Geraads', u'D. Geraads'),
    (u'D.C. Johanson', u'D.C. Johanson'),
    (u'E. Delson', u'E. Delson'),
    (u'E.S. Vrba', u'E.S. Vrba'),
    (u'F.C. Howell', u'F.C. Howell'),
    (u'G. Petter', u'G. Petter'),
    (u'G. Suwa', u'G. Suwa'),
    (u'G.G. Eck', u'G.G. Eck'),
    (u'H.B. Krentza', u'H.B. Krentza'),
    (u'H.B. Wesselman', u'H.B. Wesselman'),
    (u'H.B.S. Cooke', u'H.B.S. Cooke'), (u'Institute Staff', u'Institute Staff'), (u'J.C. Rage', u'J.C. Rage'),
    (u'K.E. Reed', u'K.E. Reed'), (u'L.A. Werdelin', u'L.A. Werdelin'), (u'L.J. Flynn', u'L.J. Flynn'),
    (u'M. Sabatier', u'M. Sabatier'), (u'M.E. Lewis', u'M.E. Lewis'), (u'N. Fessaha', u'N. Fessaha'),
    (u'P. Brodkorb', u'P. Brodkorb'), (u'R. Bobe-Quinteros', u'R. Bobe-Quinteros'), (u'R. Geze', u'R. Geze'),
    (u'R.L. Bernor', u'R.L. Bernor'), (u'S.R. Frost', u'S.R. Frost'), (u'T.D. White', u'T.D. White'),
    (u'T.K. Nalley', u'T.K. Nalley'), (u'V. Eisenmann', u'V. Eisenmann'), (u'W.H. Kimbel', u'W.H. Kimbel'),
    (u'Z. Alemseged', u'Z. Alemseged'), (u'S. Oestmo', u'S. Oestmo'), (u'J. Rowan', u'J. Rowan'),
    (u'C.J. Campisano', u'C.J. Campisano'), (u'J. Robinson', u'J. Robinson'), (u'I. Smail', u'I. Smail'),
    (u'I. Lazagabaster', u'I. Lazagabaster')
)


LGRP_COLLECTION_CODES = (
    ("AA", "AA"),
    ("AM", "AM"),
    ("AM12", "AM12"),
    ("AS", "AS"),
    ("AT", "AT"),
    ("BD", "BD"),
    ("BG", "BG"),
    ("BR", "BR"),
    ("DK", "DK"),
    ("FD", "FD"),
    ("GR", "GR"),
    ("HD", "HD"),
    ("HS", "HS"),
    ("KG", "KG"),
    ("KL", "KL"),
    ("KT", "KT"),
    ("LD", "LD"),
    ("LG", "LG"),
    ("LN", "LN"),
    ("LS", "LS"),
    ("MF", "MF"),
    ("NL", "NL"),
    ("OI", "OI"),
    ("SS", "SS"),
)

LGRP_ELEMENT_CHOICES = (
    ('astragalus', 'astragalus'),
    ('bacculum', 'bacculum'),
    ('bone (indet.)', 'bone (indet.)'),
    ('calcaneus', 'calcaneus'),
    ('canine', 'canine'),
    ('capitate', 'capitate'),
    ('carapace', 'carapace'),
    ('carpal (indet.)', 'carpal (indet.)'),
    ('carpal/tarsal', 'carpal/tarsal'),
    ('carpometacarpus', 'carpometacarpus'),
    ('carpus', 'carpus'),
    ('chela', 'chela'),
    ('clavicle', 'clavicle'),
    ('coccyx', 'coccyx'),
    ('coprolite', 'coprolite'),
    ('cranium', 'cranium'),
    ('cranium w/horn core', 'cranium w/horn core'),
    ('cuboid', 'cuboid'),
    ('cubonavicular', 'cubonavicular'),
    ('cuneiform', 'cuneiform'),
    ('dermal plate', 'dermal plate'),
    ('egg shell', 'egg shell'),
    ('endocast', 'endocast'),
    ('ethmoid', 'ethmoid'),
    ('femur', 'femur'),
    ('fibula', 'fibula'),
    ('frontal', 'frontal'),
    ('hamate', 'hamate'),
    ('horn core', 'horn core'),
    ('humerus', 'humerus'),
    ('hyoid', 'hyoid'),
    ('Ilium', 'Ilium'),
    ('incisor', 'incisor'),
    ('innominate', 'innominate'),
    ('ischium', 'ischium'),
    ('lacrimal', 'lacrimal'),
    ('long bone ', 'long bone '),
    ('lunate', 'lunate'),
    ('mandible', 'mandible'),
    ('manus', 'manus'),
    ('maxilla', 'maxilla'),
    ('metacarpal', 'metacarpal'),
    ('metapodial', 'metapodial'),
    ('metatarsal', 'metatarsal'),
    ('molar', 'molar'),
    ('nasal', 'nasal'),
    ('navicular', 'navicular'),
    ('naviculocuboid', 'naviculocuboid'),
    ('occipital', 'occipital'),
    ('ossicone', 'ossicone'),
    ('parietal', 'parietal'),
    ('patella', 'patella'),
    ('pes', 'pes'),
    ('phalanx', 'phalanx'),
    ('pisiform', 'pisiform'),
    ('plastron', 'plastron'),
    ('premaxilla', 'premaxilla'),
    ('premolar', 'premolar'),
    ('pubis', 'pubis'),
    ('radioulna', 'radioulna'),
    ('radius', 'radius'),
    ('rib', 'rib'),
    ('sacrum', 'sacrum'),
    ('scaphoid', 'scaphoid'),
    ('scapholunar', 'scapholunar'),
    ('scapula', 'scapula'),
    ('scute', 'scute'),
    ('sesamoid', 'sesamoid'),
    ('shell', 'shell'),
    ('skeleton', 'skeleton'),
    ('skull', 'skull'),
    ('sphenoid', 'sphenoid'),
    ('sternum', 'sternum'),
    ('talon', 'talon'),
    ('talus', 'talus'),
    ('tarsal (indet.)', 'tarsal (indet.)'),
    ('tarsometatarsus', 'tarsometatarsus'),
    ('tarsus', 'tarsus'),
    ('temporal', 'temporal'),
    ('tibia', 'tibia'),
    ('tibiotarsus', 'tibiotarsus'),
    ('tooth (indet.)', 'tooth (indet.)'),
    ('trapezium', 'trapezium'),
    ('trapezoid', 'trapezoid'),
    ('triquetrum', 'triquetrum'),
    ('ulna', 'ulna'),
    ('vertebra', 'vertebra'),
    ('vomer', 'vomer'),
    ('zygomatic', 'zygomatic'),
)

LGRP_ELEMENT_PORTION_CHOICES = (
    ('almost complete', 'almost complete'),
    ('anterior', 'anterior'),
    ('basal', 'basal'),
    ('complete', 'complete'),
    ('diaphysis', 'diaphysis'),
    ('diaphysis+distal', 'diaphysis+distal'),
    ('diaphysis+proximal', 'diaphysis+proximal'),
    ('distal', 'distal'),
    ('dorsal', 'dorsal'),
    ('epiphysis', 'epiphysis'),
    ('fragment', 'fragment'),
    ('fragments', 'fragments'),
    ('indeterminate', 'indeterminate'),
    ('lateral', 'lateral'),
    ('medial', 'medial'),
    ('midsection', 'midsection'),
    ('midsection+basal', 'midsection+basal'),
    ('midsection+distal', 'midsection+distal'),
    ('posterior', 'posterior'),
    ('proximal', 'proximal'),
    ('symphysis', 'symphysis'),
    ('ventral', 'ventral'),
)

LGRP_ELEMENT_NUMBER_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('3(medial)', '3(medial)'),
    ('4', '4'),
    ('4(lateral)', '4(lateral)'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('2-7', '2-7'),
    ('8-12', '8-12'),
    ('indeterminate', 'indeterminate'),
)

LGRP_ELEMENT_MODIFIER_CHOICES = (
    ('articulated', 'articulated'),
    ('caudal', 'caudal'),
    ('cervical', 'cervical'),
    ('coccygeal', 'coccygeal'),
    ('distal', 'distal'),
    ('intermediate', 'intermediate'),
    ('lower', 'lower'),
    ('lumbar', 'lumbar'),
    ('manual', 'manual'),
    ('manual distal', 'manual distal'),
    ('manual intermediate', 'manual intermediate'),
    ('manual proximal', 'manual proximal'),
    ('pedal', 'pedal'),
    ('pedal distal', 'pedal distal'),
    ('pedal intermediate', 'pedal intermediate'),
    ('pedal proximal', 'pedal proximal'),
    ('proximal', 'proximal'),
    ('sacral', 'sacral'),
    ('thoracic', 'thoracic'),
    ('upper', 'upper'),
    ('indeterminate', 'indeterminate')
)

LGRP_SIDE_CHOICES = (
    (u'L', u'L'),
    (u'R', u'R'),
    (u'Indeterminate', u'Indeterminate'),
    (u'L+R', u'L+R')
)

LGRP_WEATHERING_CHOICES = (
    (0, '0 - unweathered'),
    (1, '1 - parallel cracking'),
    (2, '2 - flaking'),
    (3, '3 - rough'),
    (4, '4 - fibrous'),
    (5, '5 - crumbling')
)

lgrp_db_path = '/Users/reedd/Documents/projects/PaleoCore/projects/LGRP/LGRP_Paleobase4_2016.sqlite'
def import_vocabulary(column_name, path=lgrp_db_path):
    connection = sqlite3.connect(lgrp_db_path)
    cursor = connection.cursor()
    colrs = cursor.execute("SELECT {} FROM LookUpTable WHERE {} IS NOT NULL".format(column_name, column_name))
    column_names = [c[0] for c in cursor.description]
    col_list = []
    for row in colrs:
        l = list(row)
        l.append(row[0])
        col_list.append(tuple(l))
    return tuple(col_list)
