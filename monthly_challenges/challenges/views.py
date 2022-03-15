from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


# Create your views here.

months = {
    "january": "This is january",
    "february": "This is february",
    "march": "This is march",
    "april": "This is april",
    "may": "This is may",
    "june": "This is june",
    "july": "This is july",
    "august": "This is august",
    "september": "This is september",
    "october": "This is october",
    "november": "This is november",
    "december": "This is december",
}


def index(request):
    list_item = ""
    month_list = list(months.keys())
    for month in month_list:
        list_item += f"<li><a href=\"{month}\">{month}</a></li>"
    data = f"<ul>{list_item}</ul>"
    return HttpResponse(data)


def monthly_challenge(request, month):
    print(str(type(month))+f"This is month: ${type(month) is int}")
    if type(month) is int:
        if(month <= 12 and month >= 1):
            keys = list(months.keys())[month-1]
            return HttpResponseRedirect(keys)
        else:
            return HttpResponseNotFound("Invalid Number")
    month_result = months.get(month)
    if month_result is None:
        print("returning 404")
        return HttpResponseNotFound()
    else:
        return HttpResponse(
            f'''<h1>This is {month} req:
         \n{month_result}</h1>'''
         )
