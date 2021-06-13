from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import random
import time
#specify the path to chromedriver.exe (download and save on your computer)
driver = wd.Chrome(executable_path='D:/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://selfregistration.cowin.gov.in/")

Mob =driver.find_element_by_id('mat-input-0')
Mob.clear()
Mob.send_keys(input('Enter Mobile Number :'))
send_otp=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main-content > app-login > ion-content > div > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col:nth-child(1) > ion-grid > form > ion-row > ion-col.col-padding.md.hydrated > div > ion-button")))
send_otp.click()
time.sleep(2)
enter_otp=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mat-input-1')))
enter_otp.clear()

# enter_otp.click()
enter_otp.send_keys(input("Enter OTP : "))
time.sleep(1)
submit=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#main-content > app-login > ion-content > div > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col > ion-grid > form > ion-row > ion-col:nth-child(3) > div > ion-button'))).click()
time.sleep(3)
schedule=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#main-content > app-beneficiary-dashboard > ion-content > div > div > ion-grid > ion-row > ion-col > ion-grid.beneficiary-box.md.hydrated > ion-row.sepreetor.ng-star-inserted.md.hydrated > ion-col > ion-grid > ion-row.dose-data.md.hydrated > ion-col:nth-child(2) > ul > li > a'))).click()
time.sleep(2)
pin=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mat-input-2'))).send_keys(input('Pincode :'))
time.sleep(2)
search=driver.find_element_by_css_selector('ion-button[type="submit"]')
search.click()
time.sleep(2)
group=driver.find_element_by_css_selector('label[tabindex="0"]').click()
time.sleep(5)
 
t=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#main-content > app-appointment-table > ion-content > div > div > ion-grid > ion-row > ion-col > ion-grid > ion-row > ion-col:nth-child(2) > form > ion-grid > ion-row:nth-child(2) > ion-col > div.covid-button-desktop.ion-text-end.book-btn.button-container__right > ion-button'))).click()
