from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  
  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  # говорим Selenium проверять в течение n секунд, пока кнопка не станет кликабельной
  price = WebDriverWait(browser, 12).until(
          EC.text_to_be_present_in_element((By.ID, "price"), "100"))
  button1 = browser.find_element(By.ID, "book")
  button1.click()

  x_element = browser.find_element(By.CSS_SELECTOR, "label span:nth-child(2)")
  x = x_element.text
  y = calc(x)

  answer = browser.find_element(By.ID, "answer")
  answer.send_keys(y)

  button2 = browser.find_element(By.ID, "solve").click()

finally:
  time.sleep(10)
  browser.quit()