from django.shortcuts import render


def home(request):
    data = {}
    return render(request, 'core/home.html', data)