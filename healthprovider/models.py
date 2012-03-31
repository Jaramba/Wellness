from django.db import models

class HealthProvider(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		pass
