from django.db import models

# Create your models here.

class Website(models.Model):
    name = models.CharField(max_length=256)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)