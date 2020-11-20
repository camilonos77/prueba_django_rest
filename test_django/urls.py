# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    #path('admin/', admin.site.urls),
    path('api/v1/', include('api_app.urls')), # path url app Api rest


]
