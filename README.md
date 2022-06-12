# 동학개미 - 주식 뉴스 분석 및 주가 예측 웹사이트

> [2021 한이음 공모전 동학개미팀] 빅데이터 기반 주식 및 뉴스 분석 시스템 구축

* Paper : [A Stock trend Prediction based on Explainable Artificial Intelligence](https://www.koreascience.or.kr/article/CFKO202133648830923.page)
* Tech Stacks : django, scikit-learn, xai, html, scrapy, beautiful-soup, mongodb, mysql, nlp
* Tools : figma, pycharm, git, jupyter-notebook, aws-ec2

<br/>

## 📖 상세 내용

![동학개미 소개](https://user-images.githubusercontent.com/90924434/173228452-0d7140c8-72cd-4f19-9bdc-307c559b36a0.png)

<aside>
  
📈 동학개미는 **주가 예측 및 종목 뉴스 분석 서비스**로 동학 개미들의 합리적인 투자 결정을 응원하는 마음으로 시작된 프로젝트입니다. 동학 개미를 위한 프로젝트이므로 국내 주식을 대상으로 합니다. 해당 주식이 90일 후에 상승할지 하락할지에 대한 **전망을 예측**한 결과와 관련 뉴스가 주식에 긍정적인 영향을 줄지, 부정적인 영향을 줄지 **감성 분석**한 결과를 제공합니다. 주가 예측엔 앙상블 알고리즘이 사용되었으며, **설명 가능 인공지능 XAI 기법**중 **SHAP기법**을 활용하여 모형을 해석 가능한 형태로 제시합니다.

</aside>

<br/>

## 🗺  서비스 구성도

![동학개미 서비스 구성도](https://user-images.githubusercontent.com/90924434/173228460-11f886f3-8f3e-43a6-8792-85c773c13468.png)

<br/>

## 🛠️ 사용 기술 및 라이브러리

- Python Django,MongoDB, MySQL
- XAI - shap, Scikit-learn
- html, css
- scrapy, beautifulsoup, konlpy, nltk
- Aws - ec2, apache2

<br/>

## 🌱  역할 분배

- **정수민** : 팀장, 프로젝트 관리, 주가 데이터 수집 및 저장, 주가 전망 예측 실험 및 논문 작성, 서버 담당
- **김지현** : 뉴스 데이터 수집 및 저장, 감성 분석, 주가 전망 예측 실험 및 논문 작성(1저자), 프로젝트 배포
- **이연수** : 프론트엔드 + 백엔드 전반, 주가 전망 예측 실험 및 논문 작성
- **조설아** : 뉴스 데이터 수집 및 저장, 주가 전망 예측 실험 및 논문 작성, 프론트(베이스)
- **안정은** : 주가 전망 예측 실험 및 논문 작성

<br/>

## 💡 깨달은 점

- 설명 가능 인공지능 기법을 통해 인공지능 모형의 학습 과정을 분석할 수 있음.
- 주식 데이터의 노이즈를 autoencoder를 활용하여 제거
    
    → 논문지에 해당 내용을 추가해 등재하기 위해 현재 프로젝트 진행중(2021.03-2022.06)
    
- 정형 데이터 분석에서 딥러닝 모델보다 앙상블 모델로 우수한 성능을 낼 수 있음.
- 장기 프로젝트에 작업량이 많아 팀원들이 모두 지칠 수 있는 상황이었지만, 함께할 때 시너지가 좋은 팀원들을 만나면 재밌게 진행할 수 있음.
- 팀원들 5명이 모두 비슷한 기술 스택을 가지고 있어서, 분배가 어려움.
    - 해결: 웹개발 파트를 기능별로 나눠서 작업 분배.

<br/>

## 👀  서비스 화면

![서비스 화면 메인 - AI 분석](https://user-images.githubusercontent.com/90924434/173228468-b5a79316-c55c-4ee8-8a7c-4179fd89ac4b.png)

![서비스 화면 1 - 감성 분석](https://user-images.githubusercontent.com/90924434/173228474-817c2ecf-9049-4712-8782-9eb2afe507e9.png)

![서비스 화면 2 - 캔들 스틱 차트](https://user-images.githubusercontent.com/90924434/173228484-75d38ce1-a2c1-4768-9fb9-b54164c000cf.png)
