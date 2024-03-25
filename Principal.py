from selenium import webdriver
from selenium.webdriver.common.by import By


objSelenium = webdriver.Edge()
def AbreSite():
    objSelenium.get('https://www.bet365.com')


def NavegaSite():
    objSelenium.fullscreen_window()
    objSelenium.find_element(By.XPATH('/html/body/div[1]/div/div[3]/div[2]/div/div[4]/div[5]/div[2]')).click()


    AbreSite()
    NavegaSite()

