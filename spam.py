from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import ActionChains


driver=webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
time.sleep(15)
def sender():
    
    xp="//span[@title='Harshit']" #Xpath is soo nice to use  #syntax==>  //tagname[@attribute='value']
    base=driver.find_element_by_xpath(xp)
    base.click()
    time.sleep(20)
sender()
def message(msgTXT):
    txt=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
    txt.send_keys(msgTXT+Keys.RETURN)
    time.sleep(2)
# for i in range(20):
#     message("this is a script "+str(i))
    
