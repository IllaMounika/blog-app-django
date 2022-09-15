from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Library(models.Model):
    booktitle=models.CharField(max_length=250)
    #bookid=models.IntegerField()
    #is_available=models.BooleanField()

    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.booktitle