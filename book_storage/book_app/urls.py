from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('genre/<int:id>/', views.books_by_genre),
    path('author/<int:id>/', views.books_by_author),
    path('book/<int:id>/', views.book),
]