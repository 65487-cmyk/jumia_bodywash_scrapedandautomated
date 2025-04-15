from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import os
import sys
import time
import pandas as pd


now=datetime.now()
year_month_date=now.strftime('%Y%m%d')
website='https://www.jumia.co.ke/skin-care-body-washes/#catalog-listing'
#set selenium to default headless mode
option1=Options()
option1.add_argument("--headless")  # Ensure this argument is set
option1.add_argument("--disable-gpu")  # Disable GPU acceleration (can be helpful for headless mode)
option1.add_argument("--no-sandbox")  # For some environments like Docker


service1=Service(executable_path='chromedriver.exe')

driver=webdriver.Chrome(service=service1, options=option1)

driver.get(website)

#handle newsletter popup
news_button=WebDriverWait(driver,10).until(
   EC.element_to_be_clickable((By.XPATH,
'//button[@class="cls" and @aria-label="newsletter_popup_close-cta"]'))
)
news_button.click()
#handle cookie popups
cookie_btn=WebDriverWait(driver,5).until(
   EC.element_to_be_clickable((By.XPATH,
     '//span[contains(text(), "Accept cookies")]'))
)
cookie_btn.click()
#find elements



productnames=[]
newprices=[]
oldprices=[]
reviews=[]
totalstars=[]

page=1
while True:
   page +=1
   files=driver.find_elements(by='xpath', value='//div[@class="info"]')

   for file in files:
      try:
         productname=file.find_element(By.XPATH, value='./h3').text
      except:
         productname='N/A'

      try:
         newprice=file.find_element(By.XPATH, value='./div[@class="prc"]').text
      except:
         newprice='N/A'

      try:
         oldprice=file.find_element(By.XPATH, value='.//div[@class="s-prc-w"]/div').text
      except:  
         oldprice='N/A'

      try:
         totalreview=file.find_element(By.XPATH, value='.//div[@class="rev"]').text
      except:
         totalreview='N/A'

      try:
         stars=file.find_element(By.XPATH, value='.//div[contains(@class,"stars")]').get_attribute('aria-label')
      except:
         stars='N/A'

      productnames.append(productname)
                    
      newprices.append(newprice)
      oldprices.append(oldprice)
      reviews.append(totalreview)
      totalstars.append(stars)
#click the next page button
   try:
      next_button=WebDriverWait(driver,5).until(
         EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Next Page"]')))
      driver.execute_script("arguments[0].scrollIntoView();", next_button)  # helps in headless mode
      next_button.click()
#wait for new page to load
      WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="info"]'))
        )
   except:
      break
          

df_bodywashes=pd.DataFrame({'Name':productnames,
              'currentprice':newprices,
              'formerprice':oldprices,
              'Reviews':reviews,
              'Totalstars':totalstars})
application_path=os.path.dirname(sys.executable)
file_name=f'pricereport7py={year_month_date}.csv'
file_path=os.path.join(application_path,file_name)
df_bodywashes.to_csv(file_path)

print('Scraping done!check the csv file')

driver.quit()