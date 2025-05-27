# ToDo List with Authentication and Tailwind CSS

This is a Django-based ToDo list application featuring user authentication, task management, and a Tailwind CSS–styled frontend. It includes a Chart.js pie chart to visualize task status distribution.

## Features

* **User Authentication**: Sign up, log in, and log out functionality using Django's built-in auth system.
* **Task CRUD**: Create, read, update, and delete tasks.
* **Task Statuses**: Tasks can be pending, in progress, or completed.
* **Visual Dashboard**: A pie chart (Chart.js) showing the number of tasks per status.
* **Tailwind CSS**: Utility‑first styling for a modern, responsive UI.
* **Secure**: CSRF protection, `@login_required` decorators, and permission checks using `get_object_or_404`.

## Prerequisites

* Python 3.8+
* Node.js & npm (for Tailwind CSS)
* PostgreSQL (or SQLite for development)
* Git

## Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd todo_list_with_auth
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   * Create a `.env` file at the project root:

     ```dotenv
     SECRET_KEY=your_django_secret_key
     DEBUG=True
     DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/DB_NAME
     NPM_BIN_PATH=C:\Program Files\nodejs\npm.cmd
     ```

## Database Setup

* **PostgreSQL**: Ensure your `DATABASE_URL` points to a running PostgreSQL instance.
* **SQLite**: For quick development, you can switch to SQLite in `settings.py`:

  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }
  ```

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**

   ```bash
   python manage.py createsuperuser
   ```

## Tailwind CSS Integration

1. **Install Tailwind dependencies**

   ```bash
   python manage.py tailwind install
   ```

2. **Start the Tailwind watcher**

   ```bash
   python manage.py tailwind start
   ```

3. **Include Tailwind CSS** in `base.html` (already configured):

   ```django
   {% load tailwind_tags %}
   <head>
     {% tailwind_css %}
   </head>
   ```

4. **Build for production**

   ```bash
   python manage.py tailwind build
   ```

## Running the Application

1. **Start the Django development server**

   ```bash
   python manage.py runserver
   ```

2. **Access the app**
   Open your browser and navigate to `http://127.0.0.1:8000/tasks/`.

## Deployment

* Use `python manage.py tailwind build` to generate production CSS.
* Run `python manage.py collectstatic` to gather static files.
* Configure Gunicorn (or another WSGI server) and a reverse proxy (Nginx).
* Set `DEBUG=False` and ensure environment variables are set securely.

## Repository Structure

```
├── manage.py
├── requirements.txt
├── todo_list_with_auth/        # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tasks/                      # Django app for tasks
│   ├── migrations/
│   ├── templates/tasks/
│   ├── static/tasks/js/
│   └── ...
├── theme/                      # django-tailwind app
│   ├── static_src/
│   ├── tailwind.config.js
│   └── ...
└── README.md                   # This file
```

## License

This project is licensed under the MIT License.

---

Happy coding! 🚀
