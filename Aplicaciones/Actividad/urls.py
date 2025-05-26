from django.urls import path
from . import views
urlpatterns= [
    path ('', views.inicio),
    path('nuevoCargo', views.nuevoCargo),
    path('guardarCargo', views.guardarCargo),
    path ('eliminarCargo/<id>', views.eliminarCargo),
    path ('editarCargo/<id>', views.editarCargo),
    path ('procesarEdicionCargo/<id>', views.procesarEdicionCargo)

]



