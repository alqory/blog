from django.urls import path
from . import views
from .views import *

app_name ='blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('tambah',views.tambah,name='tambah'),
    path('update/<id>',views.update,name='update'),
    path('hapus/<id>',views.hapus,name='hapus'),
    path('detail/<slug_input>',views.detail_post,name='detail'),
    path('kategori/<Kategori_input>',views.kategories,name='kategori'),

    # factory

    path('home1',BlogIndex.as_view(), name='home')
]