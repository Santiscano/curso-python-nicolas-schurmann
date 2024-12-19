from django.urls import path
from . import views  # desde la carpeta donde me encuentro importa views

# esto es convencion crear la variable
urlpatterns = [
    path('', views.index, name='index')
]