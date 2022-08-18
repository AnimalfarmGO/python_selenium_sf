from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(r"C:\Users\BykovGA\Desktop\Development\py\selenium\python_selenium_sf\chromedriver")
driver.get("https://twitch.tv")
driver.find_element(By.XPATH, "//*[@aria-label=\"Больше\"]").click()
sleep (3)
#driver.find_elements(By.XPATH, "//*[@class=\"Layout-sc-nxg1ff-0 aleoz\"]")[10].click()
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div/div/div/div/div[3]/div/div/div[11]/a/div/div").click()
sleep (15)
driver.quit()
