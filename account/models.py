from django.db import models
from django.contrib.auth.models import User


class user_extend(models.Model):
	user_name=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
	latitde=models.DecimalField(max_digits=19, decimal_places=10)
	longitude=models.DecimalField(max_digits=19, decimal_places=10)

	def publish(self):
		self.latitde = timezone.now()
		self.save()


# Create your models here.
