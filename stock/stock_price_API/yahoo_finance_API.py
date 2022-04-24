import pandas as pd

import yfinance as yf
from datetime import date, datetime, timedelta
from pandas import DataFrame, Series
import re
from pytz import timezone
import schedule, time
from openpyxl import Workbook

KST = timezone('Asia/Seoul')
today = datetime.now()
today = today.astimezone(KST)

# 주식 이름과 코드(딕셔너리)
codePairs = { "035420.KS":"네이버", "005930.KS":"삼성전자", "090430.KS":"아모레퍼시픽",
        "005380.KS":"현대차", "051910.KS":"LG화학", "035720.KS":"카카오",
        "005490.KS":"POSCO", "302440.KS":"SK바이오사이언스", "036570.KS":"엔씨소프트",
        "034020.KS":"두산중공업", "011200.KS":"HMM","020560.KS":"아시아나항공",
        "009830.KS":"한화솔루션", "004170.KS":"신세계", "041510.KQ":"에스엠",
        "000100.KS":"유한양행", "293490.KQ":"카카오게임즈", "000660.KS":"SK하이닉스",
        "068270.KS":"셀트리온", "012330.KS":"현대모비스"}

# names = codePairs.values() #주식 이름만 추출해서 리스트화
# codes = codePairs.keys() #주식 코드만 추출해서 리스트화

# codePairs.keys()가 리스트로써의 기능을 못해서 따로 codes 리스트를 만듦
codes = ["035420.KS", "005930.KS", "090430.KS", "005380.KS", "051910.KS", "035720.KS",
         "005490.KS", "302440.KS", "036570.KS", "034020.KS", "011200.KS", "020560.KS",
         "009830.KS", "004170.KS", "041510.KQ", "000100.KS", "293490.KQ", "000660.KS",
         "068270.KS", "012330.KS"]

# # 조회할 날짜 정하기
# if today.hour < 16: # 장마감시간 전에는 하루 전날의 데이터
#     resultDate = date.today()-timedelta(1)
# else:
#     resultDate = date.today() # 장마감 후에는 오늘 정보 업데이트
# ##resultDate = re.sub("-", "", resultDate)

def job():
  df = yf.download(codes, start=date.today(), end=date.today())
  df.to_excel('donghakgaemi/stock/stock_price_API/yahooFinanceAPI_data.xlsx')

schedule.every(1).days.do(job)

while True:
  schedule.run_pending()
  time.sleep(1)
