from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def index(request):
    return render(request, 'core/index.html', {})

def login_sistema(request):
    if request.user.is_authenticated:
        return redirect('core:index')
    
    if request.method == "POST":
        username = request.POST.get('login')
        password = request.POST.get('password')
        
        usuario = authenticate(request, username=username, password=password)
        
        if usuario:
            login(request, usuario)
            return redirect('core:index')
        else:
            return render(request, 'core/login.html', {'erro': 'Usuário ou senha inválidos.'})
    
    return render(request, 'core/login.html', {})

@login_required(login_url='/login')
def logout_sistema(request):
    logout(request)
    return redirect('core:login_sistema')