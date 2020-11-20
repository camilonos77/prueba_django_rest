# -*- coding: utf-8 -*-
from __future__ import absolute_import


# Libs django - project
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response


# Libs app
from api_app.models import *
from api_app.serializers import DataSetSerializer,RowSerializer

# Libs external vendor
from datetime import datetime, time, date, timedelta
from io import StringIO
import csv
from django.contrib.gis.geos import Point





class ListDataSet(generics.ListCreateAPIView):

    """
        ListDataSet class
        ClassView para gestionar el endPoint de Dataset
        Args:
           
    """

    queryset = Dataset.objects.filter(status_active = 1 )
    serializer_class = DataSetSerializer


    def post(self,request):

        """
            post  method
            Se configura funcionamiento metodo http post
            Args:
                request(dict): contiene la informacion request http
           
        """

        try:
            file_request_list = request.FILES
            # se valida si el request tiene el archivo
            if "file" in file_request_list:
                name_field = request.data["name"]
                data = {
                        "name":  name_field,
                        "date": date.today()
                }
                serializer = self.get_serializer(data = data)
                serializer.is_valid(raise_exception=True)
                
                file_request = file_request_list["file"]
                filename = file_request.name
                # se valida la extension del archivo

                if filename.endswith('.csv'): 
                    dataset_instance = serializer.save()# create dataset instance
                    file_csv = file_request.read().decode('utf-8')
                    # se lee archivo csv
                    csv_data = csv.reader(StringIO(file_csv), delimiter=',')
                    counter_rows = 0
                    for row in csv_data:
                        if counter_rows > 0:
                            print(row)
                           
                            # se crea objeto point
                            point = Point(float(row[0]) , float(row[1]))
                            # se crea el nuevo objeto row
                            item_row = Row()
                            item_row.dataset_id = dataset_instance
                            item_row.client_id = int(row[2])
                            item_row.client_name = row[3]
                            item_row.point = point
                            item_row.save() # se almacena el nuevo objeto Row
                            
                            
                        counter_rows =  counter_rows + 1

                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    # se valida extension del archivo para que sea csv
                    raise Exception('ERROR el archivo no contiene una extensión válida')
            else:
                 # se valida que el request tenga el archivo
                 raise Exception('ERROR el request no contine un archivo con el valor file')
        except Exception as e:
            # se retorna la Exception si se genera un error no controlado
            return Response(str(e))  




class ListRow(generics.ListCreateAPIView):

    """
        ListRow class
        ClassView para gestionar el endPoint de Row
        Args:
           
    """
    serializer_class = RowSerializer

    def get_queryset(self):

        """
            get_queryset  method
            Se configura funcionamiento par consultar con parametros queryset
            Args:
                
           
        """
        
        queryset = queryset = Row.objects.filter(status_active = 1 )

        # se obtienen queryset del request
        dataset_id = self.request.query_params.get('dataset_id', None)
        name_dataset = self.request.query_params.get('name', None)
        point = self.request.query_params.get('point', None)
        
        # se generan las diferentes combinaciones para que los queryset no sea 
        # obligatorios sino que estos sean  opcionales

        if (dataset_id is not None) and (name_dataset is not None) and (point is not None):
            print("entro a point ")
            queryset = queryset.filter(   point = point , dataset_id = dataset_id, dataset_id__name =  ""+(name_dataset))
            return queryset

        elif (dataset_id is not None) and (name_dataset is not None):
            queryset = queryset.filter(dataset_id = dataset_id, dataset_id__name =  ""+(name_dataset))
            return queryset
        
        elif (dataset_id is not None) and (point is not None):
            queryset = queryset.filter(dataset_id = dataset_id,  point = point  )
            return queryset

        elif (name_dataset is not None) and (point is not None):
            queryset = queryset.filter(dataset_id__name =  ""+(name_dataset) , point = point )
            return queryset


        if name_dataset is not None:
            queryset = queryset.filter(dataset_id__name =  ""+(name_dataset) )
            return queryset

        elif dataset_id is not None:
            queryset = queryset.filter(dataset_id = dataset_id)
            return queryset

        elif point is not None:
            queryset = queryset.filter(point = point)
            return queryset
        else:
            return queryset