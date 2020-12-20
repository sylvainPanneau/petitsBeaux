from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import time
from time import sleep


print("\n Scanning... \n")
firefox_options =   Options()
firefox_options.add_argument("--headless")
firefox_options.page_load_strategy = 'eager'
browser = webdriver.Firefox(options=firefox_options)

browser.get("https://ent.univ-paris13.fr/applications/notes/")
browser.find_element(By.ID, "username").send_keys("12016045")
browser.find_element(By.ID, "password").send_keys("0114016375T")
browser.find_element(By.ID, "submit").click()
moyenne = browser.find_element_by_class_name('ligneResumeMoyenne').text

def note_loop_check():
    test = True
    keep_checking = "y"
    start = time()
    print("\n Scanning... You will be notified if something comes up ! \n")
    while test and keep_checking=="y":
        moyenne = browser.find_element_by_class_name('ligneResumeMoyenne').text
        test = float(moyenne) == 16.91
        anchor = time()
        if anchor-start > 1200:
            keep_checking = input("Keep scanning for new notes ? (y/n)")
            start = time()
            print("Moyenne :", moyenne)
            print("\n Scanning... \n")
    return test

print("Moyenne :", moyenne)
keep_checking = input("Keep scanning for new notes ? (y/n) : ")
if keep_checking == "y":
    x=note_loop_check()
else:
    quit()
if not x:
    print("Nouvelle note en ligne !")
else:
    print("RAS")