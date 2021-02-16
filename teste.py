from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests


driver = webdriver.Chrome()

def wait_loading():
    while True:
        try:
            driver.find_element_by_id('ng-app')
        except:
            break
        

    

driver.get('https://gshow.globo.com/realities/bbb/bbb21/votacao/paredao-bbb21-vote-para-eliminar-fiuk-nego-di-ou-sarah-fc1cc356-3a7d-452f-9d55-50e4f0902e54.ghtml')
driver.find_element_by_id('barra-item-login').click()
driver.find_element_by_name('login').send_keys('brunoferreira.tecnico@gmail.com')
driver.find_element_by_name('password').send_keys('brunorock')
driver.find_element_by_class_name('button').click()

wait_loading()



driver.find_elements_by_xpath("//*[contains(text(), 'Nego Di')]")
driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[4]/div/div[5]/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div/div/div').click()
driver.find_element_by_id('anchor').click()
driver.find_element_by_xpath('//*[@id="roulette-root"]/div/div[9]/div/div/div[1]/div[2]/button').click()
print('')