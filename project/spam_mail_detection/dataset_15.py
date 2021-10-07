from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import re

def find_link_href(url, domain):
  try:
    header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
    html = requests.get(url, headers=header, timeout=5).text
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find_all('link')

  # if link source is not from its own web site, it will return 0
    cnt = 0
    for i in range(len(tag)):
      if domain not in str(tag[i]):
        cnt += 1
    if cnt == 0:
      return 0
    return cnt / len(tag)
  except:
    return 0

def get_domain(url):
  domain = ""
  cnt = 0
  for i in url:
    if i == '/':
      cnt += 1
    if cnt == 3:
      break
    if cnt == 2:
      domain += i
  domain = domain[1:]
  return domain

df = pd.read_csv('verified_online.csv')
df = pd.DataFrame(df)
df = pd.DataFrame(df['url'])
df['href'] = 0
df['href'] = df['href'].astype('float64')

for i in range(3000, 11018):
  url = df['url'][i]
  domain = get_domain(url)
  try:
    df.loc[[i], 'href'] = find_link_href(url, domain)
  except:
    df.loc[[i], 'href'] = 0
df.to_csv('./data_15.csv', mode='w')
