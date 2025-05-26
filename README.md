# Social Network Platform

A full-featured social media web application built with Django that enables users to connect, share content, and interact with each other's posts.
and here is the demo: https://network-twitter-yaya.onrender.com/

---

## Features

- User registration, login, and logout
- Create, edit, and delete posts
- Like and unlike posts (with real-time updates)
- Follow and unfollow other users
- View your own profile and others' profiles
- See posts from people you follow on the "Following" page
- Responsive Bootstrap 5 design

---

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** Django Templates, Bootstrap 5, Font Awesome
- **Database:** SQLite (default, can use PostgreSQL)
- **Async:** JavaScript Fetch API for like/unlike actions
- **Static Files:** Whitenoise for production
- **Deployment:** Render.com

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sozjamil/Network-Twitter.git
cd your-repo
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file or set the following in your environment:

```
DJANGO_SECRET_KEY=your-secret-key
DEBUG=True
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Collect static files (for production)

```bash
python manage.py collectstatic
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## Deployment (Render.com)

1. Push your code to GitHub.
2. Create a new Web Service on [Render.com](https://render.com/).
3. Set the build command:
   ```
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```
4. Set the start command:
   ```
   gunicorn project4.wsgi
   ```
   *(Replace `project4` with your Django project folder name if different)*
5. Add environment variables (`DJANGO_SECRET_KEY`, etc.) in the Render dashboard.
6. Deploy!

---

## Project Structure

```
project4/
├── manage.py
├── network/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   └── static/
├── project4/
│   ├── settings.py
│   └── wsgi.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

## License

This project is for educational purposes (Harvard CS50W Project 4).  
Feel free to use and modify for your own learning!

---
