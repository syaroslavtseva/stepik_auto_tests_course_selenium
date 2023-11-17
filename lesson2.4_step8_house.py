from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
try:
#Открыть страницу
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
#Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)    
    price = WebDriverWait(browser, 12).until(
EC.text_to_be_present_in_element((By.ID, "price"),'$100')
)
#Нажать на кнопку    
    button1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button1.click()
    
    
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
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
