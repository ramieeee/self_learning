from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://www.phishtank.com/")

keyword = "instagram.com" # 검색어
elem = driver.find_element_by_xpath('//*[@id="maincol"]/div/div[2]/form/p/input[1]')
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

# driver.quit()
