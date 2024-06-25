import pandas as pd
from pathlib import Path

# Путь к текущему объединенному файлу
merged_file = 'merged_data.csv'

# Путь к новому файлу для добавления
new_file = '15.06.csv'

# Чтение текущего объединенного файла, если он существует
if Path(merged_file).is_file():
    merged_df = pd.read_csv(merged_file)
else:
    merged_df = pd.DataFrame()

# Чтение нового файла
new_df = pd.read_csv(new_file)

# Извлечение даты из имени нового файла (например, '15.06')
file_date = Path(new_file).stem

# Добавление столбца с датой (если такой столбец уже есть, он будет перезаписан)
new_df['Дата'] = file_date

# Объединение данных нового файла с текущим DataFrame
merged_df = pd.concat([merged_df, new_df], ignore_index=True)

# Сохраняем результат в новый CSV файл
merged_df.to_csv(merged_file, index=False)

print(f'Данные из файла {new_file} добавлены и сохранены в файл {merged_file}')
