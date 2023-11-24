from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest

def answer():
        return str(math.log(int(time.time())))
        
        
@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, page):
#открыть в Chrome урок по ссылке    
    link = f"https://stepik.org/lesson/{page}/step/1"
    browser.get(link)
    input = browser.find_element(By.CLASS_NAME, "navbar__auth_login").click()
    
#авторизоваться со своими логином и паролем    
    login = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="login"]'))
    )
    login.send_keys("111")
    password = browser.find_element(By.NAME, "password")
    password.send_keys("111")
# Отправляем заполненную форму
    button1 = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    button1.click()
#ввести правильный ответ
    time.sleep(10)
    #cleaning = browser.find_element(By.CLASS_NAME, "again-btn").click()
    
    input1 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
    )
    
    y = answer()
    input1.send_keys(str(y))
 # Отправляем ответ
    button2 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button2.click()   
    
    #feedback
    # находим элемент, содержащий текст
    feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
     # записываем в переменную feedback_text текст из элемента 
    feedback_text = feedback.text
    assert "Correct!" == feedback_text
    
