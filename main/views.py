from django.shortcuts import render

def indexPage(requests):
    return render(requests, 'index.html')