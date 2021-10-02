from Bookstore.models import Book
from Bookstore import db


def test_Book():
    newname = Book('dog','kris')

    db.session.add(newname)
    db.session.commit()

    books = Book.query.all()
    for book in books:
        print(book)



    assert (1==1)