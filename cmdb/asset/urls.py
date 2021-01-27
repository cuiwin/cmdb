from . import views
from django.urls import path
app_name = "asset"

urlpatterns = [
    path('',views.index, name='index'),
    path('list/ajax/', views.list_ajax, name='list_ajax'),
    path('get/ajax/', views.get_ajax, name='get_ajax'),
    path('delete/ajax/', views.delete_ajax, name='delete_ajax'),

]