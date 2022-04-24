import pandas as pd
import re

def cleansing(text):
    try:
        pattern = "\[.*\]|\s-\s.*" # 대괄호 안에있는 언론사 정보 제거
        text = re.sub(pattern=pattern, repl='', string=text)
        pattern = '[0-9]' # 숫자제거
        text = re.sub(pattern=pattern, repl='', string=text)
        pattern = '[^\w\s]' # 특수기호제거
        text = re.sub(pattern=pattern, repl='', string=text)
        pattern = '([ㄱ-ㅎㅏ-ㅣ]+)' # 한글 자음, 모음 제거
        text = re.sub(pattern=pattern, repl='', string=text)
        pattern = '네이버|파이낸셜뉴스|서울경제|이데일리|머니투데이|뉴스|데일리 뉴스|헤럴드 경제|금지|무단|배포|저작권'
        text = re.sub(pattern=pattern, repl='', string=text)
        return text
    except TypeError:
        pass

from konlpy.tag import Komoran
komoran = Komoran(userdic='dic/userdic.txt')
def tokenizing(text):
    try:
        tagged = komoran.pos(text)

        # 일반 명사, 고유 명사, 형용사만 추출
        token = [ word for word,pos in tagged if pos in ['NNG','NNP','VA']]
        return token
    except AttributeError:
        pass


pos_dic = ('상승','급등','실적','매수의견','강화','확대','규모','무상증자','유상감자','자사주','수혜',\
           '고배당','신제품','개발','취득','신고가','최초','추천','실적개선','리포트','액면분할','병합',\
           '추진','신규','테마','매수세','성장세','증가','기대','호실적','깜짝실적','고속 성장','최대',\
           '최대치','호조','신사업 호조','서프라이즈','쾌조','최고','최고실적','줄상향','상향','장미빛',\
           '흑자','오를','오르다','긍정적','경영권분쟁','기대감','강세')

neg_dic = ('적자','검찰 조사','임금체불','적발','미지급','위반','논란','약세','좌절','하락','부정적',\
           '유상증자','무상감자','순삭','관리종목','감사의견','불성실','불성실공시','실적악화','악화',\
           '규제','소송','횡령','환율이슈','고점매도','회피','매도세','재무부담','우려','부담','분통','지적','급락','감소','떨어졌')

def pos_scoring(tokens_list, sent_dic):
    try:
        match_word = [x for x in tokens_list if x in sent_dic]

        score = len(match_word)

        return score
    except TypeError:
        pass

def neg_scoring(tokens_list, sent_dic):
    try:
        match_word = [x for x in tokens_list if x in sent_dic]

        score = len(match_word) * -1

        return score
    except TypeError:
        pass

def tagging(sent):
    try:
        if sent > 0:
            return 1 # 긍정으로 분석된 경우
        elif sent == 0:
            return 0 # 중립으로 분석된 경우
        elif sent < 0:
            return -1 # 부정으로 분석된 경우
    except:
        pass



# test
#text = '상승할 가능성이 높다. 장미빛 미래가 있다. 하락하지 않는다. 하락'
#text = cleansing(text)
#tokens_list = tokenizing(text)
#print('부정 감성 지수',neg_scoring(tokens_list, pos_dic))
#print('긍정 감성 지수', pos_scoring(tokens_list, neg_dic))
#sent  = neg_scoring(tokens_list, pos_dic) + pos_scoring(tokens_list, neg_dic)
#print('종합 분석 의견', tagging(sent))

