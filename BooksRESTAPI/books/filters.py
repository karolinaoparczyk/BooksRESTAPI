import crispy_forms
from crispy_forms.layout import Layout, Submit
from django_filters import FilterSet

from .models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = ['published_date']

class BookFilterFormHelper(crispy_forms.helper.FormHelper):
    form_method = 'GET'
    layout = Layout(
        'published_date',
        Submit('submit', 'Search', css_class='btn-primary'),
    )