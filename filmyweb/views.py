from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from filmyweb.models import Film

# Create your views here.

def test_response(request):
    films = Film.objects.all()
    test = 'test'
    return render(request, 'filmyweb/starting.html', {'films': films})
