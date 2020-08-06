from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import BookTableView, detail, get_books, BookDetail, BookList

urlpatterns = [
    path('',  BookTableView.as_view(), name='books'),
    path('<book_id>', detail, name='detail'),
    path('get_books/', get_books, name='get_books'),
    path('apibooks/', BookList.as_view()),
    path('apibooks/<int:pk>/', BookDetail.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
