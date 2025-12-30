# 📚 Book Management System (Flask + SQLite)

A simple and clean **CRUD web application** built using **Flask** and
**SQLite**.\
This project allows users to **add, edit, view, and delete** books
through a minimal and responsive web interface.

------------------------------------------------------------------------

## 🚀 Features

-   ✔ Add new books (Title, Author, Year)\
-   ✔ View all stored books in a clean table\
-   ✔ Edit any book details\
-   ✔ Delete books with confirmation\
-   ✔ SQLite for lightweight persistent storage\
-   ✔ Flask + SQLAlchemy ORM\
-   ✔ Simple and fully responsive UI

------------------------------------------------------------------------

## 🖥️ Tech Stack

  Component    Technology
  ------------ ----------------
  Backend      Flask (Python)
  Database     SQLite
  ORM          SQLAlchemy
  Templating   Jinja2
  Frontend     HTML + CSS

------------------------------------------------------------------------

## 📂 Project Structure

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

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/<your-username>/book_management_system_project.git
cd book_management_system_project
```

### 2️⃣ Create & activate a virtual environment (recommended)

``` bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

### 3️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

``` bash
python app.py
```

Your app will be live at:\
👉 **http://127.0.0.1:5000**

------------------------------------------------------------------------

## 📝 How It Works

-   The homepage (`/`) displays all books from the SQLite database.
-   A form at the bottom lets users **add a new book**.
-   Each book entry includes:
    -   **Edit** → update book details\
    -   **Delete** → remove book with confirmation\
-   The database file **`books.db`** is automatically created on first
    run.

------------------------------------------------------------------------

## 🛠 Requirements

    Flask==3.1.2
    Flask-SQLAlchemy==3.1.1
    SQLAlchemy==2.0.44
    Jinja2==3.1.6
    Werkzeug==3.1.4

------------------------------------------------------------------------

## 🤝 Contributing

Pull requests are welcome!\
You may improve:

-   UI/UX\
-   Add a search bar\
-   Add sorting/filtering\
-   Add login authentication

------------------------------------------------------------------------

## ⭐ Support This Project

If this project helped you, consider giving it a **⭐ on GitHub**!
