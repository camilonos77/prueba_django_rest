# -*- coding: utf-8 -*-
from __future__ import absolute_import



# Libs django - project
from rest_framework import serializers

# Libs app
from api_app import models

# Libs external vendor




class DataSetSerializer(serializers.ModelSerializer):

    """
        DataSetSerializer class
        Crea la clase Selializar para exponer el Objeto Dataset con el Api rest
        Args:
           
    """
    # se exponen los atributos del objeto en el endpoint
    class Meta:
        fields = (
            'id',
            'name',
            'date',
        )
        model = models.Dataset



class RowSerializer(serializers.ModelSerializer):

    """
        DataSetSerializer class
        Crea la clase Selializar para exponer el Objeto Row con el Api rest
        Args:
           
    """
    # se exponen los atributos del objeto en el endpoint
    class Meta:
        fields = (
            'client_name',
            'dataset_id',
            'point',
            'client_id'
        )
        model = models.Row