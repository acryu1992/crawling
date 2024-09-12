import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

current_time = time.strftime("%Y-%m-%d %H%M", time.localtime())
title_list = []

url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EC%86%8D%EB%B3%B4&p='
for i in range(1, 11):
    res = req.get(url + str(i))
    soup = bs(res.text, 'lxml')
    title = soup.select('div.item-title > .tit-g.clamp-g > a')
    for title_ in title:
        title_list.append(title_.text.strip())

dic = {'속보제목' : title_list}
df = pd.DataFrame(dic)
filename = current_time + ".csv"
df.to_csv('data.csv', encoding="euc-kr", index=False)
