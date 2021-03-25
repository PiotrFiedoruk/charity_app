from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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

class AddDonationView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'charity_app/form.html')

class LoginUserView(View):

    def get(self, request):
        return render(request, 'charity_app/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(username=email)
        auth_user = authenticate(username=user.email, password=password)
        if auth_user:
            login(request, auth_user)
            return render(request, 'charity_app/index.html')
        else:
            return render(request, 'charity_app/login.html')

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('landing_page')

class RegisterView(View):

    def get(self, request):
        return render(request, 'charity_app/register.html')

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            User.objects.create_user(username=email, email=email, first_name=name, last_name=surname, password=password)
            return redirect('login')
        else:
            return render(request, 'charity_app/register.html')
