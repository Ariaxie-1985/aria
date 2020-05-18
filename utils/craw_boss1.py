# coding:utf-8
# @Time  : 2020/2/18 22:09
# @Author: Xiawang
# Description:


from bs4 import BeautifulSoup

soup = BeautifulSoup(open('boss1.html', encoding='utf-8'), "html.parser")

for company in soup.find_all(attrs={'class': 'conpany-text'}):
    print(company.h4.text)