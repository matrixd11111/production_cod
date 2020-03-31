from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from .forms import PlayerRegisterForm


def login(request):
    username = request.POST.get('login')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    print()
    if user:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    return render(request, 'authapp/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def registred(request):
    form = PlayerRegisterForm()
    if request.method == 'POST':
        form = PlayerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'form': form}
    return render(request, 'authapp/registration.html', context)
