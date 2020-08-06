import crispy_forms
import django_filters
from crispy_forms.layout import Layout, Submit, Button, Reset
from django_filters import FilterSet

from .models import Book


class BookFilter(FilterSet):
    published_date = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Book
        fields = ['published_date', 'authors']

class BookFilterFormHelper(crispy_forms.helper.FormHelper):
    form_method = 'GET'
    form_class = 'form-horizontal'
    label_class = 'col-lg-2'
    field_class = 'col-lg-8'
    layout = Layout(
        'published_date',
        'authors',
        Submit('submit', 'Search',),
    )