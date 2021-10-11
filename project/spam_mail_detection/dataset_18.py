from bs4 import BeautifulSoup
import urllib.request

url=''
rank_str = BeautifulSoup(urllib.request.urlopen("https://www.alexa.com/minisiteinfo/" +url),'html.parser').text
rank_str = rank_str.split()

if rank_str[7] == 'No':
    print('none')
else:
    rank_num = rank_str[7][1:]
    rank_int=int(rank_num.replace(',',''))
    print(rank_str)
    print()
    print('%s\n' %url)
    print('the rank is #%d' %rank_int)
