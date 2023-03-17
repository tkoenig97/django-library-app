from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    book_info = []
    books = Book.objects.prefetch_related('author')
    for book in books:
        print(book.authors.all().values())
    return render(request, 'pages/books.html')

def books_by_genre(request, id):
    pass

def books_by_author(request, id):
    pass

def book(request, id):
    pass