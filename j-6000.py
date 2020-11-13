from selenium import webdriver
import time
PROXY = "127.0.0.1:8080" # IP:PORT or HOST:PORT
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)  # 今は chrome_options= ではなく options=

# driver.get('https://iknow.jp/content/japanese')
# print(driver.title)
driver.get('https://iknow.jp/courses/566921')
time.sleep(3)

mp3 = driver.find_elements_by_xpath('//div[@class="item-audio-container"]')
for m in mp3:
    m.find_element_by_xpath('./span').click()
    time.sleep(1)
driver.save_screenshot('results.png')
driver.quit()