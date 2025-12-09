from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database (SQLite)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Book ID
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=True)

# Create database
with app.app_context():
    db.create_all()

# Show books + Add book
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']

        new_book = Book(title=title, author=author, year=int(year) if year else None)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('index'))

    books = Book.query.all()
    return render_template('index.html', books=books)

# Edit book
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        year = request.form['year']
        book.year = int(year) if year else None

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', book=book)

# Delete book
@app.route('/delete/<int:book_id>', methods=['POST'])
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
