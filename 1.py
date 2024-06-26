from bs4 import BeautifulSoup
import pandas as pd
import os

# Открываем сохраненный HTML файл
html_filename = 'Баймагамбетова, д. 183.html'

if not os.path.exists(html_filename):
    print(f"HTML файл '{html_filename}' не найден.")
    exit(1)

with open(html_filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Парсим HTML контент
soup = BeautifulSoup(html_content, 'html.parser')
feedback_items = soup.find_all('div', class_='feedbacks-item-product')

feedbacks = []

for item in feedback_items:
    stars = len(item.find_all('svg', class_='icon-star'))
    date = item.find('span', {'data-tag': 'date'}).text.strip()
    text = item.find('span', {'data-tag': 'text'}).text.strip()
    
    feedbacks.append({
        'stars': stars,
        'date': date,
        'text': text
    })

# Создаем DataFrame из списка отзывов
df = pd.DataFrame(feedbacks)

# Убедимся, что директория для сохранения файла существует
output_directory = 'Отзывы_Костанайская55'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print(f"Создана директория: {output_directory}")

# Сохраняем DataFrame в XLSX файл
xlsx_filename = os.path.join(output_directory, '2.xlsx')

with pd.ExcelWriter(xlsx_filename, engine='openpyxl') as writer:
    df.to_excel(writer, index=False)

print(f"Отзывы успешно сохранены в файл {xlsx_filename}")
