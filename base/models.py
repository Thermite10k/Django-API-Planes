

from ast import operator
from django.db import models

# Create your models here.


class Parts(models.Model):
    serialNumber = models.IntegerField()
    countInStock = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Planes(models.Model):
    model = models.CharField(max_length=255)
    category = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.model


class Operators(models.Model):
    name = models.CharField(max_length=255)
    planes = models.ManyToManyField(
        Planes)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class faultyPart(models.Model):
    operator = models.ForeignKey(
        Operators.planes, on_delete=models.SET_NULL, null=True)
    part = models.ForeignKey(Parts, on_delete=models.SET_NULL, null=True)
    plane = models.ForeignKey(
        operator.planes, on_delete=models.SET_NULL, null=True)
    _id = models.AutoField(primary_key=True, editable=False)
    status = models.BooleanField(default=False)
    comment = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.part.serialNumber
