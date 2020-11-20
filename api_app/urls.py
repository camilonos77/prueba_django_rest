# -*- coding: utf-8 -*-
from __future__ import absolute_import


# Libs django - project
from django.contrib import admin
from django.urls import path,include


# Libs app
from api_app.views import ListDataSet,ListRow


# Libs external vendor


# patrones url del app
urlpatterns = [
   
   
    path('datasets', ListDataSet.as_view()), # url path dataset endpoint


    path('rows', ListRow.as_view()),# url path row endpoint
   

]