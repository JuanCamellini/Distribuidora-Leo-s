from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.cart_summary, name="cart_summary"),
    path('agregar/', views.cart_add, name="agregar-carrito"),
    path('update/', views.cart_update, name="cart_update"),
    path('delete/', views.cart_delete, name="cart_delete"),

]