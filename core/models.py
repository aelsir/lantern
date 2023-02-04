from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Published Manager to return only published fields
class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)
        

# Create your models here.
class Post(models.Model):
    
    # Status of the posts
    class Status(models.TextChoices):
        DRAFT = 'DF', 'مسودة'
        PUBLISHED = 'PB', 'منشور'

    
    title = models.CharField(max_length=250)
    title_arabic = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    # define the managers
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title
    
    # get the absolute url so I don't have to refer to it each time in the frontend
    def get_absolute_url(self):
        return reverse("core:detail", args=[self.publish.year,
                                            self.publish.month,
                                            self.publish.day,
                                            self.slug])
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
          ordering = ['created']
          indexes = [
               models.Index(fields=['created'])
          ]
    
    def __str__(self):
        return f"تعليق بواسطة {self.name} على {self.post}"
    
