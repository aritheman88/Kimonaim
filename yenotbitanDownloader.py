from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os, requests, pyperclip, shutil
from datetime import date

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

today = date.today()
print(today.year)
print(today)

url_month = ''
if today.month < 10:
    url_month = "0" + str(today.month)
else:
    url_month = str(today.month)

url_day = ''
if today.day < 10:
    url_day = "0" + str(today.day)
else:
    url_day = str(today.day)



yenot_URl = 'http://publishprice.ybitan.co.il/' + str(today.year) + url_month + url_day + '/'
print(yenot_URl)

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors=yes')
options.add_experimental_option("detach", True)

dir_to_save_files = r'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(dir_to_save_files, chrome_options=options)
driver.get(yenot_URl)

links = []


for l in range(200,2900):
    try:
        yenot_xpath = r'/html/body/div/div[2]/table/tbody/tr[' + str(l) + r']/td[2]/a'
        conn = driver.find_element(By.XPATH, yenot_xpath)
        link = conn.get_attribute('href')
        if link.startswith('http://publishprice.ybitan.co.il/' + str(today.year) + url_month + url_day + '/PriceFull') == True:
            links.append(link)
    except:
        continue

print("Total pricefull files detected: ", len(links))
time.sleep(3)
del links[20:]
print(len(links))
print("Number of files after reduction: ", len(links))



dir_to_save_files = os.path.join(r'C:\Users\Ariel\Desktop\Python\Kimonaim\yenotBitan', str(today))
download_dir = r"C:\Users\Ariel\Downloads"


for link in links:
    driver.get(link)
    filename = link[42:]
    path_download = os.path.join(download_dir, filename)
    time.sleep(2)

    # Move the file to a chosen directory
    try:
        shutil.move(path_download, dir_to_save_files)
        print(f"Downloaded {filename} and moved file to directory {dir_to_save_files}")
    except:
        print (f"{filename} already exists in {dir_to_save_files}")

print ("END")


driver.quit()