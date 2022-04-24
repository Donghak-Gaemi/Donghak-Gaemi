import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView
from django.views.generic import View
from time import mktime, strptime
from stock.models import stockModel, priceModel, predictModel, accuracyModel, newsModel, sentimentModel
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from django.core import serializers


# Create your views here.

# 종목 리스트
def home(request):
    MAX_LIST_CNT = 10 # 한 페이지에 보여주는 종목 수
    name = stockModel.objects.values('stock_name')
    r = []
    for n in name: # 주식 리스트 생성
        code = stockModel.objects.filter(stock_name=n['stock_name']).values('stock_code')[0]
        price_id = priceModel.objects.filter(stock_code = code['stock_code']).order_by('-date').values('stock_id')[0] # 주가 아이디
        close = priceModel.objects.filter(stock_code = code['stock_code']).order_by('-date').values('close')[0]
        before = priceModel.objects.filter(stock_code = code['stock_code']).order_by('-date').values('close')[1]
        fluc = round(((close['close'] - before['close'])/close['close']), 2)
        fluction = {'fluction':fluc}
        predict = predictModel.objects.filter(stock_id = price_id['stock_id']).values('result')[0]
        accuracy = accuracyModel.objects.filter(stock_code = code['stock_code']).order_by('-model_id').values('accuracy')[0]
        result = {**n, **code, **close, **predict, **accuracy, **price_id, **fluction}
        r.append(result)

    page = request.GET.get('page', 1)  # page 번호를 get 파라미터로 받고 없으면 기본값 1로 설정
    list = r
    paginator = Paginator(list, MAX_LIST_CNT)
    page_obj = paginator.get_page(page)
    context = {'page': page_obj}
    return render(request, 'stock/list.html', context)

'''
# 종목 상세페이지(뉴스)
def detail_stock_news(request, id):
    close = priceModel.objects.get(stock_id = id)
    before = priceModel.objects.filter(stock_code = close.stock_code).order_by('-date').values('close')[1]
    diff = (close.close - before['close'])
    difference = {'difference': diff}
    fluc = round((close.close - before['close']) / close.close,2)
    fluction = {'fluction': fluc}
    stock = close.stock_code
    price = priceModel.objects.filter(stock_code = close.stock_code).order_by('date')
    close_list = []
    open_list = []
    for p in price:
        time_tuple = strptime(str(p.date), '%Y-%m-%d')
        utc_now = mktime(time_tuple) * 1000
        close_list.append([utc_now, p.close])
        open_list.append([utc_now, p.open])

    # 뉴스
    news_id = newsModel.objects.filter(stock_code = close.stock_code).order_by('-registration_date').values('news_id')
    news_list = []
    for n in news_id:
        news_press = newsModel.objects.filter(news_id = n['news_id']).values('press')[0]
        news_link = newsModel.objects.filter(news_id = n['news_id']).values('link')[0]
        news_title = newsModel.objects.filter(news_id = n['news_id']).values('title')[0]
        result = sentimentModel.objects.filter(news_id = n['news_id']).values('result')[0]
        list = {**news_press, **news_link, **news_title, **result}
        news_list.append(list)

    MAX_LIST_CNT = 6
    page = request.GET.get('page', 1)  # page 번호를 get 파라미터로 받고 없으면 기본값 1로 설정
    list = news_list
    paginator = Paginator(news_list, MAX_LIST_CNT)
    page_obj = paginator.get_page(page)
    price = {'close':close,
             'difference':difference,
             'fluction':fluction,
             'stock':stock,
             'close_list':close_list,
             'open_list':open_list,
             'page':page_obj}
    #stock = stockModel.objects.filter(stock_code = price['stock_code_id']).values()
    return render(request, 'stock/detail.html', price)
'''

def detail_stock_news(request, id):
    close = priceModel.objects.get(stock_id = id)
    before = priceModel.objects.filter(stock_code = close.stock_code).order_by('-date').values('close')[1]
    diff = (close.close - before['close'])
    difference = {'difference': diff}
    fluc = round((close.close - before['close']) / close.close,2)
    fluction = {'fluction': fluc}
    stock = close.stock_code
    price = priceModel.objects.filter(stock_code = close.stock_code).order_by('date')
    chart_list = []
    close_list = []
    for p in price:
        time_tuple = strptime(str(p.date), '%Y-%m-%d')
        utc_now = mktime(time_tuple) * 1000
        chart_list.append([utc_now, p.open, p.high, p.low, p.close])
        close_list.append(p.close)

    # 뉴스
    news_id = newsModel.objects.filter(stock_code = close.stock_code).order_by('-registration_date').values('news_id')
    news_list = []
    for n in news_id:
        news_press = newsModel.objects.filter(news_id = n['news_id']).values('press')[0]
        news_link = newsModel.objects.filter(news_id = n['news_id']).values('link')[0]
        news_title = newsModel.objects.filter(news_id = n['news_id']).values('title')[0]
        result = sentimentModel.objects.filter(news_id = n['news_id']).values('result')[0]
        list = {**news_press, **news_link, **news_title, **result}
        news_list.append(list)

    MAX_LIST_CNT = 6
    page = request.GET.get('page', 1)  # page 번호를 get 파라미터로 받고 없으면 기본값 1로 설정
    list = news_list
    paginator = Paginator(news_list, MAX_LIST_CNT)
    page_obj = paginator.get_page(page)
    price = {'close':close,
             'difference':difference,
             'fluction':fluction,
             'stock':stock,
             'close_list':json.dumps(close_list),
             'chart_list':json.dumps(chart_list),
             'page':page_obj}
    #stock = stockModel.objects.filter(stock_code = price['stock_code_id']).values()
    return render(request, 'stock/detail.html', price)

def detail_ai(request, id):
    close = priceModel.objects.get(stock_id=id)
    before = priceModel.objects.filter(stock_code=close.stock_code).order_by('-date').values('close')[1]
    diff = (close.close - before['close'])
    difference = {'difference': diff}
    fluc = round((close.close - before['close']) / close.close, 2)
    fluction = {'fluction': fluc}
    stock = close.stock_code
    acc = accuracyModel.objects.get(stock_code=close.stock_code)
    accuracy = accuracyModel.objects.filter(stock_code=acc.stock_code).values('accuracy')[0]
    predict = predictModel.objects.filter(model_id=acc.model_id).values('result')[0]
    price = priceModel.objects.filter(stock_code=close.stock_code).order_by('date')
    chart_list = []
    for p in price:
        time_tuple = strptime(str(p.date), '%Y-%m-%d')
        utc_now = mktime(time_tuple) * 1000
        chart_list.append([utc_now, p.open, p.high, p.low, p.close])
    ai = {
        'close':close,
        'difference':difference,
        'fluction':fluction,
        'stock':stock,
        'accuracy':accuracy,
          'predict':predict,
        'chart_list': json.dumps(chart_list),
          }
    return render(request, 'stock/detail_ai.html', ai)




