from clickhouse_driver import Client

client = Client('localhost', port=8123)  # Порт 8123 для HTTP-интерфейса

csv_file = 'C:/Users/annav/OneDrive/Desktop/client_server_interaction/HW3/books_data.csv'

# Запрос на загрузку данных из CSV файла во временную таблицу
load_data_query = f'''
    INSERT INTO temp_books
    FORMAT CSVWithNames
    FROM '{csv_file}'
'''

client.execute(load_data_query)

# Запрос для проверки загруженных данных (можно закомментировать после проверки)
select_query = '''
    SELECT * FROM temp_books LIMIT 10
'''

# Выполнение запроса на выборку данных для проверки (можно закомментировать после проверки)
result = client.execute(select_query)
print(result)

# Закрытие соединения с ClickHouse
client.disconnect()
