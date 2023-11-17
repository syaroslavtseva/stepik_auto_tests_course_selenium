from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
try:
#Открыть страницу
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
#Нажать на кнопку    
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
#Переключиться на новую вкладку   http://suninjuly.github.io/redirect_page.html?
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
#Пройти капчу для робота и получить число-ответ
#Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#Посчитать математическую функцию от x
    x = x_element.text
    y = calc(x)
#Ввести ответ в текстовое поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y) 
#Submit    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
