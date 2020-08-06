from .models import Book, Author, Category


def insert_data(json, external_data=False):
    if external_data:
        json = json['items']
    for i in range(len(json)):
        if external_data:
            book_item = json[i]['volumeInfo']
            book = {
                'title': book_item['title'],
                'published_date': book_item['publishedDate'][:4],
                'average_rating': book_item.get('averageRating'),
                'ratings_count': book_item.get('ratingsCount'),
                'thumbnail': book_item['imageLinks']['thumbnail']
            }
        else:
            book_item = json[i]
            book = {
                'title': book_item['title'],
                'published_date': book_item['published_date'][:4],
                'average_rating': book_item.get('average_rating'),
                'ratings_count': book_item.get('ratings_count'),
                'thumbnail': book_item['thumbnail']
            }
        books_matching = Book.objects.filter(title=book['title'], published_date=book['published_date'])
        book_instance = None
        if books_matching.count() > 0:
            book_instance = Book.objects.get(title=book['title'], published_date=book['published_date'])
            book_instance.average_rating = book['average_rating']
            book_instance.ratings_count = book['ratings_count']
            book_instance.thumbnail = book['thumbnail']
        else:
            book_instance = Book.objects.create(title=book['title'], published_date=book['published_date'],
                                average_rating=book['average_rating'], ratings_count=book['ratings_count'],
                                thumbnail=['thumbnail'])

        for k in range(len(book_item['authors'])):
            if external_data:
                author, author_created = Author.objects.update_or_create(name=book_item['authors'][k])
            else:
                author, author_created = Author.objects.update_or_create(pk=book_item['authors'][k])
            book_instance.authors.add(author)

        if book_item.get('categories') is not None:
            for j in range(len(book_item['categories'])):
                if external_data:
                    category, category_created = Category.objects.update_or_create(name=book_item['categories'][j])
                else:
                    category, category_created = Category.objects.update_or_create(pk=book_item['authors'][k])
                book_instance.categories.add(category)

        book_instance.save()

