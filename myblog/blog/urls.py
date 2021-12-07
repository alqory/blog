from django.urls import path
from . import views
from .views import *

app_name ='blog'

urlpatterns = [
    # path('',views.index,name='index'),
    path('tambah',views.tambah,name='tambah'),
    path('update/<id>',views.update,name='update'),
    path('hapus/<id>',views.hapus,name='hapus'),
    # path('detail/<slug_input>',views.detail_post,name='detail'),
    # path('kategori/<Kategori_input>',views.kategories,name='kategori'),

    # factory

    path('',BlogIndex.as_view(), name='home'),
    path('<slug>',BlogDetail.as_view(),name='detail'),
    path('kategori/<category_id>', BlogKategori.as_view(),name='kategori'),
    path('manage/', BlogManage.as_view(), name='manage'),
    path('manage/create', BlogCreate.as_view(), name='create')
]