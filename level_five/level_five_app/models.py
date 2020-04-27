from django.db import models
from django.contrib.auth.models import User

class userinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_image = models.ImageField(upload_to='profile_pics',blank=True)


    def __str__(self):
        return self.user.username


# Create your models here.
