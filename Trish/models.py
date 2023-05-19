from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length = 255)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        # return reverse('article_view', args = (str(self.id)))
        return reverse('home')

    def success_url(self):
        return reverse_lazy('home')

class Post(models.Model):
    title = models.CharField(max_length = 255)
    header_image = models.ImageField(null = True, blank = True, upload_to = "images/")
    title_tag = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = RichTextField(blank = True, null = True)
    # body = models.TextField()
    post_date = models.DateField(auto_now_add = True)
    category = models.CharField(max_length = 255)
    snippet = models.CharField(max_length = 255)
    likes = models.ManyToManyField(User, related_name = 'blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        # return reverse('article_view', args = (str(self.id)))
        return reverse('home')

    def success_url(self):
        return reverse_lazy('home')