from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser.find_element(By.ID, "latitude").send_keys("48.819626" + Keys.ENTER) #récupérer lat/long avec le main
browser.find_element(By.ID, "longitude").send_keys("2.404811" + Keys.ENTER)
browser.find_element_by_class_name("btn.btn-primary").click()
adress = browser.find_element(By.ID, "address").text
print(adress)
