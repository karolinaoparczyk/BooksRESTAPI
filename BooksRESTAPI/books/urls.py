from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import BookTableView, detail, get_books, BookDetail, BookList

urlpatterns = [
                  path('login/', LoginView.as_view(), {'template_name': 'djangobin/login.html'}, name='login'),
                  path('logout/', LogoutView.as_view(), {'next_page': 'login/'}, name='logout'),
                  path('books/', login_required(BookTableView.as_view()), name='books'),
                  path('books/<book_id>', detail, name='detail'),
                  path('books/get_books/', get_books, name='get_books'),
                  path('books/apibooks/', BookList.as_view()),
                  path('books/apibooks/<int:pk>/', BookDetail.as_view()),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
