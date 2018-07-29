from django.db import models

class Sent(models.Model):
    class Meta():
        verbose_name='отправленный запрос'
        verbose_name_plural='отправленные запросы'
    
    uri = models.TextField('URI')
    json_out = models.TextField('отправленный json')
    status = models.TextField('статус ответа')
    json_in = models.TextField('ответный json')

class Token(models.Model):
    code = models.TextField('токен', default='')