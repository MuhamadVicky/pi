from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CATEGORY_CHOICES = [
    ['Fiksi', 'Fiksi'],
    ['Berita', 'Berita'],
    ['Olahraga', 'Olahraga'],
    ['Teknologi', 'Teknologi'],
]


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published = models.BooleanField()
    created_date = models.DateTimeField()
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()

        if self.published and not self.published_date:
            self.published_date = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title + ' ' + self.author.username
