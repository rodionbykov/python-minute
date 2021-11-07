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

def index(request):
    list_items = ""
    month_names = list(challenges.keys())

    for month_name in month_names:
        capitalized_month_name = month_name.capitalize()
        month_path = reverse("monthly_challenge", args=[month_name])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month_name}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def challenges_by_month_number(request, month_number):
    month_names = list(challenges.keys())

    if month_number > len(month_names):
        return HttpResponseNotFound("Month not found")

    month = month_names[month_number - 1] # for 0 based list
    redirect_path = reverse("monthly_challenge", args=[month]) # will take actual URL from urls file
    return HttpResponseRedirect(redirect_path)

def challenges_by_month_name(request, month):
    return_text = ""
    try:
        return_text = challenges[month]
        return HttpResponse(return_text)
    except:
        return HttpResponseNotFound("Challenge not found")
