from django.shortcuts import render

from .models import Book

def home_view(request):
    return render(request, 'home.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books.html', context={'books': books})