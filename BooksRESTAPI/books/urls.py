from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import debug_toolbar

from .views import BookListView, detail

urlpatterns = [
    path('',  BookListView.as_view(), name='books'),
    path(r'^(?P<book_id>[0-9]+)/$', detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
