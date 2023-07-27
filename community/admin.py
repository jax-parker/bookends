from django.contrib import admin
from .models import Forum


# Register your models here.

@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "post",
     )
    list_filter = ("subject",)
