from django.http import HttpResponse
from django.template import loader

from .models import Book


def books(request):
    books_list = Book.objects.all()
    template = loader.get_template('books/books_list.html')
    context = {
        'books': books_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, book_id):
    return HttpResponse("book %s" % book_id)

