from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate,login, logout
# Create your views here.


def userout(request):
    logout(request)
    return HttpResponse("logout")


def userin(request):
    return HttpResponse("login")