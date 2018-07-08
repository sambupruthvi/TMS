from django.shortcuts import render

def welcome(request):
    return render(request, "accounts/home.html")
