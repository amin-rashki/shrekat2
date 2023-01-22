from django.shortcuts import render



def farm(request):
    return render(request, 'farmer/farm.html')
