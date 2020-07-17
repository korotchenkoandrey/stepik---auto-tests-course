from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):

  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector("#input_value")
    x = element1.text
    y = calc(x)
    element2 = browser.find_element_by_id("answer")
    element2.send_keys(y)
    element3 = browser.find_element_by_id("robotCheckbox")
    element3.click()
    element4 = browser.find_element_by_id("robotsRule")
    element4.click()
    element5 = browser.find_element_by_class_name("btn.btn-default")
    element5.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла