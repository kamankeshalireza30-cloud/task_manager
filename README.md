# 📋 Django Task Manager - Full Stack Application

A modern, responsive task management application built with Django and Tailwind CSS.

## ✨ Features

- **Full CRUD Operations**: Create, Read, Update, and Delete tasks
- **Real-time Toggle**: Mark tasks as complete/incomplete without page reload (AJAX)
- **Beautiful UI**: Modern, minimalist design with Tailwind CSS
- **Statistics Dashboard**: Track your progress with completion metrics
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Empty State Handling**: Helpful UI when no tasks exist
- **Progress Tracking**: Visual progress bar and task counters

## 🛠️ Technology Stack

- **Backend**: Django 4.2+ (Python)
- **Frontend**: Tailwind CSS (via CDN)
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Icons**: Font Awesome 6.4.0

## 📁 Project Structure

```
task_manager/
├── manage.py
├── task_manager/              # Main project directory
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── tasks/                     # Tasks app directory
    ├── __init__.py
    ├── admin.py              # Admin interface configuration
    ├── apps.py               # App configuration
    ├── models.py             # Task model definition
    ├── views.py              # Class-based views
    ├── urls.py               # URL routing
    ├── migrations/
    │   └── __init__.py
    └── templates/
        ├── base.html         # Base template
        └── tasks/
            ├── task_list.html          # Main task list view
            ├── task_form.html          # Create/Edit form
            └── task_confirm_delete.html # Delete confirmation
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Create Project Structure

```bash
# Create main project directory
mkdir task_manager
cd task_manager

# Create Django project
django-admin startproject task_manager .

# Create tasks app
python manage.py startapp tasks
```

### Step 2: Install Django

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Django
pip install django
```

### Step 3: Copy Application Files

Copy the provided files to their respective locations:

1. **Copy to `tasks/` directory**:
   - `models.py`
   - `views.py`
   - `urls.py`
   - `admin.py`
   - `apps.py`

2. **Create template structure**:
   ```bash
   mkdir -p tasks/templates/tasks
   ```

3. **Copy templates**:
   - `base.html` → `tasks/templates/`
   - `task_list.html` → `tasks/templates/tasks/`
   - `task_form.html` → `tasks/templates/tasks/`
   - `task_confirm_delete.html` → `tasks/templates/tasks/`

### Step 4: Configure Settings

Edit `task_manager/settings.py`:

```python
# Add 'tasks' to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',  # Add this line
]

# Template configuration (ensure this exists)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,  # This should be True
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Step 5: Configure Main URLs

Edit `task_manager/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Include tasks URLs
]
```

### Step 6: Run Migrations

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

### Step 7: Create Superuser (Optional)

```bash
# Create admin user to access /admin
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### Step 8: Run Development Server

```bash
# Start the Django development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to see the application!

## 📝 Usage Guide

### Creating a Task

1. Click the "New Task" button in the navigation
2. Enter a task title (required)
3. Optionally add a description
4. Click "Create Task"

### Viewing Tasks

- The home page displays all tasks in a card layout
- View statistics at the top showing total, completed, and pending tasks
- See a progress bar showing your completion percentage

### Updating a Task

1. Click the "Edit" button on any task card
2. Modify the title, description, or completion status
3. Click "Update Task"

### Completing a Task

- Simply click the checkbox on any task card
- The task will be marked as complete instantly (via AJAX)
- The page will refresh to update statistics

### Deleting a Task

1. Click the "Delete" button on any task card
2. Confirm deletion on the confirmation page
3. Task will be permanently removed

## 🎨 Customization

### Changing Colors

Edit `base.html` and modify the Tailwind config:

```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: {
                    50: '#eef2ff',   // Light shade
                    500: '#6366f1',  // Main color
                    700: '#4338ca',  // Dark shade
                }
            }
        }
    }
}
```

### Adding More Fields

1. Edit `models.py` to add fields
2. Run migrations: `python manage.py makemigrations && python manage.py migrate`
3. Update forms in `views.py`
4. Update templates to display new fields

## 🔒 Security Notes

- CSRF protection is enabled by default
- Always use `{% csrf_token %}` in forms
- The AJAX toggle function includes CSRF token handling
- Never commit `SECRET_KEY` to version control

## 🐛 Troubleshooting

### Templates Not Found
- Ensure `APP_DIRS` is `True` in `settings.py`
- Verify template files are in `tasks/templates/tasks/`

### Static Files Not Loading
- Tailwind CSS is loaded via CDN, no static files needed
- Ensure internet connection for CDN resources

### Database Errors
- Run `python manage.py migrate` to apply migrations
- Delete `db.sqlite3` and run migrations again if needed

## 📦 Production Deployment

For production deployment:

1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Use PostgreSQL or MySQL instead of SQLite
4. Set up static file serving (collectstatic)
5. Use a production WSGI server (Gunicorn, uWSGI)
6. Configure HTTPS and secure cookies

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project as a learning resource or starting point for your own applications.

## 📧 Support

For issues or questions, please create an issue in the repository.

---

**Built with ❤️ using Django and Tailwind CSS**
