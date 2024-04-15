from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from CupDraft.models import Country
from CupDraft.serializers import CountrySerializer
from django.http.response import JsonResponse
from django.http import Http404

import CupDraft.draft as draft

start = 0
offset = 4

pot1 = Country.objects.all().order_by('CountryRank')[start:offset]
pot2 = Country.objects.all().order_by('CountryRank')[start+4:offset+4]
pot3 = Country.objects.all().order_by('CountryRank')[start+8:offset+8]
pot4 = Country.objects.all().order_by('CountryRank')[start+12:]

# pot1 = []
# pot2 = []
# pot3 = []
# pot4 = []




draftApp = draft.Draft(list(pot1),list(pot2),list(pot3),list(pot4))

# Create your views here.
@csrf_exempt
def countryApi(request, id=0):
    if request.method == 'GET':
        countries = Country.objects.all().order_by('CountryRank')
        country_serializer = CountrySerializer(countries, many= True)
        return JsonResponse(country_serializer.data, safe=False)
    
@csrf_exempt
def startDraft(request):
    if request.method == 'GET':
        draftApp.sorteoCA(list(pot1),list(pot2),list(pot3),list(pot4))
        while not draftApp.isValid():
            draftApp.resetAll()
            draftApp.sorteoCA(list(pot1),list(pot2),list(pot3),list(pot4))
            print(draftApp.isValid())
        
        #print(draftApp.isValid())
        return JsonResponse('Succes!', safe=False)



@csrf_exempt
def ResetApp(request):
    if request.method == 'DELETE':
        #init the pots 
        draftApp.resetAll()
        return JsonResponse('Reset Successfuly',safe =False)
    
@csrf_exempt
def groupApi(request, groupName):
    if request.method == 'GET':
        if groupName == 'A':
            countries = draftApp.GA
        elif groupName == 'B':
            countries = draftApp.GB
        elif groupName == 'C':
            countries = draftApp.GC
        elif groupName == 'D':
            countries = draftApp.GD
        else:
            countries = []
        country_serializer = CountrySerializer(countries, many= True)
        return JsonResponse(country_serializer.data, safe=False)

@csrf_exempt
def groupAApi(request):
    if request.method == 'GET':
        countries = draftApp.GA
        country_serializer = CountrySerializer(countries, many= True)
        return JsonResponse(country_serializer.data, safe=False)

@csrf_exempt
def groupBApi(request):
    if request.method == 'GET':
        countries = draftApp.GB
        country_serializer = CountrySerializer(countries, many= True)
        
        return JsonResponse(country_serializer.data, safe=False) 

@csrf_exempt
def groupCApi(request):
    if request.method == 'GET':
        countries = draftApp.GC
        country_serializer = CountrySerializer(countries, many= True)
        
        return JsonResponse(country_serializer.data, safe=False)
    
@csrf_exempt
def groupDApi(request):
    if request.method == 'GET':
        countries = draftApp.GD
        country_serializer = CountrySerializer(countries, many= True)
        return JsonResponse(country_serializer.data, safe=False)
    
@csrf_exempt
def getCountryByCode(request, countryCode):
    if request.method == 'GET':

        print(countryCode)
        try:
            country = Country.objects.get(CountryCode= countryCode)
            country_serializer = CountrySerializer(country)
            return JsonResponse(country_serializer.data,safe=False)
        except Country.DoesNotExist:
            return JsonResponse(Http404("Country not found"))
        
@csrf_exempt
def setKOPhase(request):
    if request.method == 'GET':
        setGroups()
        #print(draftApp.isValid())
        return JsonResponse('Succes!', safe=False)
        
def setGroups():
    if checkIfEmpty(draftApp.GA) and checkIfEmpty(draftApp.GB) and checkIfEmpty(draftApp.GC) and checkIfEmpty(draftApp.GD):
        countriesA = [Country.objects.get(CountryCode= 'ARG'),Country.objects.get(CountryCode= 'PER'),Country.objects.get(CountryCode= 'CHI'),Country.objects.get(CountryCode= 'CF5')]
        countriesB = [Country.objects.get(CountryCode= 'MEX'),Country.objects.get(CountryCode= 'ECU'),Country.objects.get(CountryCode= 'VEN'),Country.objects.get(CountryCode= 'JAM')]
        countriesC = [Country.objects.get(CountryCode= 'USA'),Country.objects.get(CountryCode= 'URU'),Country.objects.get(CountryCode= 'PAN'),Country.objects.get(CountryCode= 'BOL')]
        countriesD = [Country.objects.get(CountryCode= 'BRA'),Country.objects.get(CountryCode= 'COL'),Country.objects.get(CountryCode= 'PAR'),Country.objects.get(CountryCode= 'CF6')]
        
        draftApp.GA = countriesA
        draftApp.GB = countriesB
        draftApp.GC = countriesC
        draftApp.GD = countriesD



def checkIfEmpty(groupList):
    return all([elem == None for elem in groupList])