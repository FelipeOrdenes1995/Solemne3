from django.urls import path
from os import name
from .views import home, productos, planmobile, listado_planes, nuevo_plan, modificar_plan, eliminar_plan, internethogar, registro_usuario, telefoniahogar, nuestraempresa, normativaslegales, formulario, realizarpago

urlpatterns = [
    path('', home, name="home"),
    path('productos/', productos,name="productos"),
    path('planmobile/', planmobile,name="planmobile"),
    path('listado-planes/', listado_planes,name="listado_planes"),
    path('nuevo-plan/', nuevo_plan,name="nuevo_plan"),
    path('modificar-plan/<id>/', modificar_plan,name="modificar_plan"),
    path('eliminar-plan/<id>/', eliminar_plan,name="eliminar_plan"),
    path('registro/', registro_usuario, name='registro_usuario'),
    path('internethogar/', internethogar,name="internethogar"),
    path('telefoniahogar/', telefoniahogar,name="telefoniahogar"),
    path('nuestraempresa/', nuestraempresa,name="nuestraempresa"),
    path('normativaslegales/', normativaslegales,name="normativaslegales"),
    #path('formulario/', formulario,name="formulario"),
    path('realizarpago/', realizarpago,name="realizarpago"),

]

