from django.db import models


# Create your models here.
class Chismis(models.Model):
    chismis = models.CharField(max_length=255)
    chismis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chismis
