from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# -------------------------
# Database Configuration
# -------------------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SQLite (local + Render compatible)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'books.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# -------------------------
# Book Model
# -------------------------
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=True)


# Create database if not exists
with app.app_context():
    db.create_all()


# -------------------------
# Home + Add Book
# -------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')

        # Safe conversion for empty year input
        year_value = int(year) if year and year.isdigit() else None

        new_book = Book(title=title, author=author, year=year_value)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('index'))

    # Show newest books first (optional improvement)
    books = Book.query.order_by(Book.id.desc()).all()
    return render_template('index.html', books=books)


# -------------------------
# Edit Book
# -------------------------
@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        book.title = request.form.get('title')
        book.author = request.form.get('author')

        year = request.form.get('year')
        book.year = int(year) if year and year.isdigit() else None

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', book=book)


# -------------------------
# Delete Book
# -------------------------
@app.route('/delete/<int:book_id>', methods=['POST'])
def delete(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('index'))


# -------------------------
# Entry Point
# -------------------------
if __name__ == '__main__':
    # Debug only for local running
    app.run(debug=True)
