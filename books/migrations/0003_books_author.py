# Generated by Django 3.2.20 on 2023-07-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_remove_books_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="books",
            name="author",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
