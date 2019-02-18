from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class category(models.Model):
	title=models.CharField(max_length=255,null=True)
	


	def publish(self):
		self.title = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class infy(models.Model):
	first=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True)
	category=models.ForeignKey(category, on_delete=models.CASCADE,null=True)
	name = models.CharField(max_length=200,null=True)
	middle=models.CharField(max_length=200)
	img = models.ImageField(upload_to='', default='no-photo.png')
	last=models.CharField(max_length=200)
	
	


	def publish(self):
		self.name = timezone.now()
		self.save()

	def __str__(self):
		return self.name

class userImage(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	img = models.ImageField(upload_to='user-img', default='no-photo.png')












# Create your models here.
