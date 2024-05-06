from django.shortcuts import render

def carslist(request):
    return render(request, 'carslist.html')