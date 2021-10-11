from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def check_alexa_rank(url):
    rank_str = BeautifulSoup(urllib.request.urlopen("https://www.alexa.com/minisiteinfo/" + url),'html.parser').text
    rank_str = rank_str.split()

    if rank_str[7] == 'No':
        return 1
    else:
        rank_num = rank_str[7][1:]
        rank_int=int(rank_num.replace(',',''))
        if rank_int:
            return 0

df = pd.read_csv('verified_online.csv')
df = pd.DataFrame(df)
df = pd.DataFrame(df['url'])
df['alexa'] = 0

for i in range(len(df)):
    url = df['url'][i]
    try:
        df.loc[[i], 'alexa'] = check_alexa_rank(url)
    except:
        df.loc[[i], 'alexa'] = 'N/A'
    
# df.to_csv('./data_18.csv', mode='w')
