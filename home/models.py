from django.db import models
from cabinet.models import User
import datetime
from django.utils import timezone
 

class Book(models.Model):
	title = models.CharField(max_length=30, blank=True)
	image = models.ImageField(upload_to="images/", default="images/black.jpg")
	author_name = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
	description = models.CharField(max_length=1000)
	price = models.IntegerField()
	views = models.IntegerField(default=0)
	pub_date = models.DateTimeField('Дата публикауции', default=timezone.now)
	status = models.CharField(max_length=30, default="В процессе")
	tags = models.ManyToManyField('Tag', blank=True, related_name='books')
	genres = models.ManyToManyField('Genre', blank=True, related_name='books')

	def __str__(self):
		return self.title

	def in_this_week(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	def in_this_month(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 30))

	def in_this_year(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 365))

	class Meta:
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'


class Tag(models.Model):    
	name = models.CharField(verbose_name='Название', max_length=60)     
	slug = models.SlugField(verbose_name='URL')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Тег'
		verbose_name_plural = 'Теги'


class Genre(models.Model):
	name = models.CharField(max_length=20)
	slug = models.SlugField(verbose_name='URL')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Жанр'
		verbose_name_plural = 'Жанры'

class Chapter(models.Model):
	book = models.ForeignKey(Book, on_delete = models.CASCADE)
	number = models.IntegerField()
	title = models.CharField(max_length=30, default="title")
	text = models.TextField()
	pub_date = models.DateTimeField('Дата публикауции', default=timezone.now)

	class Meta:
		verbose_name = 'Глава'
		verbose_name_plural = 'Главы'

	def __str__(self):
		return f"Глава {self.number}"


class Comment(models.Model):
	chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE)
	author_name = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
	comment_text = models.CharField(max_length = 50000)
	pub_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'


class Person(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="person")
	read = models.ManyToManyField("Book", blank=True, related_name="users")

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = 'Людь'
		verbose_name_plural = 'Люди'