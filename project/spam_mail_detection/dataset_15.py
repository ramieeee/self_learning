from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def find_link_href(url, domain):
  result = urlopen(url)
  html = result.read()

  soup = BeautifulSoup(html, 'html.parser')
  tag = soup.find_all('link')

  # if link source is not from its own web site, it will return 0
  cnt = 0
  for i in range(len(tag)):
    if domain not in str(tag[i]):
      cnt += 1
  try:
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

for i in range(len(df)):
  url = df['url'][i]
  domain = get_domain(url)
  # df.loc[[i], 'href'] = float(find_link_href(url, domain))
  try:
    df.loc[[i], 'href'] = float(find_link_href(url, domain))
  except:
    pass
