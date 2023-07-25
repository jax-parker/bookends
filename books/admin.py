from django.contrib import admin
from .models import Books
# Register your models here.


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "book_type",
        "description",
        "comments",
        "image",
    )
    list_filter = ("book_type",)
