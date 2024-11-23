# paragraphs

from selenium import webdriver
from selenium.webdriver import Keys # для ввода текста с клавиатуры
from selenium.webdriver.common.by import By # поиск элементов
import time
import random

browser = webdriver.Chrome()
browser.get('https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0#%D0%A1%D0%BE%D0%BB%D0%BD%D1%86%D0%B5')

hatnotes = []

for element in browser.find_elements(By.TAG_NAME,'div'):
    cl = element.get_attribute('class')
    if cl == 'hatnote navigation-not-searchable':
        hatnotes.append(element.text)

print(hatnotes)
hatnote = random.choice(hatnotes)
link = hatnote.find_element(By.TAG_NAME,'a').get_attribute('href')
browser.get(link)


