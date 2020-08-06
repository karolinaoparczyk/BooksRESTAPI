from django.http import HttpResponse
from django_tables2 import SingleTableView

from .filters import BookFilter
from .models import Book
from .tables.tables import BookTable


class BookListView(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = 'books/book_list.html'
    filterset_class = BookFilter
    

def detail(request, book_id):
    return HttpResponse("book %s" % book_id)

