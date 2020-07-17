from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_id("num1")
    element2 = browser.find_element_by_id("num2")
    summa = int(element1.text) + int(element2.text)
    summatext = str(summa)
    element3 = browser.find_element_by_id("dropdown")
    element3.click()
    element4 = browser.find_element_by_css_selector(f"[value='{str(summa)}']")
    #element4 = Select(browser.find_element_by_tag_name("select"))
    #element4.select_by_visible_text(summatext)  # ищем элемент с текстом "Python"
    element4.click()
    element5 = browser.find_element_by_tag_name("button")
    element5.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла