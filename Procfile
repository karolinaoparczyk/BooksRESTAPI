release: python manage.py migrate
web: gunicorn BooksRESTAPI.wsgi --preload --log-file - --log-level debug