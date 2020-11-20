# -*- coding: utf-8 -*-
from __future__ import absolute_import


# Libs django - project
from django.test import TestCase
from django.contrib.gis.geos import Point

# Libs app
from api_app.models import *
# Libs external vendor

from datetime import datetime, time, date, timedelta
from rest_framework.test import APIClient
from rest_framework import status



class ApiTestCase(TestCase):
    """
        ApiTestCase class
        Clase que permite ejecutar las pruebas unitarias del proyecto
        Args:
           
    """
    

    @classmethod
    def setUpTestData(cls):

        """
        setUpTestData method
        Crea en la instancia de la bd de test un dataset
        Args:
           
        """

        print(" Se inicia la configuracion de datos iniciales para realizar la consulta de datos de los metodos GET ")
        # se crea el objeto dataset
        data = {
                        "name":  "archivo dataset",
                        "date": date.today()
        }
        # se instancia el modelo del dataset
        nuevo_dataset = Dataset()
        nuevo_dataset.name = data["name"]
        nuevo_dataset.date = data["date"]
        nuevo_dataset.save()

        row_1 = [19.3475164,-99.2009924,12,"ram"]
        row_2 = [20.3475164,-99.2009924,14,"rooster"]
        row_3 = [21.3475164,-99.2009924,15,"iguana"]
        list_rows = [row_1,row_2,row_3]
        # se almacenan los objetos Row relacionando el dataset
        for row in list_rows:
            point = Point(float(row[0]) , float(row[1]))
            item_row = Row()
            item_row.dataset_id = nuevo_dataset
            item_row.client_id = int(row[2])
            item_row.client_name = row[3]
            item_row.point = point
            item_row.save()


    def test_get_dataset_endoint(self):
        """

            Se verifica el functionamiento del endpoint GET /api/v1/datasets el cual obtiene los datasets

        """
        client = APIClient()
        response = client.get(
            '/api/v1/datasets',
            {

            }

        )
        self.assertEqual(response.status_code , status.HTTP_200_OK)
        

    def test_get_rows_endoint(self):
        """

            Se verifica el functionamiento del endpoint GET /api/v1/rows el cual obtiene los objetos row de cada dataset

        """
        client = APIClient()
        response = client.get(
            '/api/v1/rows',
            {

            }
        )
        for item in response.data["results"]:
            print(item)


        self.assertEqual(response.status_code , status.HTTP_200_OK)