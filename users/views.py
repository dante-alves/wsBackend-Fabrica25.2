from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout



def register_view(request):
    if request.method == "POST": #if the form is submited and is POST
        form = UserCreationForm(request.POST) # form recebe os dados
        if form.is_valid(): # verifica se é válido para salvar
            login(request, form.save()) # isso é para automaticamente logar o usuário ao registrar e com form.save() salvar no banco de dados
            return redirect("posts:list")
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user()) # isso serve para logar
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("posts:list")