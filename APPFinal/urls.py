from django.urls import path
from APPFinal import views
from django.shortcuts import render
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('departamentoformulario/', views.departamentoFormulario, name="DepartamentoFormulario"),
    path('buscarBarrio/', views.buscar_barrio, name="BuscarBarrio"),
    path('buscarBarrio/buscar/', views.buscar),
    path('departamentos/lista', views.DepartamentosLista.as_view(), name = "ListaDepartamentos"),
    path('departamentos/nuevo', views.DepartamentosCrear.as_view(), name = "NuevoDepartamento"),
    path('departamentos/<int:pk>', views.DepartamentosDetalle.as_view(), name="DetalleDepartamento"),
    path('departamentos/<pk>/editar', views.DepartamentosEditar.as_view(), name = "EditarDepartamento"),
    path('departamentos/<pk>/borrar', views.DepartamentosBorrar.as_view(), name = "BorrarDepartamento"),
    path('login/', views.login_request, name="Login"),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='APPFinal/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('cambiarContrasenia', views.CambiarContrasenia.as_view(), name="CambiarContrasenia"),
    path('avatar/<int:user_id>/', views.serve_avatar, name='serve_avatar'),
    path('acercademi/', views.acerca_de_mi, name="Acerca de mi")
    ]
    
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)