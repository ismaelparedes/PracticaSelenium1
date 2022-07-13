from selenium import webdriver as navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

webSite = 'https://www.adamchoi.co.uk/teamgoals/detailed'

driver = navegador.Edge()
driver.maximize_window()
driver.get(webSite)

all_matches = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches.click()

selectCountry = Select(driver.find_element(By.ID,'country'))
selectCountry.select_by_visible_text('Spain')

valores = driver.find_elements(By.TAG_NAME,'tr')

for valor in valores:
    print(valor.text)
#coemntario