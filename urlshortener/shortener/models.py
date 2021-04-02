from django.db import models

class Url(models.Model):
    link = models.CharField(max_length=5000)
    uuid = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Url'
        verbose_name_plural = 'Urls'