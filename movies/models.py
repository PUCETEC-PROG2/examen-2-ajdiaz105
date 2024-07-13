from django.db import models

# Create your models here.

class Movie(models.Model):
    title=models.CharField(max_length=100,null=False)
    generous=models.CharField(max_length=100,null=False)
    name = models.CharField(max_length=30,null=False)
    year = models.IntegerField(null=False,default=1)
    synopsis = models.TextField(max_length=330,null=False)

    def __str__(self) -> str:
        return self.name