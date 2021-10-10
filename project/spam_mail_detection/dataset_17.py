from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd

# extract domain(e.g. https://youtube.com/ -> youtube.com)
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

def phish_check(domain):
    options = Options()
    options.add_argument("headless") # runs chrome background
    driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
    driver.get('https://www.phishtank.com/')

    find_url = driver.find_element_by_xpath('//*[@id="maincol"]/div/div[2]/form/p/input[1]')
    find_url.send_keys(domain) # search domain
    find_url.send_keys(Keys.RETURN) # enter
    try:
        result = driver.find_element_by_xpath('//*[@id="widecol"]/div/h3').text
        driver.quit()
        if 'This site is not a phishing site' in result:
            return 0
    except:
        driver.quit()
        return 1
        
df = pd.read_csv('verified_online1.csv')
df = pd.DataFrame(df)
df = pd.DataFrame(df['url'])
df['phishtank'] = 0

for i in range(len(df)):
    url = df['url'][i]
    domain = get_domain(url)
    df.loc[[i], 'phishtank'] = phish_check(domain)
df.to_csv('./data_17.csv', mode='w')
