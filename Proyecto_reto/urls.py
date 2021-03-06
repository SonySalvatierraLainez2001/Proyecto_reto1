from django.contrib import admin
from django.urls import path
from reto import views

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('MyV/', views.MyV, name="MyV"),
#CuRso7/A#############################################################################
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('modificarestudiante/<int:pk>', views.modificarestudiante, name="modificarestudiante"),
    path('crearestudiante/', views.crearestudiante, name="crearestudiante"),
    path('eliminarestudiante/<int:pk>', views.eliminarestudiante, name="eliminarestudiante"),
    path('familia/', views.familia, name="familia"),
    path('modificarfamilia/<int:pk>', views.modificarfamilia, name="modificarfamilia"),
    path('crearfamilia/', views.crearfamilia, name="crearfamilia"),
    path('eliminarfamilia/<int:pk>', views.eliminarfamilia, name="eliminarfamilia"),
    path('salud/', views.salud, name="salud"),
    path('modificarsalud/<int:pk>', views.modificarsalud, name="modificarsalud"),
    path('crearsalud/', views.crearsalud, name="crearsalud"),
    path('eliminarsalud/<int:pk>', views.eliminarsalud, name="eliminarsalud"),
    path('retiro/', views.retiro, name="retiro"),
    path('modificarretiro/<int:pk>', views.modificarretiro, name="modificarretiro"),
    path('crearretiro/', views.crearretiro, name="crearretiro"),
    path('eliminarretiro/<int:pk>', views.eliminarretiro, name="eliminarretiro"),
    path('formulario/', views.formulario, name="formulario"),
    path('modificarformulario/<int:pk>', views.modificarformulario, name="modificarformulario"),
    path('crearformulario/', views.crearformulario, name="crearformulario"),
    path('eliminarformulario/<int:pk>', views.eliminarformulario, name="eliminarformulario"),
    path('admin/', admin.site.urls),
    path('general/', views.general, name="general"),
    path('modificargeneral/<int:pk>', views.modificargeneral, name="modificargeneral"),
    path('creargeneral/', views.creargeneral, name="creargeneral"),
    path('eliminargeneral/<int:pk>', views.eliminargeneral, name="eliminargeneral"),
#CURSO 7/B=====================================================================================================================
    path('estudiantes7B/', views.estudiantes7B, name="estudiantes7B"),
    path('modificarestudiante7B/<int:pk>', views.modificarestudiante7B, name="modificarestudiante7B"),
    path('crearestudiante7B/', views.crearestudiante7B, name="crearestudiante7B"),
    path('eliminarestudiante7B/<int:pk>', views.eliminarestudiante7B, name="eliminarestudiante7B"),
    path('familia7B/', views.familia7B, name="familia7B"),
    path('modificarfamilia7B/<int:pk>', views.modificarfamilia7B, name="modificarfamilia7B"),
    path('crearfamilia7B/', views.crearfamilia7B, name="crearfamilia7B"),
    path('eliminarfamilia7B/<int:pk>', views.eliminarfamilia7B, name="eliminarfamilia7B"),
    path('salud7B/', views.salud7B, name="salud7B"),
    path('modificarsalud7B/<int:pk>', views.modificarsalud7B, name="modificarsalud7B"),
    path('crearsalud7B/', views.crearsalud7B, name="crearsalud7B"),
    path('eliminarsalud7B/<int:pk>', views.eliminarsalud7B, name="eliminarsalud7B"),
    path('retiro7B/', views.retiro7B, name="retiro7B"),
    path('modificarretiro7B/<int:pk>', views.modificarretiro7B, name="modificarretiro7B"),
    path('crearretiro7B/', views.crearretiro7B, name="crearretiro7B"),
    path('eliminarretiro7B/<int:pk>', views.eliminarretiro7B, name="eliminarretiro7B"),
    path('formulario7B/', views.formulario7B, name="formulario7B"),
    path('modificarformulario7B/<int:pk>', views.modificarformulario7B, name="modificarformulario7B"),
    path('crearformulario7B/', views.crearformulario7B, name="crearformulario7B"),
    path('eliminarformulario7B/<int:pk>', views.eliminarformulario7B, name="eliminarformulario7B"),
#CURSO6/A========================================================================================================================================
    path('estudiantes6A/', views.estudiantes6A, name="estudiantes6A"),
    path('modificarestudiante6A/<int:pk>', views.modificarestudiante6A, name="modificarestudiante6A"),
    path('crearestudiante6A/', views.crearestudiante6A, name="crearestudiante6A"),
    path('eliminarestudiante6A/<int:pk>', views.eliminarestudiante6A, name="eliminarestudiante6A"),
    path('familia6A/', views.familia6A, name="familia6A"),
    path('modificarfamilia6A/<int:pk>', views.modificarfamilia6A, name="modificarfamilia6A"),
    path('crearfamilia6A/', views.crearfamilia6A, name="crearfamilia6A"),
    path('eliminarfamilia6A/<int:pk>', views.eliminarfamilia6A, name="eliminarfamilia6A"),
    path('salud6A/', views.salud6A, name="salud6A"),
    path('modificarsalud6A/<int:pk>', views.modificarsalud6A, name="modificarsalud6A"),
    path('crearsalud6A/', views.crearsalud6A, name="crearsalud6A"),
    path('eliminarsalud6A/<int:pk>', views.eliminarsalud6A, name="eliminarsalud6A"),
    path('retiro6A/', views.retiro6A, name="retiro6A"),
    path('modificarretiro6A/<int:pk>', views.modificarretiro6A, name="modificarretiro6A"),
    path('crearretiro6A/', views.crearretiro6A, name="crearretiro6A"),
    path('eliminarretiro6A/<int:pk>', views.eliminarretiro6A, name="eliminarretiro6A"),
    path('formulario6A/', views.formulario6A, name="formulario6A"),
    path('modificarformulario6A/<int:pk>', views.modificarformulario6A, name="modificarformulario6A"),
    path('crearformulario6A/', views.crearformulario6A, name="crearformulario6A"),
    path('eliminarformulario6A/<int:pk>', views.eliminarformulario6A, name="eliminarformulario6A"),
#===========================================================================================================================================
    path('consultar_usuarios/', views.consultarusuarios, name="consultar_usuarios"),
    path('crear_usuario/', views.crearusuario, name="crear_usuario"),
    path('modificar_usuario/<int:pk>', views.modificarusuario, name="modificar_usuario"),
    path('eliminar_usuario/<int:pk>', views.eliminarusuario, name="eliminar_usuario"),


    #roles
    path('consultar_roles/', views.consultarroles, name="consultar_roles"),
    path('crear_rol/', views.crearrol, name="crear_rol"),
    path('modificar_rol/<int:pk>', views.modificarrol, name="modificar_rol"),
    path('eliminar_rol/<int:pk>', views.eliminarrol, name="eliminar_rol"),

    # roles y usuarios relacionados
    path('consultar_roles_usuarios/', views.consultarrolesusuarios, name="consultar_roles_usuarios"),
    path('crear_rol_usuario/', views.crearrolusuario, name="crear_rol_usuario"),
    path('modificar_rol_usuario/<int:pk>', views.modificarrolusuario, name="modificar_rol_usuario"),
    path('eliminar_rol_usuario/<int:pk>', views.eliminarrolusuario, name="eliminar_rol_usuario"),
]
