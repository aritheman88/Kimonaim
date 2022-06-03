from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os, requests, pyperclip, shutil
from datetime import date

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors=yes')

dir_to_save_files = r'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(dir_to_save_files, chrome_options=options)

driver.get('https://url.publishedprices.co.il/login')
time.sleep(2)
userElem = driver.find_element(By.CSS_SELECTOR, '#username')
userElem.send_keys('osherad')
driver.find_element_by_css_selector('#login-button').click()
time.sleep(2)

searchElem = driver.find_element_by_css_selector('#fileList_filter > input')
searchElem.send_keys(('pricefull'))
time.sleep(5)

xpath_selectors = [
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[1]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[3]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[6]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[9]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[12]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[15]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[16]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[20]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[22]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[24]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[26]/td[1]/a',
    '/html/body/div[2]/div[2]/form/div[2]/table/tbody/tr[28]/td[1]/a'

]


today = date.today()
dir_to_save_files = os.path.join(r'C:\Users\Ariel\Desktop\Python\Kimonaim\osherAd', str(today))
download_dir = r"C:\Users\Ariel\Downloads"

links = []
for selector in xpath_selectors:
    conn = driver.find_element_by_xpath(selector)
    link = conn.get_attribute('href')
    links.append(link)

    # Download file to default folder
    driver.get(link)
    time.sleep(3)

    filename = link[41:]
    path_download = os.path.join(download_dir, filename)

    # Move the file to a chosen directory
    try:
        shutil.move(path_download, dir_to_save_files)
        print(f"Downloaded {filename} and moved file to directory {dir_to_save_files}")
    except:
        print (f"{filename} already exists in {dir_to_save_files}")

print ("END")



# time.sleep(5)
driver.quit()