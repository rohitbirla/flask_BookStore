from Bookstore import app,db
from flask import render_template,redirect,render_template,url_for
from Bookstore.forms import AddForm,BuyForm
from Bookstore.models import Book
import os

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
    
        name = form.name.data
        author=form.author.data

        
        new_book = Book(name,author)

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('add.html',form=form)

@app.route('/list')
def list():
    
    books = Book.query.all()
    return render_template('list.html', books=books)

@app.route('/buy', methods=['GET', 'POST'])
def buy():

    form = BuyForm()

    if form.validate_on_submit():
        id = form.id.data
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()

        return redirect(url_for('list'))
    return render_template('buy.html',form=form)

if __name__=='__main__':
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)