# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.gis.geos import Point



from api_app.models import *


from datetime import datetime, time, date, timedelta
from rest_framework.test import APIClient
from rest_framework import status



class ApiTestCase(TestCase):
    
    #def setUp(self):    
    #    #print(":::::: iniciando pruebas de api rest :::::::")
    

    @classmethod
    def setUpTestData(cls):
        print(" Se inicia la configuracion de datos iniciales para realizar la consulta de datos de los metodos GET ")
        # se crea el objeto dataset
        data = {
                        "name":  "archivo dataset",
                        "date": date.today()
        }
        nuevo_dataset = Dataset()
        nuevo_dataset.name = data["name"]
        nuevo_dataset.date = data["date"]
        nuevo_dataset.save()

        row_1 = [19.3475164,-99.2009924,12,"ram"]
        row_2 = [20.3475164,-99.2009924,14,"rooster"]
        row_3 = [21.3475164,-99.2009924,15,"iguana"]
        list_rows = [row_1,row_2,row_3]
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

            Se verifica el functionamiento del endpoint GET /api/v1/ el cual obtiene los datasets

        """
        client = APIClient()
        response = client.get(
            '/api/v1/',
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