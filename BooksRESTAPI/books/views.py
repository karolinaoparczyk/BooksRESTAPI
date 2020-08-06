from django.http import HttpResponse
from django.views.generic import TemplateView
from django_tables2 import SingleTableView, RequestConfig

from .filters import BookFilter, BookFilterFormHelper
from .models import Book
from .tables.tables import BookTable


class BookTableView(TemplateView):
    template_name = 'books/book_list.html'

    def get_queryset(self, **kwargs):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookTableView, self).get_context_data(**kwargs)
        my_filter = BookFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        my_filter.form.helper = BookFilterFormHelper()
        table = BookTable(my_filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = my_filter
        context['table'] = table
        return context

def detail(request, book_id):
    return HttpResponse("book %s" % book_id)

