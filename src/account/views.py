from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm, AccountUpdateForm

# Create your views here.

# Registration


def registration_view(request):
    template = 'account/register.html'
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pw = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_pw)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  # request.GET
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, template, context)

# Log out


def logout_view(request):
    logout(request)
    return redirect('home')

#  Log in


def login_view(request):
    template = 'account/login.html'
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, template, context)

# Account Update


def account_view(request):
    template = 'account/account.html'
    context = {}
    if not request.user.is_authenticated:
        return redirect('login')

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                'email': request.POST['email'],
                'username': request.POST['username']
            }
            form.save()
            context['success_message'] = "User account has been updated"

    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username
            }
        )

    context['account_form'] = form
    return render(request, template, context)
