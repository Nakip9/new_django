# Educational Django Blog

This project demonstrates the essential steps for building a basic blog with Django. Each file contains inline comments so you can follow the build from configuring settings through rendering posts on the homepage.

## Getting Started

1. **Install dependencies**
   ```bash
   pip install django
   ```
2. **Apply migrations** – creates the `Post` table.
   ```bash
   python manage.py migrate
   ```
3. **Create a superuser** – lets you log into the admin and add posts.
   ```bash
   python manage.py createsuperuser
   ```
4. **Run the development server**
   ```bash
   python manage.py runserver
   ```
5. **Add posts** via http://127.0.0.1:8000/admin/ and then view them on the homepage.

Because the environment used to generate this project does not ship with Django, the automated checks may show import errors until you install the package locally.
