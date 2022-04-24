from bs4 import BeautifulSoup
from urllib.request import urlopen

import re
import pandas as pd

# 감성 분석용 초기 test data 구축

def getUrl(bs, stockcode):
    # 맨 마지막 페이지 번호 가져오기
    for link in bs.find_all('a'):
        if '맨뒤' in link.text:
            n = int(link['href'].split('page=')[1].split('&')[0])

    urls = []
    for i in range(1, n + 1):
        url = 'https://finance.naver.com/item/news_news.naver?code=' + stockcode + '&page=' + str(i) + '&sm=title_entity_id.basic&clusterId='
        urls.append(url)
    if urls:
        print('url들을 불러왔습니다')

    return urls


def getLinks(urls, includeUrl):
    internalLinks = []

    for url in urls:
        html = urlopen(url)
        bs = BeautifulSoup(html.read(), 'html.parser')

        # 내부 링크
        for link in bs.find_all('a'):
            if link is not None:
                if link.attrs['href'].startswith(includeUrl):
                    if link not in internalLinks:
                        url = 'https://finance.naver.com/' + link.attrs['href']
                        internalLinks.append(url)

    if internalLinks:
        print(len(internalLinks), '개 링크 수집 완료')

        return internalLinks


def crawl_news(stockcode, internalLinks):
    news = []

    for i, link in enumerate(internalLinks):
        try:
            print(link)
            html = urlopen(link)
            bs = BeautifulSoup(html.read(), 'html.parser')

            # 제목
            title = bs.tbody.find('th').text

            # 신문사, 날짜 시간
            newspaper, datetime = bs.tbody.findAll('th')[1].span.text.split('  ')

            # 기사 내용
            content = bs.find('div', {'id': 'news_read'})
            content.find('div', {'class': "link_news"}).extract()
            content = re.sub("\n|\t", "", content.text)

            news.append([title, newspaper, datetime, content, stockcode, link])

            if i % 10 == 0:
                print(i, '번째 기사 수집중----------------------')

        except AttributeError:
            continue

    return news


from pymongo import MongoClient

def crawl_news_to_db(stockcode):
    url = 'https://finance.naver.com/item/news_news.naver?code='+stockcode+'&page=&sm=title_entity_id.basic&clusterId='
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    includeUrl = '/item/news_read.naver?article_id'

    urls = getUrl(bs, stockcode)
    internalLinks = getLinks(urls, includeUrl)
    news = crawl_news(stockcode, internalLinks)

    # localhost에 연결
    client = MongoClient('localhost', 27017)

    db = client.donghakgaemi

    df = pd.DataFrame(news, columns=['title', 'newspaper', 'datetime', 'content', 'stockcode', 'link'])

    df.to_csv(stockcode + '.csv', index=False)
    docs = df.to_dict("records")

    for doc in docs:
        db.news.insert_one(doc)



if __name__ == '__main__':
    codes = ["035420", "005930", "090430", "005380", "051910", "035720", "005490", "302440",
            "036570", "034020", "011200", "020560", "009830", "004170", "041510",
            "000100", "293490", "000660", "068270", "012330"]

    for code in codes:
        crawl_news_to_db(code)