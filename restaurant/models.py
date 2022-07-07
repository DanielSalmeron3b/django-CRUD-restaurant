from django.db import models

# Create your models here.

class Dish(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='images/', verbose_name='Image' , null=True)
    description = models.TextField(verbose_name='Description', null=True)

    # Show some data about the dish in the admin interface
    def __str__(self):
        row = 'Title: ' + self.title +  " - " + "Description: " + self.description
        return row

    # If a dish is deleted, delete the image also
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()