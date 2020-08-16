from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    f_name = models.CharField(max_length=20, blank=False)
    l_name = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=40, blank=False)
    phone = models.CharField(max_length=10, blank=False)
    address = models.TextField(blank=False)

    def __str__(self):
        return f'{self.user.username} - Profile'
    # python manage.py migrate --run-syncdb

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	image = models.ImageField(default='default.png', upload_to='profile_pics')
# 	is_restaurant = models.BooleanField(default=False)
# 	is_customer = models.BooleanField(default=False)

# 	def __str__(self):
# 		return f'{self.user.username} Profile'

# 	def save(self, *args, **kwargs):
# 		super().save(*args, **kwargs)

# 		img = Image.open(self.image.path)

# 		if img.height > 300 or img.width > 300:
# 			output_size = (300, 300)
# 			img.thumbnail(output_size)
# 			img.save(self.image.path)
