from django.shortcuts import render
from  django.core.handlers.wsgi import WSGIRequest
from .models import Book,Author,Review


def home(request: WSGIRequest):
    books=Book.objects.all()
    return render(request,'home.html',{'books':books})
# Create your views here.

def author(request:WSGIRequest):
    author=Author.objects.all()
    return render(request,'authors.html',{'author':author})

def coments(request : WSGIRequest):
    reviews=Review.object.all()
    return render(request,'comments.html',{'reviews':reviews})