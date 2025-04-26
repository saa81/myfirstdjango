from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def hello(request):
    return HttpResponse("Привет мир, это моё первое прдеставление!")

def greet(request, name):
    return HttpResponse(f"Привет, {name}! Рад тебя видеть!")

def book_list(request):
    books = Book.objects.all()
    books_text = ', '.join([books.title for book in books])
    return HttpResponse(f"Ваши книги {books_text}")

def my_page(request):
    return render(request, template_name='index.html')

def pt(request):
    return render(request, template_name='pt-05.html')



def how_are_you(request):
    return HttpResponse("Как дела?")

def good_bye(request):
    return HttpResponse("Пока!")

