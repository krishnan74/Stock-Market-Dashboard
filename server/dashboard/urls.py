from django.urls import path
from . import views

urlpatterns = [
    path('getAllStocks/', views.getAllStocks, name='stocks'),
    path('getStockDetails/', views.getStockDetails, name='stock_details'),
    path('addWatchList/', views.addWatchList, name='add_stock'),
    path('getWatchList/', views.getWatchList, name='get_watch_list'),
]