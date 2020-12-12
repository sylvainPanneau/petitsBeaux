from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

options = Options()
options.set_preference("browser.download.folderList",2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir","./")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
options.set_preference("pdfjs.disabled", True)
options.set_preference("plugin.disable_full_page_plugin_for_types", "application/pdf")
browser = webdriver.Firefox(firefox_options=options)

browser.get("https://media.interieur.gouv.fr/deplacement-covid-19/")
browser.find_element(By.ID, "field-firstname").send_keys("48.819626")
browser.find_element(By.ID, "field-lastname").send_keys("2.404811")
browser.find_element(By.ID, "field-birthday").send_keys("01/01/1900")
browser.find_element(By.ID, "field-placeofbirth").send_keys("2.404811")
browser.find_element(By.ID, "field-address").send_keys("2.404811")
browser.find_element(By.ID, "field-zipcode").send_keys("75001")
browser.find_element(By.ID, "field-city").send_keys("Paris")
browser.find_element(By.ID, "field-heuresortie").send_keys("02:16")
browser.find_element(By.ID, "checkbox-achats_culturel_cultuel").click()
browser.find_element(By.ID, "generate-btn").click()
