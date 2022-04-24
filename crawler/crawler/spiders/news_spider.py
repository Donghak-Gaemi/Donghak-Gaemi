# -*- coding: utf-8 -*-

import scrapy
from ..items import Item

# url_request 코드 --> [ i종목의 j신문사 기사 크롤링 for j in 신문사 for i in 종목]
# 어떻게 짜지....?
class NewsSpider(scrapy.Spider):
    name = "news"
    # 최신순
    # 종목 = ['NAVER',
    #  '삼성전자',
    #  '아모레퍼시픽',
    #  '현대차',
    #  'LG화학',
    #  '카카오',
    #  'POSCO',
    #  'SK바이오사이언스',
    #  '엔씨소프트',
    #  '두산중공업',
    #  'HMM',
    #  '아시아나항공',
    #  '한화솔루션',
    #  '신세계',
    #  '에스엠',
    #  '유한양행',
    #  '카카오게임즈',
    #  'SK하이닉스',
    #  '셀트리온',
    #  '현대모비스']
    # 신문사 = {'1011':'서울경제','1018':'이데일리', '1014':'파이낸셜뉴스'}
    
    # 아래 예시(첫 줄)는 최신순 정렬 / 서울경제 신문사 / 삼성전자 검색 url
    urls = [
        "https://search.naver.com/search.naver?where=news&query=삼성전자&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1011&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0",
        # "https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1018&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0",
        # "https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=1&office_type=1&office_section_code=3&news_office_checked=1014&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0",
    ]

    def parse(self, response):
        # 한 페이지 내의 전체 뉴스 url 파싱(페이지당 10개 뉴스)
        news_page_links = response.css('a.news_tit::attr(href)').getall()
        # parse_news 에 위에서 파싱한 url 넘겨주기
        yield from response.follow_all(news_page_links, self.parse_news)
        # 다음 페이지 링크 파싱
        pagination_links = response.css('a.btn_next').attrib['href']
        # 재귀(다음 페이지 파싱)
        yield from response.follow_all(pagination_links, self.parse)

    def parse_news(self, response):
        # 데이터 클렌징
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        # 뉴스 정보를 파싱 및 저장

        # 1. scrapy crawl news
        # 문제 : 인코딩 안됨, jl 파일로 저장됨. -> json으로 출력하는 방법 모르겠음
        item = Item()
        item['date'] = extract_with_css('span.url_txt::text').split()[0]
        item['title'] = extract_with_css('div.art_tit::text')
        item['article'] = ''.join(response.css('div.article_view::text').getall()).strip()
        yield item

        # 2. scrapy crawl news -O news.json
        # yield {
        #     'date': extract_with_css('span.url_txt::text').split()[0],
        #     'title': extract_with_css('div.art_tit::text'),
        #     'article': ''.join(response.css('div.article_view::text').getall()).strip(),
        # }