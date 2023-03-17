from django.shortcuts import render
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
        
        
    return render(request, 'pages/books.html', {"books":book_info})

def books_by_genre(request, id):
    pass

def books_by_author(request, id):
    pass

def book(request, id):
    pass