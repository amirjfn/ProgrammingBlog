from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserEditForm


def Login_view(request):
    if request.user.is_authenticated == True:
        return redirect('home:home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home:home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', context={'form': form})

def register_view(request):
    context = {'errors': []}
    if request.user.is_authenticated == True:
        return redirect('home:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            context['errors'].append('passwords are not same')
            return render(request, 'account/reqister.html', context)

        user1 =User.objects.create(username=username, password=password1, email=email )
        login(request, user1)
        return redirect('home:home')
    return render(request, 'account/reqister.html')

def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == 'POST':
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'account/edit.html', context={'form':form})


def logout_view(request):
    logout(request)
    return redirect('/')