from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    book_info = []
    books = Book.objects.prefetch_related('author')
    for book in books:
        book_info.append({
        'book' : book,
        'authors' : book.authors.all()
        })
        print(book_info)
        
        
    return render(request, 'pages/books.html', {"books":book_info, "nested":True})

def books_by_genre(request, id):
    pass

def books_by_author(request, id):
    author = Author.objects.get(id = id)
    data = {
        'books' : Author.objects.get(id = id).book.all(),
        'nested': False
    }
    
    return render(request, 'pages/books.html', data)

def book(request, id):
    pass