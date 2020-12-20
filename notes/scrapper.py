from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import time


firefox_options =   Options()
firefox_options.add_argument("--headless")
firefox_options.page_load_strategy = 'none'
browser = webdriver.Firefox(options=firefox_options)

browser.get("https://ent.univ-paris13.fr/applications/notes/")
browser.find_element(By.ID, "username").send_keys("12016045")
browser.find_element(By.ID, "password").send_keys("0114016375T")
browser.find_element(By.ID, "submit").click()
moyenne = browser.find_element_by_class_name('ligneResumeMoyenne').text

def note_loop_check():
    test = True
    moyenne = browser.find_element_by_class_name('ligneResumeMoyenne').text
    keep_checking = "y"
    i=0
    start = time()
    while test and keep_checking=="y":
        test = float(moyenne) == 16.91
        i+=1
        anchor = time()
        if anchor-start > 1200:
            keep_checking = input("Keep scanning for new notes ? (y/n)")
            start = time()
            print(moyenne)
    return test

print(moyenne)
x=note_loop_check()
if not x:
    print("Nouvelle note en ligne !")
else:
    print("RAS")

