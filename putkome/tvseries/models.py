from django.db import models

class Serie(models.Model):
	name = models.CharField(max_length=300)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.name}"
	
	class Meta:
		ordering: ['name']
		verbose_name = "TV Serie"
		verbose_name_plural = "Tv Series"

class Season(models.Model):
	serie = models.ForeignKey(
		Serie,
		on_delete=models.CASCADE)
	season_number = models.CharField(max_length=300)
	
	def __str__(self):
		return f"{self.serie} - s{self.season_number}"

	class Meta:
		unique_together = [['serie', 'season_number']]

class Episode(models.Model):
	episode_number = models.IntegerField()
	season = models.ForeignKey(
		Season,
		on_delete=models.CASCADE)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.season} ep{self.episode_number}"

	class Meta:
		unique_together = [['episode_number', 'season']]
