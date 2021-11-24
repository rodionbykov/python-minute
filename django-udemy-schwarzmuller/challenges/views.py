from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

challenges = {
    "january": "Get warm",
    "february": None,
    "march": "Allergies",
    "april": "Go outside",
    "may": "Walk in forest",
    "june": "Seaside",
    "july": "Sun blocker applied",
    "august": "Vegetables and fruit",
    "september": "School time",
    "october": "Pumpkins",
    "november": "Cold rains",
    "december": "Family meetings"
}


def index(request):
    month_names = list(challenges.keys())

    return render(request, "challenges/index.html", {
        "months": month_names
    })


def challenges_by_month_number(request, month_number):
    month_names = list(challenges.keys())

    if month_number > len(month_names):
        return HttpResponseNotFound("Month not found")

    month = month_names[month_number - 1] # for 0 based list
    redirect_path = reverse("monthly_challenge", args=[month]) # will take actual URL from urls file
    return HttpResponseRedirect(redirect_path)


def challenges_by_month_name(request, month_name):
    try:
        return render(request, "challenges\challenge.html", {
            "challenge_month": month_name,
            "challenge_text": challenges[month_name]
        })
    except:
        raise Http404()
