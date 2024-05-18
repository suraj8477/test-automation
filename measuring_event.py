import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# from .YourClass import YourClass
# driver=webdriver.firefox()
driver=webdriver.Chrome()
driver.get('https://dashboard.whealthstudio.com/')
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div/div[4]/input").send_keys('9999988888')

driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[5]/div").click()

driver.implicitly_wait(15)
for i in range(6):
    driver.find_elements(By.XPATH, f"/html/body/div/div/div/div/div[3]/div[2]/input[{i+1}]")[0].send_keys(f'{i+1}')
driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[3]/div[3]/div").click()
driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[1]/a[5]").click()
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[1]/div[3]/div").click()
driver.find_element(By.XPATH,"//input[@placeholder='Title']").send_keys("weight main")
event_type=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/select")
measuring_event_type=Select(event_type)
measuring_event_type.select_by_value("measuring")
driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[2]/div[2]/input").send_keys("ponds")
# choose=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[3]/div[2]/input")
# choose.click()
# choose.send_keys("swimming")
# pics=Select(pic)
# driver.find_element(By.XPATH,"//div[contains(text(),'Save')]").click()
# driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[2]/div[2]/div/div[4]/div/div[2]/div[3]").click()
# driver.execute_script("window.scrollTo(0, 600)")
# time.sleep(8)
# event_drop=driver.find_element(By.XPATH,"//div[contains(@class,'eventdropdown')]//div//select[contains(@aria-label,'Default select')]")
# drop=Select(event_drop)
# drop.select_by_value("logging")
time.sleep(10)