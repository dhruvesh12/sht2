from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserVote(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE)

	voter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_vote')

	vote = models.BooleanField(default=False)



	class Meta:

		unique_together = (('user', 'voter'))
