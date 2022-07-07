from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import ActionChains


driver=webdriver.Firefox()
driver.install_addon(r"C:\Users\admin\AppData\Roaming\Mozilla\Firefox\Profiles\lqbohnwq.default-release\extensions\uBlock0@raymondhill.net.xpi", temporary=True)

driver.get("https://mangakakalot.com/chapter/jp921012/chapter_3") #link for manga ch1 or anything
body=driver.find_element_by_css_selector("body")
def scroller():
    global body
    for i in range(28):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
def navigator():
    global body
    scroller()
    next=driver.find_element_by_class_name("back") #for manganelo==navi-change-chapter-btn-next.a-h   #for mangakakalot=="back" for next ch soo fkn stupid
    next.click()
    time.sleep(2)
    print(driver.current_url)
    driver.get(driver.current_url)
    time.sleep(3)
    body=driver.find_element_by_css_selector("body")


for i in range(100):
    navigator()
