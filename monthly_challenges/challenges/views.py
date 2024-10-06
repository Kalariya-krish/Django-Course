from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenge = {
    'january' : "Eat no meat for the entire month !",
    'february' : "Walk for at least 20 minutes every day !",
    'march' : "Learn django at least 20 minutes every  day !",
    'april' : "This is April !" ,
    'may' : "This is May !" ,
    'june' : "This is June !" ,
    'july' : "This is July !" ,
    'august' : "This is August !" ,
    'september' : "This is September !" ,
    'october' : "This is October !" ,
    'november' : "This is November !",
    'december' : "This is December !"
}

def monthly_challenges_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):
    try: 
        text = monthly_challenge[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("This month is not supported")