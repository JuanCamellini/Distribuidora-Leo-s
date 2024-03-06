from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('producto/<int:pk>', views.productSingle, name="product"),
    path('categoria/<str:foo>', views.category, name="categoria"),
    path('acerca/', views.about, name="acerca"),
    path('contacto/', views.contact, name="contacto"),
    path('carrito/', views.cart, name="carrito"),
    path('base/', views.base, name="base"),
]