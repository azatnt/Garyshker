from django.db import models
from django.contrib.auth.models import User






class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user-profile-image', blank=True, default='garysh.jpg')
    city = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=120, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    investment = models.IntegerField(null=True)
    comments = models.TextField(null=True, blank=True)
    # total_investment = models.DecimalField(default=0, max_digits=99999, decimal_places=0)
    




    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)



