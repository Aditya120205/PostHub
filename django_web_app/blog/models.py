from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import os

class Post(models.Model):
	title = models.CharField(max_length=100)
	file = models.FileField(null=True,blank=True,upload_to='Files')
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension

	def download_url(self):
		# Cloudinary URLs live on a different origin than the site, so the
		# HTML `download` attribute is ignored by browsers (it only works
		# same-origin). Adding the fl_attachment flag tells Cloudinary's
		# CDN to send the file back with a Content-Disposition: attachment
		# header, which forces an actual download instead of opening the
		# file in the browser.
		url = self.file.url
		if '/upload/' in url and 'fl_attachment' not in url:
			url = url.replace('/upload/', '/upload/fl_attachment/', 1)
		return url

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})