# Django Quora Clone

A simple Quora-like Q&A platform built with Django. This application allows users to register, ask questions, answer others' questions, and like answers.

## Features

- **User Authentication**
  - Register with username, email, and password
  - Login/logout functionality
  - User profiles

- **Question Management**
  - Post questions with title and detailed content
  - View questions posted by all users
  - Detailed question view

- **Answer System**
  - Post answers to questions
  - View answers from other users
  - Like/unlike answers

## Project Structure

```
quora_clone/
├── manage.py
├── requirements.txt
├── quora_clone/          # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── qa_app/               # Main application
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations/
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── templates/        # HTML templates
    │   └── qa_app/  
    │       ├── base.html
    │       ├── login.html
    │       ├── register.html
    │       ├── home.html
    │       ├── ask_question.html
    │       ├── question_detail.html
    │       ├── profile.html
    │       └── logout.html
    
```

## Installation & Setup

1. **Clone this repository**
   ```bash
   git clone <repository-url>
   cd quora_clone
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the site in your browser at http://127.0.0.1:8000/**

## Models

- **Question**: Stores question data with title, content, author, and creation date
- **Answer**: Stores answers with content, author, related question, likes, and creation date

## Usage

1. Register a new account
2. Browse questions on the home page
3. Click on a question to view details and answers
4. Post your own questions using the "Ask Question" button
5. Answer questions on the question detail page
6. Like helpful answers
7. View your profile to see your questions, answers, and likes

## Admin Interface

Access the admin interface at http://127.0.0.1:8000/admin/ using your superuser credentials. From here, you can:

- Manage users
- Create, edit, or delete questions
- Manage answers
- View and modify likes

## Notes for Developers

- Templates follow Django's app-based organization pattern with namespacing
- User authentication uses Django's built-in auth system
- Bootstrap is used for frontend styling
- Models implement proper relationships for the Q&A functionality

## Future Enhancements

- Add comment system for answers
- Implement question categories/tags
- Add user reputation system
- Support markdown in questions and answers
- Add search functionality
