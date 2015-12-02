from django.db import models


class Poster(models.Model):

    title = models.CharField(max_length=100, verbose_name='film title', unique=True)
    poster = models.ImageField(upload_to='uploads/posters', verbose_name='film poster')
    date = models.DateTimeField(auto_now=True, verbose_name='search date')

    class Meta:
        db_table = 'poster'
        verbose_name_plural = 'posters'
