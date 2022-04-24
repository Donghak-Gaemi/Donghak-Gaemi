from django.db import models
class stockModel(models.Model):
    class Meta:
        db_table = "stock"
        managed = False,
        app_label = "default"

    stock_name = models.CharField(max_length=20, null=False, blank=False)
    stock_code = models.CharField(primary_key = True, max_length = 10, null=False, blank=False)
    stock_category = models.CharField(max_length=20, null=False, blank=False)
    stock_foundation_year = models.DateField(null=False, blank=False)
    stock_listing_date = models.DateField(null=False, blank=False)

class priceModel(models.Model):
    class Meta:
        db_table = "price"
        managed = False,
        app_label = "default"

    stock_id = models.IntegerField(primary_key=True, null=False, blank=False, db_column = 'stock_id')
    date = models.DateField(null = False, blank = False)
    open = models.IntegerField(null = False, blank = False)
    high = models.IntegerField(null = False, blank = False)
    low = models.IntegerField(null = False, blank = False)
    close = models.IntegerField(null = False, blank = False)
    volume = models.IntegerField(null = False, blank = False)
    stock_code = models.ForeignKey(stockModel, on_delete = models.CASCADE, db_column = 'stock_code')

class accuracyModel(models.Model):
    class Meta:
        db_table = "accuracy"
        managed = False,
        app_label = "default"

    model_id = models.IntegerField(primary_key=True, null=False, blank=False, db_column='model_id')
    accuracy = models.IntegerField(null=False, blank = False)
    stock_code = models.ForeignKey(stockModel, on_delete=models.CASCADE, db_column='stock_code')


class predictModel(models.Model):
    class Meta:
        db_table = "predict"
        managed = False,
        app_label = "default"

    model_id = models.ForeignKey(accuracyModel, on_delete=models.CASCADE, db_column = 'model_id')
    stock_id = models.ForeignKey(priceModel, on_delete=models.CASCADE, db_column = 'stock_id')
    result = models.IntegerField(null=False, blank = False)

class newsModel(models.Model):
    class Meta:
        db_table = "news"
        managed = False,
        app_label = "default"

    news_id = models.IntegerField(primary_key = True, null = False, blank = False, db_column='news_id')
    title = models.CharField(max_length = 100, null = False, blank = False)
    content = models.TextField(max_length = 20000, null = False, blank = False)
    summary = models.CharField(max_length = 500, null = False, blank = False)
    registrant = models.CharField(max_length = 18, null = False, blank = False) # 등록자(기자)
    press = models.CharField(max_length = 18, null = False, blank = False) # 언론사
    registration_date = models.DateField(null = False, blank = False) # 등록 날짜
    link = models.CharField(max_length = 200, null = False, blank = False) # 링크
    stock_code = models.ForeignKey(stockModel, on_delete=models.CASCADE, db_column='stock_code')


class sentimentModel(models.Model):
    class Meta:
        db_table = "sentiment"
        managed = False,
        app_label = "default"

    news_id = models.ForeignKey(newsModel, on_delete=models.CASCADE, db_column='news_id')
    result = models.IntegerField(null = False, blank = False)


from djongo import models as mgmodels

class mongonewsModel(mgmodels.Model):
    class Meta:
        managed = False,
        app_label = "news"

    title = mgmodels.CharField(max_length=100),
    newspaper = mgmodels.CharField(max_length=50),
    datetime = mgmodels.DateField(),
    content = mgmodels.CharField(max_length=20000),
    stock_code = mgmodels.CharField(),
    link = mgmodels.CharField(max_length=500),
    pos = mgmodels.IntegerField(),
    neg = mgmodels.IntegerField(),
    result = mgmodels.IntegerField()