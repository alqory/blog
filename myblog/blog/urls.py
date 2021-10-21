from django.urls import path
from . import views

app_name ='blog'

urlpatterns = [
    path('',views.index,name='index'),
    path('tambah',views.tambah,name='tambah'),
    path('update/<id>',views.update,name='update'),
    path('hapus/<id>',views.hapus,name='hapus'),
    path('detail/<id_detail>',views.detail_post,name='detail'),
    path('kategori/<Kategori_input>',views.kategori,name='kategori'),
]