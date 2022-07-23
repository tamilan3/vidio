from django.db import models
# Create your models here.
class vidiouploader(models.Model):
    name =models.CharField(max_length=50)
    vidio=models.FileField(upload_to="vidio")

    def __str__(self):
        return self.name
