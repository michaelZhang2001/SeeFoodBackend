from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to="profile_pics")

	def __str__(self):
		return f'{self.user.username} Profile' 

	def save(self, *args, **kwargs):			#this is probably not the best way to save the image due to some efficiency deficiencies, but it demonstrates how to override the save method
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)
		if img.height>300 or img.width>300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)