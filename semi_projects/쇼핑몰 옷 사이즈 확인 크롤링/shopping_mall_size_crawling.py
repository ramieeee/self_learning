import kakao_token_manage as ktm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

class size_check_bot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("headless")
        self.options.add_argument("--window-size=1024,768")
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=self.options)
        self.webpage = "https://troubadour.kr/product/detail.html?product_no=1105"
        self.driver.get(self.webpage)
        time.sleep(3)

    def find_path(self):
        color_xpath = '//*[@id="df-product-detail"]/div/div[2]/div/div/div[1]/div[1]/ul/li[1]/ul/li[2]/ul/li/a'
        text_xpath = '//*[@id="df-product-detail"]/div/div[2]/div/div/div[1]/div[1]/ul/li[2]/ul/li[2]/p/span'
        self.color = self.driver.find_element_by_xpath(color_xpath)
        self.text = self.driver.find_element_by_xpath(text_xpath)
        self.color.click()
        time.sleep(0.5)
        self.size = self.driver.find_element_by_xpath('//*[@id="df-product-detail"]/div/div[2]/div/div/div[1]/div[1]/ul/li[2]/ul/li[2]/ul/li[2]/a/span')
        self.size.click()
        time.sleep(0.5)

    def send_message(self):
        check_text = self.text.text
        if '품절' in check_text:
            ktm.sendMessageToMe("재고 \"없음\"")
        else:
            ktm.sendMessageToMe("재고 \"있음\"")
            file = "previous_message.txt"
            if file not in os.listdir():
                with open(file, 'w') as w:
                    w.write("sent")

    def kill_process(self):
        self.driver.quit()
    
    def check_previous_message(self):
        file = "previous_message.txt"
        if file not in os.listdir():
            with open(file, 'w') as w:
                w.write("")

        data = open(file, 'r')
        a = data.readline().strip()

        if a == 'sent':
            return True
        else:
            return False
        
    def run_process(self):
        if self.check_previous_message() == False:
            self.find_path()
            self.send_message()
        self.kill_process()