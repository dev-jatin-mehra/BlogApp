# Flask Blog App

A simple blog application built with Flask, SQLite, and SQLAlchemy as the ORM. It supports user authentication using PyJWT and utilizes Jinja templating for dynamic HTML rendering.

## Features
- Create, edit, and delete blog posts
- Update account: name_change , account_image, email, password, etc.
- User authentication (JWT-based)
- Error handling and structured routes
- SQLite database with SQLAlchemy ORM
- Templating with Jinja, HTML, and CSS

## Installation

### Clone the repository:
```bash
git clone https://github.com/yourusername/BlogApp-Python.git
cd BlogApp-Python
```

### Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Set up environment variables:
Create a `.env` file in the root directory and add the following:
```env
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
EMAIL=your_email
PASS=your_password
```
> **Note:** Refer to dotenv tutorials if needed.

## Database Initialization

1. Open the terminal and enter Python/Flask shell:
   ```bash
   python
   ```
2. Run the following commands:
   ```python
   from app import db
   db.create_all()
   ```

## Running the Application
To start the Flask app, run:
```bash
python run.py
```
Then, visit `http://127.0.0.1:5000` in your browser.

## Folder Structure
```
BlogApp-Python/
│── app/
│   ├── errors/      # Error handling module
│   ├── main/        # Main routes
│   ├── post/        # Blog post-related functionality
│   ├── static/      # CSS, JavaScript, and other static files
│   ├── templates/   # Jinja2 HTML templates
│   ├── test/        # Test scripts
│   ├── users/       # User authentication and management
│   ├── __init__.py  # App initialization
│   ├── config.py    # App configuration
│   ├── models.py    # Database models
│── instance/
│   ├── site.db      # SQLite database
│── .gitignore       # Ignore unnecessary files
│── README.md        # Project documentation
│── requirements.txt
│── run.py           # Main entry point
```

## Documentation
Refer to this documentation for more info: [Flask Documentation](https://flask.palletsprojects.com/en/stable/)

