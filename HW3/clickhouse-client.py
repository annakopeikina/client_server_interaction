import clickhouse_connect
import csv

client = clickhouse_connect.get_client(host='localhost', port=8123)

# Создаем временную таблицу
create_table_query = """
CREATE TEMPORARY TABLE IF NOT EXISTS temp_books
(
    category String,
    title String,
    price Float32,
    availability UInt32,
    description String
) ENGINE = Memory
"""

client.command(create_table_query)

# Открываем CSV файл
with open('C:/Users/annav/OneDrive/Desktop/client_server_interaction/books_data.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    # Пропускаем заголовок
    next(csv_reader)
    
    for row in csv_reader:
        category, title, price, availability, description = row
        
        # Экранируем апострофы в строке title
        title = title.replace("'", "''")
        
        # Вставляем данные в ClickHouse
        query = f"""
        INSERT INTO temp_books (category, title, price, availability, description)
        VALUES ('{category}', '{title}', {float(price)}, {int(availability)}, '{description}')
        """
        client.command(query)

