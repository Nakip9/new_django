from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    # The home page lists all posts, making it easy to extend with detail pages later.
    path("", views.post_list, name="post_list"),
]
