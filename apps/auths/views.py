# Django
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpRequest
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Local
from .forms import AuthsForm, RegForm
from .models import Client


class Authorization(View):
    """Authorization View."""

    template = 'authorization.html'
    form = AuthsForm

    def get(self, request: HttpRequest):
        """View template with form."""

        return render(
            request=request, 
            template_name=self.template,
            context={
                'form' : self.form,
            },
            status=200
        )

    def post(self, request: HttpRequest):
        """Data processing."""

        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                request=request,
                username=username,
                password=password
            )
            if user:
                login(request=request, user=user)
                return redirect(to='index.html')
            
            return render(
                request=request,
                template_name=self.template,
                context={
                    'form': self.form,
                    'errors': 'Неверный логин или пароль.'
                },
                status=400
            )

        return render(
            request=request,
            template_name=self.template,
            context={
                'form': self.form,
                'errors': form.errors
            },
            status=400
        )


class Registration(View):
    """View for Registration."""

    template = 'registration.html'
    form = RegForm

    def get(self, request: HttpRequest):
        return render(
            request=request,
            template_name=self.template,
            context={
                'form': self.form,
            },
            status=200
        )
    
    def post(self, request: HttpRequest):

        form = self.form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Client.objects.create_user(
                email=data['email'],
                username=data['username'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                password=data['password']
            )
            return render(
                request=request,
                template_name=self.template,
                context={
                    'form' : self.form,
                    'message' : 'success'
                },
                status=200
            )
        return render(
            request=request,
            template_name=self.template,
            context={
                'form' : self.form,
                'errors' : form.errors
            },
            status=400
        )


@method_decorator(
    login_required(login_url='/auth/login/'), 
    name='dispatch'
)
class Logout(View):
    """Logout user."""

    def get(self, request: HttpRequest):
        logout(request=request)
        return redirect(to='/auth/login/')
        
