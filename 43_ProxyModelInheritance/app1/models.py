from django.db import models


# Create your models here.
class MarketModel(models.Model):
    name = models.CharField(max_length=80, verbose_name='Market Name')
    address = models.CharField(max_length=1000)

class ProxyMarketModel(MarketModel):
    class Meta:
        proxy = True
        ordering = ['id']