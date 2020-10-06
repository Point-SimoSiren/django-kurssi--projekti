from django.shortcuts import render

def landingview(request):
    return render (request, "landingpage.html")
