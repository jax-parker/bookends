# Generated by Django 3.2.20 on 2023-07-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_books_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['-posted_date'], 'verbose_name': 'book', 'verbose_name_plural': 'books'},
        ),
        migrations.AddField(
            model_name='books',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
