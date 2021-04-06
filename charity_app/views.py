import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Avg, Count, Min, Sum
from rest_framework import viewsets, permissions, generics, mixins, filters
from rest_framework.viewsets import ModelViewSet

from charity_app.models import Donation, Institution, Category
from charity_app.serializers import InstitutionSerializer


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
        foundation = Institution.objects.all()
        foundation_type = Institution.ORGANISATION_TYPE
        foundation_category = Category.objects.all().distinct()
        context = {'foundation': foundation, 'foundation_type': foundation_type,
                   'foundation_category': foundation_category}
        return render(request, 'charity_app/form.html', context)

def get_institutions_by_type(request):
    type_ids = request.GET.getlist('type_ids')
    if type_ids is not None:
        foundation = Institution.objects.filter(categories__in=type_ids).values_list()
    else:
        foundation = Institution.objects.all().values_list()
    # context = {'foundation': foundation}
    # return render(request, 'charity_app/form.html', context)
    return JsonResponse(list(foundation), safe=False)



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

# class InstitutionViewSet(generics.ListAPIView):
#     serializer_class = InstitutionSerializer
#     # API endpoint
#     def get_queryset(self):
#         # type_ids = 3
#         type_ids = self.request.query_params.get('type_ids') # not working!
#         type_ids = str(type_ids)
#         queryset = Institution.objects.filter(categories=type_ids)
#         return queryset




# class InstitutionApiView(generics.ListAPIView):
#     serializer_class = Institution
#
#     def get_queryset(self, **kwargs):
#         """
#         Optionally restricts the returned purchases to a given user,
#         by filtering against a `username` query parameter in the URL.
#         """
#         queryset = Institution.objects.all()
#         inst = self.request.query_params.get('ids')
#         if inst is not None:
#             queryset = queryset.filter(id=inst)
#         return queryset