import os
import re
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
import time
from konlpy.tag import Okt
from collections import Counter


SAVE_DIR = "./results"


def save_review_from_url(base_url, save_name):  # 리뷰를 텍스트 파일에 저장
    def no_space(text):
        text1 = re.sub('&nbsp;|&nbsp;|\n|\t|\r', '', text)
        text2 = re.sub('\n\n','', text1)
        return text2

    res = requests.get(base_url)
    if res.status_code == 200:
        soup=BeautifulSoup(res.text,'lxml')
        total = soup.select('div.score_total > strong > em')[0].text
        pages = int(total.replace(',','')[:-1]) #17,921 > 17921로 변환 후 캐스팅
        print(f"{pages}개의 페이지에서 리뷰를 모으고 있습니다.")
        time.sleep(1)
    
    stars = []  # 평점
    comments = []  # 리뷰
    for page in tqdm(range(1, pages+1)):
        url = base_url.format(page)
        cur_url = base_url[:-2] + f"{page}" 
        res = requests.get(cur_url)
        
        # connectino이 잘 되는 경우
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            star = soup.select('div.score_result > ul > li > div.star_score > em')
            tds = soup.select('div.score_result > ul > li > div.score_reple > p > span')
            for st in star:
                stars.append(int(st.text))
            for cmt in tds:
                if cmt.text != '관람객' and cmt.text !='스포일러가 포함된 감상평입니다. 감상평 보기':
                    comments.append(no_space(cmt.text))
            if(len(comments) != len(stars)):
                print(url)
                break

    assert len(comments) == len(stars)
    reviews = list(zip(stars, comments))

    # save reviews
    high_star_comment = []
    for review in reviews:
        star, comment = review
        if star > 5:
            high_star_comment.append(comment)

    with open(os.path.join(SAVE_DIR, f'{save_name}_reviews.txt'), 'w', encoding='UTF-8') as f:
	    for review in high_star_comment:
		    f.write(review + '\n')  # 리뷰마다 줄바꿈




def save_noun_from_txt(name):  # 키워드를 텍스트 파일에 저장
    with open(os.path.join(SAVE_DIR, f'{name}_reviews.txt'), 'r', encoding='utf-8') as f:
        reviews_str = f.read()

    okt = Okt()
    noun = okt.nouns(reviews_str)
    count = Counter(noun)

    # 명사 추출 및 빈도가 높은 n개의 명사 추출
    noun_list = []
    for keyword in count.most_common(50):
        noun_list.append(keyword)

    with open(os.path.join(SAVE_DIR, f'{name}_keywords.txt'), 'w', encoding='UTF-8') as f:
        for keyword, fre in noun_list:
            f.write(keyword + '\n')



def compute_similarity(name1, name2):  # 유사도 계산
    with open(os.path.join(SAVE_DIR, f'{name1}_keywords.txt'), 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
    lst1 = [line.rstrip('\n') for line in lines]

    with open(os.path.join(SAVE_DIR, f'{name2}_keywords.txt'), 'r', encoding = 'utf-8') as f:
        lines = f.readlines()
    lst2 = [line.rstrip('\n') for line in lines]

    # 유사도 구하는 공식 = 교집합/합집합
    similarity = len(list(set(lst1).intersection(lst2))) / len(list(set().union(lst1, lst2)))
    return similarity