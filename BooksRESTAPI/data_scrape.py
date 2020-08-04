import json
import re

import requests
from bs4 import BeautifulSoup

url = 'https://www.googleapis.com/books/v1/volumes?q=Hobbit'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

quotes_soup = soup.text.replace(r'\u003cb\u003e', 'quotesign')
quotes_soup2 = quotes_soup.replace(r'\u003c/b\u003e', 'quotesign')
quotes_soup3 = quotes_soup2.replace('"The Hobbit,"', 'quotesignTheHobbitquotesign,')
quotes_soup4 = quotes_soup3.replace(r'\u003cbr\u003e', ' ')
quotes_soup5 = quotes_soup4.replace('"an adorable', 'quotesignan adorable')
quotes_soup6 = quotes_soup5.replace('story"', 'storyquotesign')
quotes_soup7 = quotes_soup6.replace('"The Hobbit: An Unexpected Journey" ',
                                    'quotesignThe Hobbit: An Unexpected Journeyquotesign')
json_soup = json.loads(quotes_soup7)

books = []
authors = []
categories = []
for i in range(len(json_soup['items'])):
    book_item = json_soup['items'][i]['volumeInfo']

    author_pks = []
    for k in range(len(book_item['authors'])):
        author_details = {
            'model': 'books.author',
            'pk': i+k+1,
            'fields': {
                'name': book_item['authors'][k]
            }
        }
        authors.append(author_details)
        author_pks.append(i+k+1)

    categories_pks = []
    if book_item.get('categories') is not None:
        for j in range(len(book_item['categories'])):
            category_details = {
                'model': 'books.category',
                'pk': i + j + 1,
                'fields': {
                    'name': book_item['categories'][j]
                }
            }
            categories.append(category_details)
            categories_pks.append(i + j + 1)

    book_details = {
        'model': 'books.book',
        'pk': i,
        'fields': {
            'title': book_item['title'],
            'authors': author_pks,
            'published_date': book_item['publishedDate'],
            'categories': categories_pks,
            'ratings_count': book_item.get('ratingsCount'),
            'thumbnail': book_item['imageLinks']['thumbnail']
        }
    }
    books.append(book_details)

f = open("BooksRESTAPI/.env", "r")
db_name = ""
db_user = ""
db_password = ""
db_host = ""
for line in f:
    result = re.match("DB_NAME=.+", line)
    if result is not None:
        db_name = line[8:].replace('\n', '')

    result = re.match("DB_USER=.+", line)
    if result is not None:
        db_user = line[8:].replace('\n', '')

    result = re.match("DB_PASSWORD=.+", line)
    if result is not None:
        db_password = line[12:].replace('\n', '')

    result = re.match("DB_HOST=.+", line)
    if result is not None:
        db_host = line[8:].replace('\n', '')
f.close()

with open('books/fixtures/books.json', 'w') as outfile:
    json.dump(books, outfile)

categories_unique = []
categories_names_unique = []
for cat in categories:
       if cat['fields']['name'] not in categories_names_unique:
           categories_names_unique.append(cat['fields']['name'])
           categories_unique.append(cat)
with open('books/fixtures/categories.json', 'w') as outfile:
    json.dump(categories_unique, outfile)

authors_unique = []
authors_names_unique = []
for author in authors:
    if author['fields']['name'] not in authors_names_unique:
        authors_names_unique.append(author['fields']['name'])
        authors_unique.append(author)
with open('books/fixtures/authors.json', 'w') as outfile:
    json.dump(authors_unique, outfile)
