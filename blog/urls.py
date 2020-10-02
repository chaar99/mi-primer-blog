from django.urls import path
from . import views

#<int:pk>- esta parte es más complicada. Significa que Django 
# espera un valor entero y lo transferirá a una vista como una variable llamada pk.
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]