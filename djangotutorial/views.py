from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def json(request):
    return JsonResponse({'foo':'bar'})