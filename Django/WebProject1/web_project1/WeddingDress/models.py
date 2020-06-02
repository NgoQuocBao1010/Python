from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class WeddingDress(models.Model):
	name = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	image = models.ImageField(default='default.jbg', upload_to='sample_pics')
	salesprice = models.IntegerField()
	rental_price = models.IntegerField()
	sizeS = models.BooleanField(default=True)
	sizeM = models.BooleanField(default=True)
	sizeL = models.BooleanField(default=True)
	sizeXL = models.BooleanField(default=True)
	admin = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


	def save(self):
		super().save()

		img = Image.open(self.image.path)
		output_size = (800, 800)
		img.thumbnail(output_size)
		img.save(self.image.path)

