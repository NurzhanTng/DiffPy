import pandas as pd
from pathlib import Path

xlsx_file = '21.06.xlsx'
df = pd.read_excel(xlsx_file)
file_date = '21.06.csv'
df.to_csv(file_date, index=False)

# Пути к файлам
file_date = '21.06.csv'
file_rf = 'рф.csv'
output_file = 'Результат.csv'
df_16_06 = pd.read_csv(file_date)
df_rf = pd.read_csv(file_rf)

# Извлечение даты из имени файла 
file_date = Path(file_date).stem  
# Объединение данных по столбцу 'Col0' и 'Филиал'
merged_df = pd.merge(df_16_06, df_rf, left_on='Col0', right_on='Филиал', how='inner')
# Добавляем столбец с датой
merged_df['Дата'] = file_date

# Переупорядочиваем столбцы и переименовываем 'Col5' в 'Рейтинг'
merged_df = merged_df[['Дата', 'Филиал', 'Рф', 'Col5']]
merged_df.rename(columns={'Col5': 'Рейтинг'}, inplace=True)

# Добавляем данные в конец файла merged_data2.csv без заголовков столбцов
merged_df.to_csv(output_file, mode='a', header= False,index=False)
df = pd.read_csv(output_file)

df.to_excel('Результат.xlsx', index=False, engine='openpyxl')
