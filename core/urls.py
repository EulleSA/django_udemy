from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contato, name='contato'),
    path('produto/', views.produto, name='produto'),
]