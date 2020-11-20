# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response

from api_app.models import *
from api_app.serializers import DataSetSerializer,RowSerializer


from datetime import datetime, time, date, timedelta
from io import StringIO
import csv
from django.contrib.gis.geos import Point


class ListDataSet(generics.ListCreateAPIView):
    queryset = Dataset.objects.filter(status_active = 1 )
    serializer_class = DataSetSerializer


    def post(self,request):
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
                    csv_data = csv.reader(StringIO(file_csv), delimiter=',')

                    #for row in csv_data:
                    #    print(row)

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
                            item_row.save()
                            print("item_row",item_row.id)
                            
                        counter_rows =  counter_rows + 1

                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    raise Exception('ERROR el archivo no contiene una extensión válida')
            else:
                 raise Exception('ERROR el request no contine un archivo con el valor file')
        except Exception as e:
            return Response(str(e))  




class ListRow(generics.ListCreateAPIView):
    #queryset = Row.objects.filter(status_active = 1 )
    serializer_class = RowSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = queryset = Row.objects.filter(status_active = 1 )

        dataset_id = self.request.query_params.get('dataset_id', None)
        name_dataset = self.request.query_params.get('name', None)
        point = self.request.query_params.get('point', None)
        
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