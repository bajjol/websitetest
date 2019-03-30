from django.db import models

class Grupbarang(models.Model):
	#A topic the user is learning about"""
	text = models.CharField(max_length=200)
	def __str__(self):
		"""Return a string representation of the model."""
		return self.text

class Testmerch(models.Model):
	grupbarang = models.ForeignKey(Grupbarang, on_delete=models.CASCADE)
	namabarang = models.CharField(max_length=50)
	gambarbarang = models.FileField(upload_to='images/')
	deskripbarang = models.TextField()
	def __str__(self):
		return self.text
