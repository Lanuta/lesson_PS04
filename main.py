from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Запускаем браузер в фоновом режиме (без GUI)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def search_wikipedia(driver, query):
    driver.get(f"https://ru.wikipedia.org/wiki/{query}")
    time.sleep(2)  # Ждем загрузки страницы

    try:
        title = driver.find_element(By.ID, "firstHeading").text
        print(f"Заголовок: {title}")
    except Exception as e:
        print("Не удалось найти статью.")
        return None

    return title

def list_paragraphs(driver):
    paragraphs = driver.find_elements(By.CSS_SELECTOR, "p")
    for i, para in enumerate(paragraphs):
        print(f"{i + 1}: {para.text}\n")

def get_related_links(driver):
    links = driver.find_elements(By.CSS_SELECTOR, "#bodyContent a[href^='/wiki/']")
    return [link for link in links if link.text]

def main():
    driver = setup_driver()
    while True:
        query = input("Введите запрос для поиска на Википедии (или 'exit' для выхода): ")
        if query.lower() == 'exit':
            break

        search_wikipedia(driver, query)

        while True:
            print("\nВыберите действие:")
            print("1: Листать параграфы статьи")
            print("2: Перейти на одну из связанных страниц")
            print("3: Выйти из программы")

            choice = input("Ваш выбор: ")
            if choice == '1':
                list_paragraphs(driver)
                elif choice == '2':
                related_links = get_related_links(driver)
                if not related_links:
                    print("Нет связанных страниц.")
                    continue
                print("\nСвязанные страницы:")
                for i, link in enumerate(related_links):
                    print(f"{i + 1}: {link.text}")

                related_choice = int(input("Выберите номер страницы для перехода: ")) - 1
                if 0 <= related_choice < len(related_links):
                    related_link = related_links[related_choice].get_attribute('href').split('/')[-1]
                    search_wikipedia(driver, related_link)
                else:
                    print("Некорректный выбор.")
            elif choice == '3':
                driver.quit()
                return
            else:
                print("Некорректный выбор.")

            if __name__ == "__main__":
                main()