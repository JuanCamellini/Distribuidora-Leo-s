from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_summary, name="cart"),
    path('agregar/', views.cart_add, name="agregar-carrito"),
    path('actualizar/', views.cart_update, name="cart_update"),
    path('delete/', views.cart_delete, name="cart_delete"),

]