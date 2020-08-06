import django_tables2 as tables
from django_tables2 import TemplateColumn

from ..models import Book


class BookTable(tables.Table):
    title = tables.Column(orderable=False)
    published_date = tables.Column(order_by='published_date')
    edit = TemplateColumn(template_name='tables/open_details_column.html', verbose_name="")

    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
        fields = ('title', 'published_date', 'edit', )
