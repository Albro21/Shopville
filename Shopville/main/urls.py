from django.urls import path
from . import views


urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('product/<str:item_name>/', views.item, name='item'),
    path('add_product/', views.add_product, name='add_product'),
]
