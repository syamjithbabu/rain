from django.urls import path
from . import views

app_name='power'

urlpatterns = [
   path('',views.Re,name='Hi')
]
