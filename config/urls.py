"""Route HTTP requests to views for the educational blog."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Step 11: Add the Django admin so you can manage blog posts via the browser.
    path("admin/", admin.site.urls),
    # Step 12: Delegate root URL handling to the blog app's URL configuration.
    path("", include("blog.urls")),
]
