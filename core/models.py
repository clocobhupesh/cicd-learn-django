# from django.db import models  # pylint: disable=unused-variable
from django.db import models


# Create your models here.
class Apple(models.Model):
    name = models.CharField(
        max_length=100,
    )
    color = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return f"""{self.name}


            ({self.color})"""
