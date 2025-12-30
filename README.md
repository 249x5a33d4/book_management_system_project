📚 Book Management System (Flask + SQLite)

A simple and clean CRUD (Create, Read, Update, Delete) web application built using Flask and SQLite.
This project allows users to add, edit, view, and delete books through a minimal web interface.

🚀 Features

✔ Add new books (Title, Author, Year)

✔ View all stored books in a clean table

✔ Edit any book details

✔ Delete books with confirmation

✔ SQLite used for lightweight, persistent storage

✔ Flask + SQLAlchemy ORM

✔ Fully responsive, simple UI

🖥️ Tech Stack
Component	Technology
Backend	Flask (Python)
Database	SQLite
ORM	SQLAlchemy
Templating	Jinja2
Frontend	HTML + CSS
📂 Project Structure
book_management_system_project/
│
├── app.py
├── books.db
├── requirements.txt
├── hello.py
│
└── templates/
    ├── base.html
    ├── index.html
    └── edit.html

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/book_management_system_project.git
cd book_management_system_project

2. Create & activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python app.py


Your app will start at:
👉 http://127.0.0.1:5000

📝 How It Works

The homepage (/) displays all books.

A form at the bottom lets users add a new book.

Each book row includes:

Edit → updates the book

Delete → removes it from the database with confirmation

SQLite database (books.db) automatically gets created if not found.

📸 Screenshots (Optional)

Add screenshots here later if you want: UI, Add Book page, Edit Book page.

🛠 Requirements
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
SQLAlchemy==2.0.44
Jinja2==3.1.6
Werkzeug==3.1.4


Or simply use the included requirements.txt.

🤝 Contributing

Pull requests are welcome!
If you'd like to improve UI or add features (search books, sort table, login system), feel free to contribute.

⭐ Support This Project

If this project helped you, please consider giving it a ⭐ on GitHub!
