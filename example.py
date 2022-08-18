from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(r"C:\Users\BykovGA\Desktop\Development\py\selenium\python_selenium_sf\chromedriver")
driver.get("https://google.com")
driver.find_element(By.XPATH, "//*[@name=\"q\"]").send_keys('Youtube' + Keys.RETURN)
sleep(2)
driver.save_screenshot('sf.png')
driver.quit()