from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to='category/')
    numeration = models.IntegerField(blank=True)

    def __str__(self):
        return self.title
