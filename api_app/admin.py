# -*- coding: utf-8 -*-
from django.contrib import admin
from api_app.models import *




# Se registran los Modelos del app del API al admin de Django

admin.site.register(Row)
admin.site.register(Dataset)