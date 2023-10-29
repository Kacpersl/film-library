from django.db import models

# Create your models here.

class Writer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return (f'{self.first_name} {self.last_name}')


class Film(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Writer, on_delete=models.CASCADE)
    release_date = models.DateField()
    cove = models.ImageField(upload_to='covers', null=True, blank=True)

    def __str__(self):
        return self.title

