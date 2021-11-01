from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request, month):
    return_text = ""
    match month:
        case "january":
            return_text = "Do not overeat"
        case "february":
            return_text = "Get yourself warm"
        case _:
            return_text = "No challenge for you"
    return HttpResponse(return_text)
