import requests
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django_tables2 import RequestConfig
from rest_framework import generics, permissions

from .filters import BookFilter, BookFilterFormHelper
from .get_external_data import insert_data
from .models import Book
from .serializers import BookSerializer
from .tables.tables import BookTable


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookTableView(TemplateView):
    template_name = 'books/book_list.html'

    def get_queryset(self, **kwargs):
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=Hobbit")
        # response = requests.get("http://127.0.0.1:8000/books/apibooks/")
        data = response.json()
        insert_data(data, True)
        # insert_data(data)
        book_list = Book.objects.order_by('-published_date')
        return book_list

    def get_context_data(self, **kwargs):
        context = super(BookTableView, self).get_context_data(**kwargs)
        my_filter = BookFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        has_filter = any(field in self.request.GET for field in set(my_filter.get_fields()))
        my_filter.form.helper = BookFilterFormHelper()
        table = BookTable(my_filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = my_filter
        context['has_filter'] = has_filter
        context['table'] = table
        return context

def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'books/book_details.html', {'book': book})


def get_books(request):
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=war')
    data = response.json()
    insert_data(data, True)
    return redirect('books')
