from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from django.utils.text import slugify

BOOK_TYPES = (
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
    ("biography", "Biography"),
    ("self-help", "Self-Help"),
    ("travel", "Travel"),
    ("comedy", "Comedy"),
)


class Books(models.Model):
    """Model to create and manage books"""

    user = models.ForeignKey(User, related_name="book_owner",
                                                on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    author = models.CharField(max_length=300, null=True, blank=True)
    description = models.CharField(max_length=500, null=False, blank=False)
    comments = RichTextField(max_length=10000, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="books/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    book_type = models.CharField(max_length=50,
                                 choices=BOOK_TYPES, default="mystery")
    posted_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
            super(Books, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-posted_date"]
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return str(self.title)
