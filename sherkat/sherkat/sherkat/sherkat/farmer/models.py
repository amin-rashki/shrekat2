from django.db import models


class Kshavarz(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    family = models.CharField(max_length=50, null=True, blank=True)
    father = models.CharField(max_length=50, null=True, blank=True)
    kodMele = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    kodEshtrak = models.IntegerField(null=True, blank=True)
    ctiy = models.CharField(max_length=50, null=True, blank=True)
    licenseNumber = models.IntegerField(null=True, blank=True)
    dateRegistration = models.DateTimeField(null=True)
    activiityStatus = models.CharField(max_length=100, null=True, blank=True)
    rosta = models.CharField(max_length=100, null=True, blank=True)
    river = models.CharField(max_length=100, null=True, blank=True)
    chahak = models.CharField(max_length=100, null=True, blank=True)
