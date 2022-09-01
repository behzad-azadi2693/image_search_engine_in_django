from django.db import models

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return f'{self.id}-{self.name}'

    @property
    def image_name(self):
        return self.image.url