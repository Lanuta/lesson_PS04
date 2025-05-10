import wikipediaapi

# Инициализируем объект Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('ru')

def get_article(query):
    """Получаем статью по запросу."""
    page = wiki_wiki.page(query)
    if not page.exists():
        print(f"Статья с названием '{query}' не найдена.")
        return None
    return page

def list_paragraphs(page):
    """Выводим параграфы статьи."""
    print(f"\nСодержание статьи '{page.title}':")
    for section in page.sections:
        print(f"\n{section.title}:\n{section.text[:200]}...")  # Показываем первые 200 символов параграфа

def search_article():
    """Основная функция игры."""
    while True:
        query = input("\nВведите запрос для поиска в Википедии: ")
        page = get_article(query)

        if page:
            print(f"\nНайдено! Заголовок статьи: {page.title}")
            while True:
                print("\nЧто хотите сделать?")
                print("1. Листать параграфы статьи.")
                print("2. Перейти на одну из связанных страниц.")
                print("3. Выйти из программы.")

                choice = input("Ваш выбор (1/2/3): ")

                if choice == '1':
                    list_paragraphs(page)

                elif choice == '2':
                    print("\nСписок связанных статей:")
                    links = page.links
                    for i, link in enumerate(links):
                        print(f"{i+1}. {link.title}")

                    choice_link = input("\nВыберите номер статьи для перехода или введите 'q' для выхода: ")
                    if choice_link.lower() == 'q':
                        break
                    else:
                        try:
                            link_number = int(choice_link) - 1
                            new_page = links[link_number]
                            page = get_article(new_page.title)
                            if page:
                                print(f"\nПерехожу к статье: {page.title}")
                        except (ValueError, IndexError):
                            print("Неверный ввод, попробуйте снова.")

                elif choice == '3':
                    print("Выход из программы. Спасибо за игру!")
                    return
                else:
                    print("Некорректный выбор, попробуйте снова.")

# Запуск программы
search_article()