from selenium import webdriver
from selenium.webdriver import Keys
#Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time
import random


def search_wikipedia(query):
    # Открываем браузер и переходим на Википедию
    driver.get("https://ru.wikipedia.org")

    # Находим поле поиска и вводим запрос
    search_box = driver.find_element(By.NAME, "search")
    search_box.clear()
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)


def list_paragraphs():
    # Получаем все параграфы статьи
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, p in enumerate(paragraphs):
        print(f"{i + 1}: {p.text}\n")

    return paragraphs


def get_related_links():
    # Получаем все ссылки на внутренние страницы
    links = driver.find_elements(By.CSS_SELECTOR, "p a[href^='/wiki/']")
    return links


def main():
    global driver
    driver = webdriver.Chrome()  # Убедитесь, что ChromeDriver установлен и доступен в PATH

    try:
        while True:
            query = input("Введите запрос для поиска в Википедии (или 'выход' для завершения): ")
            if query.lower() == 'выход':
                break

            search_wikipedia(query)

            while True:
                # Листаем параграфы статьи
                print("\nВыберите действие:")
                print("1: Листать параграфы статьи")
                print("2: Перейти на одну из связанных страниц")
                print("3: Выйти из программы")

                choice = input("Введите номер действия: ")

                if choice == '1':
                    paragraphs = list_paragraphs()
                    input("Нажмите Enter для продолжения...")  # Задержка для просмотра содержания
                elif choice == '2':
                    links = get_related_links()
                    print("\nСвязанные страницы:")
                    for i, link in enumerate(links):
                        print(f"{i + 1}: {link.text}")
                        link_choice = int(input("Выберите номер страницы для перехода: ")) - 1
                    if 0 <= link_choice < len(links):
                        links[link_choice].click()  # Переходим на выбранную страницу
                    else:
                        print("Неверный выбор. Попробуйте снова.")

                elif choice == '3':
                        print("Выход из программы...")
                return
            else:
                print("Неверный выбор. Попробуйте снова.")
    finally:
        driver.quit()  # Закрываем браузер

if __name__ == "__main__":
    main()