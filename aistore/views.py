from django.shortcuts import render

def home(request):
    return render(request, 'aistore/aistore-home.html')
