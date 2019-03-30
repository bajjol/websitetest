from django.db import models
from django.utils import timezone
from django.forms import ModelForm

# Create your models here.
class Post(models.Model):
	judul = models.CharField(max_length=200)
	text = models.TextField(null=True)
	clip = models.FileField(upload_to='video/', null=True)
	created_date = models.DateTimeField(default=timezone.now)
	def __unicode__(self):
		return self.judul

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
