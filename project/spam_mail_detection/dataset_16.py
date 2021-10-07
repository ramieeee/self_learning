import requests
import pandas as pd

df = pd.read_csv('verified_online.csv')
df = pd.DataFrame(df)
df = pd.DataFrame(df['url'])
df['redirect'] = 0
df['redirect'] = df['redirect'].astype('float64')

for i in range(len(df)):
  url = df['url'][i]

  header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}
  try:
    responses = requests.get(url, headers=header, timeout=5)

    cnt = 0
    for i in range(len(responses.history)):
        cnt = i
    try:
      df.loc[[i], 'redirect'] = cnt
    except:
      df.loc[[i], 'redirect'] = 0
  except:
    df.loc[[i], 'redirect'] = 0
df.to_csv('./data_16.csv', mode='w')
