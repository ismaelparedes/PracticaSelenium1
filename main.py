from selenium import webdriver as navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import  pandas as pd
import  time as tiempo

webSite = 'https://www.adamchoi.co.uk/teamgoals/detailed'

driver = navegador.Edge()
driver.maximize_window()
driver.get(webSite)

all_matches = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches.click()

selectCountry = Select(driver.find_element(By.ID,'country'))
selectCountry.select_by_visible_text('Spain')

tiempo.sleep(6)

valores = driver.find_elements(By.TAG_NAME,'tr')

partidos = []

for valor in valores:
    partidos.append(valor.text)

driver.quit()

#Pandas
df = pd.DataFrame({'Partidos':partidos})
print(df)
df.to_csv('Pandas.csv', index=False)