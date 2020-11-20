# -*- coding: utf-8 -*-
from __future__ import absolute_import

# Libs django - project
from django.db import models
from django.contrib.gis.db import models



# Libs app


# Libs external vendor


class Dataset(models.Model):
    
    """
        Dataset class
        Objeto que representa el DataSet cada vez que se carga un archivo
        Args:
           
    """

    name = models.CharField(max_length=95) # nombre del dataset
    date = models.DateField() # fecha de creacion del dataset
    status_active = models.IntegerField( default =  1 ) # atributo para mantener activo o no el objeto
    
    
    def __str__(self):
        """
            __str__ method
            Se realiza casting string para el objeto
            Args:
           
        """
        return "Datset : "+'%s' % (self.name)

class Row(models.Model):

    dataset_id = models.ForeignKey(Dataset, related_name='data_set_id',on_delete=models.PROTECT)
    point = models.PointField(null=True, blank=True,) # Objeto point georeferencia
    client_id = models.IntegerField() # identificador del cliente
    client_name = models.CharField(max_length=45) # nombre del cliente
    status_active = models.IntegerField( default =  1 ) # atributo para mantener activo o no el objeto
    
    
    def __str__(self):
        """
            __str__ method
            Se realiza casting string para el objeto
            Args:
           
        """
        return "Row client_name : "+'%s' % (self.client_name)
