from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Avg, Count, Min, Sum
from charity_app.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        bags = Donation.objects.all().annotate(total_bags=Sum('quantity')).aggregate(Sum('total_bags'))
        institutions = Institution.objects.all().count()
        foundations = Institution.objects.filter(type=1)
        nto = Institution.objects.filter(type=2)
        local_charity = Institution.objects.filter(type=3)
        context = {'bags': bags, 'institutions': institutions, 'foundations': foundations,
                   'nto': nto, 'local_charity': local_charity}
        return render(request, 'charity_app/index.html', context)

class AddDonationView(View):

    def get(self, request):
        return render(request, 'charity_app/form.html')

class LoginView(View):

    def get(self, request):
        return render(request, 'charity_app/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        auth_user = authenticate(username=user.username, password=password)
        if auth_user:
            login(request, auth_user)
            return render(request, 'charity_app/login.html')
        else:
            return render(request, 'charity_app/login.html')


class RegisterView(View):

    def get(self, request):
        return render(request, 'charity_app/register.html')
