from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
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
    genre = Genre.objects.get(id = id)
    books = Book.objects.all().filter(genre = genre)
    data = {
        'books' : books,
        'nested' : False
    }
    return render(request, 'pages/books.html', data)

def books_by_author(request, id):
    author = Author.objects.get(id = id)
    
    data = {
        'books' : Author.objects.get(id = id).book.all(),
        'title': author,
        'nested':False
    }
    
    return render(request, 'pages/books.html', data)

@csrf_exempt
def book(request, id):
    try:
        my_book = Book.objects.all().get(id = id)
        if request.method == 'GET':
            book = Book.objects.prefetch_related('authors').get(id = id)
            book_info = [{
                    'book': book,
                    'authors': book.authors.all()
                }]
            
            return render(request, 'pages/books.html', {"books":book_info, 'nested':True})
        
        if request.method == 'PUT':
            body = json.loads(request.body)
            print(body)
            my_book.quantity = body['quantity']
            my_book.save()
            
        if request.method == 'DELETE':
            my_book.delete()
    
        return JsonResponse({'success': True})
    
    except Exception as e:
        print(e)
        return JsonResponse({'success': False})
    
def new_book(request):
    if request.method == 'POST':
        print(request.POST)
        body = request.POST
        new_book = Book.objects.create(title = body['title'], quantity = body['quantity'], genre = Genre.objects.all().get(title = body['genre']))
        valid_authors =[author['first_name'] for author in list(Author.objects.all().values())]
        for author in valid_authors:
            new_book.authors.add(Author.objects.all().get(first_name = author)) if author in body else None
        new_book.save()
        return redirect('home')
    return render(request, 'pages/book.html')