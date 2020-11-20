# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models
from django.contrib.gis.db import models
# Create your models here.


class Dataset(models.Model):
    
    name = models.CharField(max_length=95)
    date = models.DateField()
    status_active = models.IntegerField( default =  1 )
    def __str__(self):
        return "Datset : "+'%s' % (self.name)

class Row(models.Model):

    dataset_id = models.ForeignKey(Dataset, related_name='data_set_id',on_delete=models.PROTECT)
    point = models.PointField(null=True, blank=True,)
    client_id = models.IntegerField()
    client_name = models.CharField(max_length=45)
    status_active = models.IntegerField( default =  1 )
    def __str__(self):
        return "Row client_name : "+'%s' % (self.client_name)
