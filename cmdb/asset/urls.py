from . import views
from django.urls import path
app_name = "asset"

urlpatterns = [
    path('',views.index, name='index')
]