from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('hello/<int:id>', views.hello),
    path('productos/', views.products),
    path('combos/', views.combos),
    path('crear_producto/', views.save_product),
    path('crear_combo/', views.save_combo),
]
