from django.db import models

class Receive(models.Model):
    class Meta():
        verbose_name='полученный запрос'
        verbose_name_plural='полученные запросы'
    
    date_in = models.TextField('время принятия запроса')
    method_in = models.TextField('использованный метод')
    host_in = models.TextField('название хоста')
    json_in = models.TextField('json-содержимое')