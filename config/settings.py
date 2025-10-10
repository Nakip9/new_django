"""Django settings for the educational blog project.

Each section includes a short note about why it matters when building a blog.
"""

from pathlib import Path

# Step 1: Calculate the base directory so the rest of the settings can find files.
BASE_DIR = Path(__file__).resolve().parent.parent

# Step 2: Set debugging options and security placeholders.
SECRET_KEY = "development-secret-key"
DEBUG = True
ALLOWED_HOSTS: list[str] = []

# Step 3: Register Django's core apps along with our custom "blog" app.
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",
]

# Step 4: Enable the middleware that powers sessions, messages, and security.
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Step 5: Point Django at the root URL configuration module.
ROOT_URLCONF = "config.urls"

# Step 6: Configure template discovery so Django finds ``templates/`` and app templates.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# Step 7: Allow Django to serve the project via WSGI-compatible servers.
WSGI_APPLICATION = "config.wsgi.application"

# Step 8: Use SQLite for a lightweight development database.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Step 9: Localisation defaults.
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Step 10: Static file configuration for CSS/JS/images.
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
