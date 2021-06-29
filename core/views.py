from django.contrib.auth import authenticate, login
from core.forms import PlanForm
from django.shortcuts import redirect, render
from .models import Plan
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PlanForm, CustomUserForm

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def productos(request):
    return render(request,'core/productos.html')

def planmobile(request):
    return render(request,'core/planmobile.html')

@permission_required('core.view_plan')
def listado_planes(request):
    planes = Plan.objects.all()
    data = {
        'planes':planes
    }
    return render(request, 'core/listado_planes.html', data)

@permission_required('core.add_plan')
def nuevo_plan(request):
    data = {
        'form':PlanForm()
    }
    if request.method == 'POST':
        formulario = PlanForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = "Guardado Correctamente"
        data['form'] = formulario
        
    
    return render(request, 'core/nuevo_plan.html',data)

@permission_required('core.change_plan')
def modificar_plan(request, id):
    plan = Plan.objects.get(id=id)
    data = {
        'form':PlanForm(instance=plan)
    }
    if request.method == 'POST':
        formulario = PlanForm(data=request.POST, instance=plan)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = "Modificado Correctamente"
        data ['form'] = formulario
    
    return render(request, 'core/modificar_plan.html',data)

@permission_required('core.delete_plan','core.add_plan')
def eliminar_plan(request, id):
    plan = Plan.objects.get(id=id)
    plan.delete()

    return redirect(to="listado_planes")

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    

    return render(request, "registration/registrar.html", data)

def internethogar(request):
    return render(request,'core/internethogar.html')

def telefoniahogar(request):
    return render(request,'core/telefoniahogar.html')

def nuestraempresa(request):
    return render(request,'core/nuestraempresa.html')

def normativaslegales(request):
    return render(request,'core/normativaslegales.html')

@login_required
def formulario(request):
    return render(request,'core/formulario.html')

@login_required
def realizarpago(request):
    return render(request,'core/realizarpago.html')
    