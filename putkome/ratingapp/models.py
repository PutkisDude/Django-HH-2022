from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tvseries.models import Episode

class Rating(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE
	)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	episode = models.ForeignKey(
		Episode,
		on_delete=models.CASCADE,
		related_name="episode_rating"
	)
	rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
	
	def __str__(self):
		return f"{self.episode}: Rating {self.rating} / 5"


	def get_absolute_url(self):
		return reverse('rating', kwargs={'pk' : self.pk})

## Crash with saving
#	class Meta:
#		unique_together = [['user', 'episode']]
