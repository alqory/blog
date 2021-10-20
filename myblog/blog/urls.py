from django.urls import path
from . import views

app_name ='blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index2,name='test'),
]