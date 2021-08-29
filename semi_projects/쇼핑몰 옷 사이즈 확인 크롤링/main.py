import shopping_mall_size_crawling as crawling
import kakao_token_manage as ktm
import time

if __name__ == '__main__':
    crawl = crawling.size_check_bot()
    try:
        crawl.run_process()
    except:
        ktm.refreshToken()
        time.sleep(5)
        crawl.run_process()