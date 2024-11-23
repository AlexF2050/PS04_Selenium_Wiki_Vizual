# похожим примером можно автоматизировать регистрацию на сайтах

from selenium import webdriver
from selenium.webdriver import Keys # для ввода текста с клавиатуры
from selenium.webdriver.common.by import By # поиск элементов
import time

browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0')
# проверяем наличие элемента
assert 'Википедия' in browser.title
time.sleep(3)
search_box = browser.find_element(By.ID, 'searchInput')
search_box.send_keys('Солнечная система')
search_box.send_keys(Keys.RETURN)
time.sleep(5)

a = browser.find_element(By.LINK_TEXT, 'Солнечная система')
a.click()



