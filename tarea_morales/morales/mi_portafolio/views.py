from datetime import timedelta # Importa timedelta
from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Pelicula
from .forms import ProfileForm
from .models import Profile

# Create your views here.

def index(request):
    return render(request,'mi_portafolio/index.html',{})


def perfil_peliculas(request):
    # Obtén las películas que quieres mostrar en el perfil
    peliculas_favoritas = Pelicula.objects.filter(mas_veces_vistas__gt=5)

    # Calcula la fecha de la última semana de estreno
    ultima_semana_de_estreno = timezone.now() - timedelta(days=7)

    # Obtén las últimas películas vistas en la última semana de estreno
    ultimas_peliculas_vistas = Pelicula.objects.filter(fecha_estreno__gte=ultima_semana_de_estreno.year)

    return render(request, 'mi_portafolio/perfil_peliculas.html', {
        'peliculas_favoritas': peliculas_favoritas,
        'ultimas_peliculas_vistas': ultimas_peliculas_vistas,
    })

    
def list_profiles(request):
    profile_list = Profile.objects.all().order_by('id')
    return render(request,"mi_portafolio/profile.html",{"profile_list":profile_list})

def new_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profiles_temp = Profile.objects.filter(first_name=profile.first_name,last_name=profile.last_name,address=profile.address)
            print(profiles_temp)
            if len(profiles_temp) >0:
                return redirect('index')
            else:
                profile.save()
                return redirect('profile')
    else:
        form = ProfileForm()
        return render(request,"mi_portafolio/profile-form.html",{'form':form})

def view_profile(request,id):
    profile = Profile.objects.get(id=id)
    return render(request,'mi_portafolio/view-profile.html',{'data':profile})
