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
