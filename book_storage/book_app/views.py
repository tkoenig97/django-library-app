from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
# Create your views here.

def home(request):
    book_info = []
    books = Book.objects.prefetch_related('authors')
    for book in books:
        book_info.append({
            'book': book,
            'authors': book.authors.all()
        })
    return render(request, 'pages/books.html', {"books":book_info, 'nested':True})

def books_by_genre(request, id):
    pass

def books_by_author(request, id):
    author = Author.objects.get(id = id)
    
    data = {
        'books' : Author.objects.get(id = id).book.all(),
        'title': author,
        'nested':False
    }
    
    return render(request, 'pages/books.html', data)


def book(request, id):
    pass