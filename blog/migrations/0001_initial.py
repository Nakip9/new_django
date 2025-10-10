from django.db import migrations, models


class Migration(migrations.Migration):
    """Initial database schema for the blog Post model."""

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(unique=True)),
                ("body", models.TextField()),
                ("published_at", models.DateTimeField()),
            ],
            options={"ordering": ["-published_at"]},
        ),
    ]
