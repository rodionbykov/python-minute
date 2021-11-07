from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

challenges = {
    "january": "Do not overeat",
    "february": "Get warm",
    "march": "Allergies",
    "april": "Go outside",
    "may": "Walk in forest",
    "june": "Seaside",
    "july": "Sun blocker applied",
    "august": "Vegetables and fruit",
    "september": "Schooltime",
    "october": "Pumpkins",
    "november": "Cold rains",
    "december": "Family meetings"
}

def index_by_number(request, month_number):
    month_names = list(challenges.keys())

    if month_number > len(month_names):
        return HttpResponseNotFound("Month not found")

    month = month_names[month_number - 1] # for 0 based list
    redirect_path = reverse("index", args=[month]) # will take actual URL from urls file
    return HttpResponseRedirect(redirect_path)

def index(request, month):
    return_text = ""
    try:
        return_text = challenges[month]
        return HttpResponse(return_text)
    except:
        return HttpResponse("Challenge not found")
