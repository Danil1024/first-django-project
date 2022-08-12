from django.db import models
from django.utils import timezone
from datetime import timedelta


class Сategory(models.Model):
	name = models.CharField('Название Категории', max_length=50, null=False, blank=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория' 
		verbose_name_plural = 'Категории'


class Article(models.Model):
	title = models.CharField('Заголовок', max_length=50, null=False, blank=False)
	text = models.TextField('Содержание', null=False, blank=False)
	publication_date = models.DateTimeField('Дата публикации', auto_now_add=True)
	date_of_change = models.DateTimeField('Дата изменения', default=timezone.now)
	cat = models.ForeignKey( Сategory, verbose_name='Категория', on_delete=models.SET_NULL, null = True)

	
	def save(self, *args, **kwargs):
		self.date_of_change = timezone.now()
		super(Article, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Статья' 
		verbose_name_plural = 'Статьи'




