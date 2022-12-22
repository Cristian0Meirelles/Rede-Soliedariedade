from django.contrib import messages
from django.shortcuts import render, redirect
from gestao_de_doacoes.decorators import not_auth, is_auth
from django.contrib.auth import authenticate, login, logout

@not_auth
def login_action(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, "Usuário não encontrado")
            return redirect('login')
    else:
        return render(request, 'login.html')

@is_auth
def logout_action(request):
    logout(request)
    return redirect('login')