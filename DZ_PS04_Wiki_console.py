# Напишите программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Настройка webdriver Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме, без GUI
chrome_service = Service()  # Убедитесь, что у вас есть установленный драйвер Chrome в PATH

def get_paragraphs(url):
    # Переход на страницу и получение параграфов
    driver.get(url)
    time.sleep(2)  # Ждем загрузки страницы
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    paragraphs = soup.find_all('p')
    return paragraphs

def main():
    global driver
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    while True:
        query = input("Введите название статьи для поиска (или 'exit' для выхода): ")
        if query.lower() == 'exit':
            break

        # Поиск статьи на Википедии
        search_url = f"https://ru.wikipedia.org/w/index.php?search={query}"
        driver.get(search_url)
        time.sleep(2)

        # Получение первых результатов поиска
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', class_='mw-search-result-heading')

        if not results:
            print("Ничего не найдено!")
            continue

        print("Найденные статьи:")
        links = []
        for i, result in enumerate(results[:5]):  # Показываем только первые 5 результатов
            title = result.find('a').text
            link = "https://ru.wikipedia.org" + result.find('a')['href']
            links.append(link)
            print(f"{i + 1}. {title}")

        choice = int(input("Выберите номер статьи для просмотра (или 0 для выхода): ")) - 1
        if choice == -1:
            break

        current_url = links[choice]
        while True:
            paragraphs = get_paragraphs(current_url)
            for i, paragraph in enumerate(paragraphs):
                print(f"Параграф {i + 1}: {paragraph.text.strip()}")

            print("\nДействия:")
            print("1. Листать параграфы статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выход")

            action = input("Выберите действие (1-3): ")
            if action == '1':
                continue
            elif action == '2':
                related_links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/wiki/"]')
                print("Связанные статьи:")
                links = []
                for i, link in enumerate(related_links[:5]):  # Показываем только первые 5 связанных
                    title = link.text
                    full_link = "https://ru.wikipedia.org" + link.get_attribute('href')
                    links.append(full_link)
                    print(f"{i + 1}. {title}")

                choice = int(input("Выберите номер связанной статьи для просмотра (или 0 для выхода): ")) - 1
                if choice == -1:
                    break
                current_url = links[choice]
            elif action == '3':
                break

    driver.quit()

if __name__ == "__main__":
    main()