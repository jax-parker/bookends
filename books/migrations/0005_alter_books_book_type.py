# Generated by Django 3.2.20 on 2023-07-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_auto_20230727_0916"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="book_type",
            field=models.CharField(
                choices=[
                    ("mystery", "Mystery"),
                    ("thriller", "Thriller"),
                    ("horror", "Horror"),
                    ("historical", "Historical"),
                    ("romance", "Romance"),
                    ("dystopian", "Distopian"),
                    ("fantasy", "Fantasy"),
                    ("science-fiction", "Science Fiction"),
                    ("action-adventure", "Action/Adventure"),
                    ("thriller", "Thriller"),
                    ("lgbtq+", "LGBTQ+"),
                    ("childrens", "Childrens"),
                    ("biography", "Biograppy"),
                    ("self-help", "Self-Help"),
                    ("travel", "Travel"),
                    ("comedy", "Comedy"),
                ],
                default="mystery",
                max_length=50,
            ),
        ),
    ]
