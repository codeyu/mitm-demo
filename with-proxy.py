from selenium import webdriver

PROXY = "127.0.0.1:8080" # IP:PORT or HOST:PORT
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options) 

driver.get('https://www.google.com/')
print(driver.title)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
print(driver.title)

driver.save_screenshot('search_results.png')
driver.quit()