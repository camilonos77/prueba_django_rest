from django.contrib import admin
from django.urls import path,include

from api_app.views import ListDataSet,ListRow

urlpatterns = [
   
   
    path('datasets', ListDataSet.as_view()),


    path('rows', ListRow.as_view()),
   
]