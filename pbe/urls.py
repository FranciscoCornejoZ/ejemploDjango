from django.contrib import admin
from django.urls import path
from pbe.views import bienvenida, calcula_edad, situacion, maneja 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('edad/<int:edad>', calcula_edad),
    path('situacion/<int:edad2>/<int:edad3>', situacion),
    path('maneja/<int:maneja1>', maneja)
]

