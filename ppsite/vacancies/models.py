from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Vacancies(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE,
                               related_name='blog_posts')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    
    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()\
                .filter(status=Vacancies.Status.PUBLISHED)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.name
    