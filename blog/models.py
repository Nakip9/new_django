from django.db import models


class Post(models.Model):
    """A simple blog post with enough fields to mimic a real-world example."""

    # A descriptive title shown in lists and as the page heading.
    title = models.CharField(max_length=200)
    # A slug is a URL-friendly identifier automatically generated from the title.
    slug = models.SlugField(unique=True)
    # The main article content.
    body = models.TextField()
    # Track when the post was published so we can order posts by recency.
    published_at = models.DateTimeField()

    class Meta:
        ordering = ["-published_at"]

    def __str__(self) -> str:
        return self.title
