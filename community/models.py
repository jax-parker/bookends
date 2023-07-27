from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django.utils.text import slugify

class Forum(models.Model):
    """Model to create and manage forum posts """

    user = models.ForeignKey(User, related_name="post_owner", on_delete=models.CASCADE)
    subject = models.CharField(max_length=300, null=False, blank=False)
    post = RichTextField(max_length=10000, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.subject:
            self.slug = slugify(self.subject)
            super(Forum, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-posted_date"]
        verbose_name = 'forum'
        verbose_name_plural = 'forum'

    def __str__(self):
        return str(self.subject)
