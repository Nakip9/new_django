from django.shortcuts import render

from .models import Post


def post_list(request):
    """Return the list of blog posts to the template."""

    # Query all posts (ordered by the model's Meta.ordering) to show on the homepage.
    posts = Post.objects.all()
    # Hand the post queryset to the template so it can loop over and display them.
    return render(request, "blog/post_list.html", {"posts": posts})
