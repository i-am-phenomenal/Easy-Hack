from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os

def index(request): 
    return render(request, "home.html", {})

@csrf_exempt
def shutDown(request): 
    print("11111111111111111111111111111111111")
    os.system("shutdown /s /t 1")
    return render(request, "home.html", {})