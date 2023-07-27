# Generated by Django 3.2.20 on 2023-07-27 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=300)),
                ('post', djrichtextfield.models.RichTextField(max_length=10000)),
                ('posted_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'forum',
                'verbose_name_plural': 'forum',
                'ordering': ['-posted_date'],
            },
        ),
    ]
