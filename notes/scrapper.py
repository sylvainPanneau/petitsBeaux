from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


firefox_options =   Options()
firefox_options.add_argument("--headless")
firefox_options.page_load_strategy = 'none'
browser = webdriver.Firefox(options=firefox_options)

browser.get("https://ent.univ-paris13.fr/applications/notes/")
browser.find_element(By.ID, "username").send_keys("12016045")
browser.find_element(By.ID, "password").send_keys("0114016375T")
browser.find_element(By.ID, "submit").click()
moyenne = browser.find_element_by_class_name('ligneResumeMoyenne').text

def alert_new_note(moyenne):
    return float(moyenne) != 16.91 

x=alert_new_note(moyenne)
if x:
    print("Nouvelle note en ligne !")
else:
    print("RAS")

