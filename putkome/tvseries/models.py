from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

from django.db.models import FloatField
from django.db.models.functions import Cast

class Serie(models.Model):
	name = models.CharField(max_length=300, unique=True)
	description = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
    
	def __str__(self):
		return f"{self.name}"
		
	def get_absolute_url(self):
		return reverse('serie_detail', kwargs={"pk": self.pk})

	def get_rating_url(self):
		return reverse('rating', kwargs={"pk": self.pk})

	def get_all_seasons(self):
		return self.serie_seasons.all()
	
	class Meta:
		ordering = ['name']
		verbose_name = "TV Serie"
		verbose_name_plural = "Tv Series"

class Season(models.Model):
	serie = models.ForeignKey(
		Serie,
		on_delete=models.CASCADE,
		related_name="serie_seasons"
	)	
	season_number = models.IntegerField(
		validators=[
			MaxValueValidator(100),
            MinValueValidator(1)
        ])
	
	def __str__(self):
		return f"{self.serie} - s{self.season_number}"

	def get_all_episodes(self):
		return self.season_episodes.all()

	def get_absolute_url(self):
		return reverse('season_detail', kwargs={"pk": self.pk})

		
	class Meta:
		unique_together = [['serie', 'season_number']]

class Episode(models.Model):
	episode_number = models.IntegerField(
		validators=[
			MaxValueValidator(100),
            MinValueValidator(1)
        ])
	season = models.ForeignKey(
		Season,
		on_delete=models.CASCADE,
		related_name="season_episodes")
		
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.season} ep{self.episode_number}"

	def get_absolute_url(self):
		return reverse('rating', kwargs={"pk": self.pk})

	def get_average_rating(self):
		return self.episode_rating.all().aggregate(Avg('rating'))['rating__avg']

	class Meta:
		unique_together = [['episode_number', 'season']]
