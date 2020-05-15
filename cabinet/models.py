from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
	about_me = models.CharField(max_length=100, blank=True)
	status = models.CharField(max_length=50, blank=True)
	image = models.ImageField(upload_to="images/", default="images/black.jpg")
	is_on = models.BooleanField(default=True)
	location = models.CharField(default="Neverland", max_length=20)
	birth_date = models.DateField(default=timezone.now)
	#Из-за абстрактой модели пришлось сделать ещё побочную Person

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'


class Post(models.Model):
	text = models.TextField()
	author_name = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'