from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse


def getroute(request):
    return JsonResponse('Our Api',safe=False)