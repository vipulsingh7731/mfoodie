from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('orderplaced/', views.orderplaced),
	path('restaurant/', views.restuarantMenu, name='menu'),
	path('checkout/', views.checkout, name='checkout'),
]
