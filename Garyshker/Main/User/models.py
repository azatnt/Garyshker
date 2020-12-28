from django.db import models
from django.contrib.auth.models import User






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.FileField(upload_to='profile', blank=True, default='garysh.jpg', verbose_name=" ")
    city = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    # investment = models.IntegerField(null=True)
    comments = models.TextField(null=True, blank=True)
    # total_investment = models.DecimalField(default=0, max_digits=90, decimal_places=1)





    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
