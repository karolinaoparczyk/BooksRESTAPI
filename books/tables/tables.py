import django_tables2 as tables
from django_tables2 import TemplateColumn

from ..filters import BookFilterFormHelper
from ..models import Book


class BookTable(tables.Table):
    title = tables.Column(orderable=False)
    published_date = tables.Column(order_by='published_date')
    edit = TemplateColumn(template_name='tables/details_column.html', verbose_name="")
    formhelper_class = BookFilterFormHelper

    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
        fields = ('title', 'published_date', 'authors', 'edit', )
