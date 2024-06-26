from bs4 import BeautifulSoup
import pandas as pd
import os
# Функция для обработки одного HTML файла и сохранения в Excel
def process_html_to_excel(html_filename, output_directory):
    if not os.path.exists(html_filename):
        print(f"HTML файл '{html_filename}' не найден.")
        return False

    with open(html_filename, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Парсим HTML контент
    soup = BeautifulSoup(html_content, 'html.parser')
    feedback_items = soup.find_all('div', class_='feedbacks-item-product')

    feedbacks = []

    for item in feedback_items:
        stars = 0
        stars_elements = item.find_all('svg', class_='icon-star')
        
        for star in stars_elements:
            if 'disabled' not in star.get('class', []):
                stars += 1
        
        date = item.find('span', {'data-tag': 'date'}).text.strip()
        text = item.find('span', {'data-tag': 'text'}).text.strip()
        
        feedbacks.append({
            'stars': stars,
            'date': date,
            'text': text
        })

    # Создаем DataFrame из списка отзывов
    df = pd.DataFrame(feedbacks)

    # Извлекаем часть имени файла без расширения для создания имени Excel файла
    filename_base = os.path.splitext(os.path.basename(html_filename))[0]
    xlsx_filename = os.path.join(output_directory, f'{filename_base}.xlsx')

    # Сохраняем DataFrame в XLSX файл
    with pd.ExcelWriter(xlsx_filename, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)

    print(f"Отзывы из файла '{html_filename}' успешно сохранены в файл {xlsx_filename}")
    return True

# Основной код для обработки всех HTML файлов из директории
html_files_directory = 'Html_отзывы'  # Путь к директории с HTML файлами
output_directory = 'Отзывы'  # Путь к директории для сохранения Excel файлов

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Создана директория: {output_directory}")
# Получаем список всех HTML файлов в указанной директории
html_files = [os.path.join(html_files_directory, f) for f in os.listdir(html_files_directory) if f.endswith('.html')]

for html_file in html_files:
    process_html_to_excel(html_file, output_directory)
