from django.db import models

# Create your models here.

class Quant(models.Model):
	name = models.CharField(max_length=80, null=False, blank=True);
	time_added = models.DateTimeField(auto_now_add=True, auto_now=False);
	time_started = models.DateTimeField(null=True);
	time_finished = models.DateTimeField(null=True);
	
	def __unicode__(self):
		return self.name