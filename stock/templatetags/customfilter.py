from django import template
from stock.models import priceModel, stockModel, predictModel, accuracyModel, sentimentModel

register = template.Library()


@register.filter(name = 'newslist')
def newslist(value):
    sentiment = sentimentModel.objects.filter(news_id = value).values('result')[0]
    result = sentiment['result']
    return result