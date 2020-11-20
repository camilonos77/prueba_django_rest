# -*- coding: utf-8 -*-
# apis/serializers.py
from rest_framework import serializers
from api_app import models


class DataSetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'date',
        )
        model = models.Dataset



class RowSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'client_name',
            'dataset_id',
            'point',
            'client_id'
        )
        model = models.Row