from django.db import models
from django.contrib.auth.models import User

class Cars(models.Model):
    title = models.CharField(max_length=255)
    motor = models.DecimalField(max_digits=5, decimal_places=2, default=2.0)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title