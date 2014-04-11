from django.contrib.gis.db import models


# Model for occurrence table generated by inspect.db
class Occurrence(models.Model):
    objectid = models.IntegerField(primary_key=True)
    barcode = models.IntegerField(blank=True, null=True)
    datelastmodified = models.DateTimeField(blank=True, null=True)
    basisofrecord = models.CharField(max_length=50, blank=True)
    itemtype = models.CharField(max_length=255, blank=True)
    institutionalcode = models.CharField(max_length=20, blank=True)
    collectioncode = models.CharField(max_length=20, blank=True)
    paleolocalitynumber = models.IntegerField(blank=True, null=True)
    paleosublocality = models.CharField(max_length=50, blank=True)
    itemnumber = models.CharField(max_length=50, blank=True)
    itempart = models.CharField(max_length=10, blank=True)
    catalognumber = models.CharField(max_length=255, blank=True)
    remarks = models.CharField(max_length=255, blank=True)
    itemscientificname = models.CharField(max_length=255, blank=True)
    itemdescription = models.CharField(max_length=255, blank=True)
    stateprovince = models.CharField(max_length=50, blank=True)
    locality = models.CharField(max_length=255, blank=True)
    verbatimcoordinates = models.CharField(max_length=50, blank=True)
    verbatimcoordinatesystem = models.CharField(max_length=50, blank=True)
    georeferenceremarks = models.CharField(max_length=50, blank=True)
    utmzone = models.IntegerField(blank=True, null=True)
    utmeast = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    utmnorth = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    geodeticdatum = models.CharField(max_length=20, blank=True)
    collectingmethod = models.CharField(max_length=50, blank=True)
    relatedcatalogitems = models.CharField(max_length=50, blank=True)
    earliestdatecollected = models.DateTimeField(blank=True, null=True)
    dayofyear = models.IntegerField(blank=True, null=True)
    collector = models.CharField(max_length=50, blank=True)
    finder = models.CharField(max_length=50, blank=True)
    disposition = models.CharField(max_length=255, blank=True)
    collectionremarks = models.CharField(max_length=255, blank=True)
    fieldnumber = models.DateTimeField(blank=True, null=True)
    monthcollected = models.CharField(max_length=20, blank=True)
    yearcollected = models.IntegerField(blank=True, null=True)
    individualcount = models.IntegerField(blank=True, null=True)
    preparationstatus = models.CharField(max_length=50, blank=True)
    stratigraphicmarkerupper = models.CharField(max_length=255, blank=True)
    distancefromupper = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphicmarkerlower = models.CharField(max_length=255, blank=True)
    distancefromlower = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphicmarkerfound = models.CharField(max_length=255, blank=True)
    distancefromfound = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphicmarkerlikely = models.CharField(max_length=255, blank=True)
    distancefromlikely = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    stratigraphicmember = models.CharField(max_length=255, blank=True)
    analyticalunit = models.CharField(max_length=255, blank=True)
    analyticalunit2 = models.CharField(max_length=255, blank=True)
    analyticalunit3 = models.CharField(max_length=255, blank=True)
    insitu = models.SmallIntegerField(blank=True, null=True)
    ranked = models.SmallIntegerField(blank=True, null=True)
    imageurl = models.CharField(max_length=255, blank=True)
    relatedinformation = models.CharField(max_length=50, blank=True)
    localityid = models.IntegerField(blank=True, null=True)
    stratigraphicsection = models.CharField(max_length=50, blank=True)
    stratigraphicheightinmeters = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    specimenimage = models.BinaryField(blank=True, null=True)
    weathering = models.SmallIntegerField(blank=True, null=True)
    surfacemodification = models.CharField(max_length=255, blank=True)
    point_x = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    point_y = models.DecimalField(max_digits=38, decimal_places=8, blank=True, null=True)
    problem = models.SmallIntegerField(blank=True, null=True)
    problemcomment = models.CharField(max_length=255, blank=True)
    shape = models.GeometryField(srid=32637, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'mlp_occurrence'