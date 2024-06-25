import pandas as pd
from pathlib import Path

# Пути к файлам
file_14_06 = '16.06.csv'
file_rf = 'рф.csv'

# Чтение CSV файлов
df_14_06 = pd.read_csv(file_14_06)
df_rf = pd.read_csv(file_rf)

# Извлечение даты из имени файла 14.06.csv
file_date = Path(file_14_06).stem  # Это даст нам '14.06'

# Объединение данных по столбцу 'Col0' и 'Филиал'
merged_df = pd.merge(df_14_06, df_rf, left_on='Col0', right_on='Филиал', how='inner')

# Добавляем столбец с датой
merged_df['Дата'] = file_date

 #Переупорядочиваем столбцы и переименовываем 'Col5' в 'Рейтинг'
merged_df = merged_df[['Дата', 'Филиал', 'Рф', 'Col5']]
merged_df.rename(columns={ 'Col5': 'Рейтинг'}, inplace=True)

# Сохраняем результат в новый CSV файл
output_file = 'merged_data2.csv'
merged_df.to_csv(output_file, index=False)

print(f'Данные объединены и сохранены в файл {output_file}')
