from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests
import googlemaps
from django.views.decorators.csrf import csrf_exempt
from .models import Location

from .models import * 

def main(request):
	return render(request,'main.html')
def uploaddata(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')
        location = Location(latitude=lat, longitude=lng)
        location.save()
        print(lat,lng)
        print("HI")




    return render(request, 'uploaddata.html')















