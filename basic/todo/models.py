from django.db import models
from django.urls import reverse
# Create your models here.
class todo_list(models.Model):
	image=models.FileField()
	name=models.CharField(max_length=30)
	def get_absolute_url(self):
		return reverse('todo:index')
