from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)
    published_date = models.DateTimeField()
    author = models.CharField(max_length=50)
    email = models.EmailField()

    categories = models.ManyToManyField('category')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)
    text_color = models.CharField(max_length=100)
    background_color = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
