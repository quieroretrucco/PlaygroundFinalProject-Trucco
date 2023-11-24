from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from APPFinal.models import Departamento, Avatar
from APPFinal.forms import DepartamentoFormulario, UserRegisterForm, UserEditForm
from django.shortcuts import get_object_or_404


def departamento(self):
  departamento = Departamento()
  departamento.save() 

def inicio(request):
    return render(request,"APPFinal/index.html")

def departamentoFormulario(request):
    if request.method == "POST":
        miFormulario = DepartamentoFormulario(request.POST)
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, "APPFinal/index.html")
    else:
        miFormulario = DepartamentoFormulario()
    return render(request, "APPFinal/departamento_formulario.html", {"miFormulario": miFormulario})


def buscar_barrio(request):
    return render(request, 'APPFinal/buscar_barrio.html')

def buscar(request):
      if request.GET['barrio']:
        barrio = request.GET['barrio']
        departamento = Departamento.objects.filter(barrio__icontains=barrio)
        return render(request, 'APPFinal/resultados_busqueda.html', {'barrio': barrio, 'departamento': departamento})
      else:
        respuesta = 'No enviaste datos.'
        return HttpResponse(respuesta)


class DepartamentosLista(ListView):
    model = Departamento
    context_object_name = "departamentos"
    template_name = "APPFinal/depto_lista.html"

class DepartamentosDetalle(DetailView):
    model = Departamento
    template_name = "APPFinal/depto_detalle.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        print(f"Debug: Object retrieved - {obj}")
        return obj


class DepartamentosCrear(CreateView): 
    model = Departamento
    template_name = "APPFinal/depto_crear.html"
    success_url = reverse_lazy('ListaDepartamentos')
    form_class = DepartamentoFormulario
    #fields = ['barrio', 'direccion', 'piso', 'depto', 'descripcion']


class DepartamentosEditar(UpdateView):
    model = Departamento
    template_name = "APPFinal/depto_editar.html"
    success_url = reverse_lazy('ListaDepartamentos')
    fields = ['barrio', 'direccion', 'piso', 'depto', 'descripcion']


class DepartamentosBorrar(DeleteView): #funciona, el mensaje previo a borrar no muestra los campos y faltaria mensaje de "Borrado"
    model = Departamento    
    template_name = "APPFinal/depto_borrar.html"
    success_url = reverse_lazy('ListaDepartamentos')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            login(request, user)            
            return render(request, "APPFinal/index.html", {"mensaje": f'Bienvenido {user.username}'})
    else:
        form = AuthenticationForm()
    return render(request, "APPFinal/login.html", {"form": form})

def register(request):
      if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"APPFinal/index.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            form = UserRegisterForm()        
      return render(request,"APPFinal/registro.html" ,  {"form":form})


def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()
            miFormulario.save()
            return render(request, "APPFinal/index.html")
    else:
        miFormulario = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)
    return render(request, "APPFinal/editarperfil.html", {"miFormulario": miFormulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'APPFinal/cambiar_contrasenia.html'
    success_url = reverse_lazy('EditarPerfil')

def serve_avatar(request, user_id):
    avatar = get_object_or_404(Avatar, user_id=user_id)
    response = HttpResponse(avatar.imagen, content_type='image/jpeg')
    return response