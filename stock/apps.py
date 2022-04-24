from django.apps import AppConfig
import pickle
import pandas as pd


class StockConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stock'


model = pickle.load(open('ss_model.pkl','rb'))


# @app.route('/api',methods=['POST'])
def predict():
    # 하루 주가 데이터 불러오기
    data = pd.read_csv('stock_price_API/stockprice_data.csv')
    # 삼성 종가 추출
    close = data[2][-2]
    # 모델에 데이터(삼성 1일 종가) 입력
    prediction = model.predict(close)
    # 가장 최신 예측값 output으로 추출
    output = prediction[0]
    # front ~ output==1:상승, output==0:하락
    return output

if __name__ == '__main__':
    predict()
    # app.run(port=5000, debug=True)