release: python BooksRESTAPI/manage.py migrate
web: gunicorn BooksRESTAPI.BooksRESTAPI.wsgi --preload --log-file - --log-level debug