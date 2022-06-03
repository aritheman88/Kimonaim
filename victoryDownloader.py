from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

# chrome_options = Options(chrome_options.add_experimental_option("detach", True))
#
# driver = webdriver.Chrome(options=chrome_options)



import os, requests, pyperclip, shutil
from datetime import date

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors=yes')
options.add_experimental_option("detach", True)

dir_to_save_files = r'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(dir_to_save_files, chrome_options=options)

driver.get('http://matrixcatalog.co.il/NBCompetitionRegulations.aspx')
select_chain = Select(driver.find_element(By.CSS_SELECTOR, '#MainContent_chain'))
select_chain.select_by_visible_text('ויקטורי')
time.sleep(12)

search_button = driver.find_element(By.ID, "MainContent_btnSearch").click()
select_pricefull = Select(driver.find_element(By.CSS_SELECTOR, '#MainContent_fileType'))
select_pricefull.select_by_visible_text('מחירים מלא')
time.sleep(12)
search_button = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/div/div[1]/div[1]/div/input').click()
time.sleep(10)

#
xpath_selectors = [
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[2]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[3]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[4]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[5]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[6]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[7]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[8]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[9]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[10]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[11]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[12]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[13]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[14]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[15]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[16]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[17]/td[8]/a',
    '/html/body/form/div[3]/div[3]/div/div[2]/table/tbody/tr[18]/td[8]/a'
]

today = date.today()
dir_to_save_files = os.path.join(r'C:\Users\Ariel\Desktop\Python\Kimonaim\victory', str(today))
download_dir = r"C:\Users\Ariel\Downloads"

links = []
for selector in xpath_selectors:
    conn = driver.find_element_by_xpath(selector)
    link = conn.get_attribute('href')
    links.append(link)

    # Download file to default folder
    driver.get(link)
    time.sleep(3)
    filename = link[76:]
    path_download = os.path.join(download_dir, filename)

    # Move the file to a chosen directory
    try:
        shutil.move(path_download, dir_to_save_files)
        print(f"Downloaded {filename} and moved file to directory {dir_to_save_files}")
    except:
        print (f"{filename} already exists in {dir_to_save_files}")

driver.quit()
print("Finished downloading")


