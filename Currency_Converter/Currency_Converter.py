# supports most of the conversions
# to be updated..

import os.path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas
import time
import csv
order = 1
current_time = time.ctime()

# Function(s)
def currency_applier(currency):
    global order
    if order == 1:
        currency_box = driver.find_element('xpath','//*[@id="midmarketFromCurrency"]/div[2]/div/input')
        currency_box.click()
        currency_box.send_keys(currency+Keys.ENTER)
        order += 1
    elif order == 2:
        currency_box = driver.find_element('xpath','//*[@id="midmarketToCurrency"]/div[2]/div/input')
        currency_box.click()
        currency_box.send_keys(currency+Keys.ENTER)


first_currency = input('Please enter the first currency:')
second_currency = input('Please enter the second currency:')
amount = int(input('Please enter the amount of first currency:'))
driver = webdriver.Chrome()
driver.get('https://www.xe.com/currencyconverter/')

# Wait until page loads
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(('xpath', '//*[@id="__next"]/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[1]/div[1]'))
)

# Entering values
input_box = driver.find_element('xpath','//*[@id="amount"]')
input_box.click()
input_box.send_keys(amount)
currency_applier(first_currency)
currency_applier(second_currency)

driver.find_element('xpath','//*[@id="__next"]/div[4]/div[2]/section/div[2]/div/main/div/div[2]/div[2]/button').click()

# Wait until new page loads
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(('xpath', '//*[@id="__next"]/div[4]/div[2]/section/div[2]/div/main/div[2]/div[2]/div[1]/p[2]'))
)

conversion = driver.find_element('xpath', '//*[@id="__next"]/div[4]/div[2]/section/div[2]/div/main/div[2]/div[2]/div[1]/p[2]').text
print(conversion) # prints the result of conversion to console, not really necessary

time.sleep(1) # waits for 1 secs

if not os.path.exists(r'C:\Users\Mraz1\OneDrive\Desktop\Python Projects\Live_Currency_Conversion\Currency_Converter\currency_data.csv'):
    data = pandas.DataFrame({'Time': [current_time], 'Amount': [amount], 'From': [first_currency], 'To': [second_currency], 'Conversion': [conversion]})
    data.to_csv('currency_data.csv', index=False)
else:
    file = open('currency_data.csv', 'a')
    csvwriter = csv.writer(file)
    data = [current_time, amount, first_currency, second_currency, conversion.strip('"')]
    csvwriter.writerow(data)



