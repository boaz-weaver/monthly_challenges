from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect



monthly_challenges = {
    "january": "Eat no meat the entire month!",
    "february": "Walk for at least 30 minutes every day!",
    "march": "Learn django for 20 minutes!",
    "april": "Eat no meat the entire month!",
    "may": "Walk for at least 30 minutes every day!",
    "june": "Learn django for 20 minutes!",
    "july": "Eat no meat the entire month!",
    "august": "Walk for at least 30 minutes every day!",
    "september": "Learn django for 20 minutes!",
    "october": "Eat no meat the entire month!",
    "november": "Walk for at least 30 minutes every day!",
    "december": "Learn django for 20 minutes!"
}


# Create your views here.

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months) or month == 0:
        return HttpResponseNotFound("Invalid month")        

    redirect_month = months[month -1]    
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:        
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
