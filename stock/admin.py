from django.contrib import admin
from .models import stockModel
from .models import priceModel
admin.site.register(stockModel)
admin.site.register(priceModel)

from .models import mongonewsModel
admin.site.register(mongonewsModel)