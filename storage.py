from abc import ABC, abstractmethod
import os
import sqlite3
from data_extractor import DataExtractor

class Storage(ABC):
    @abstractmethod
    def save_data(self, data_extractor: DataExtractor, file_path: str):
        pass

class FileStorage(Storage):
    def save_data(self, data_extractor: DataExtractor, file_path: str):
        text = data_extractor.extract_text(file_path)
        os.makedirs('output', exist_ok=True)
        with open('output/text.txt', 'w', encoding='utf-8') as file:
            file.write(text)

        images = data_extractor.extract_images(file_path)
        for idx, image in enumerate(images):
            with open(f'output/image_{idx}.png', 'wb') as img_file:
                img_file.write(image)

class SQLStorage(Storage):
    def save_data(self, data_extractor: DataExtractor, file_path: str):
        conn = sqlite3.connect('output/data.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS text_data (content TEXT)''')
        text = data_extractor.extract_text(file_path)
        cursor.execute('''INSERT INTO text_data (content) VALUES (?)''', (text,))

        cursor.execute('''CREATE TABLE IF NOT EXISTS links (text TEXT, url TEXT)''')
        links = data_extractor.extract_links(file_path)
        for link_text, url in links:
            cursor.execute('''INSERT INTO links (text, url) VALUES (?, ?)''', (link_text, url))

        cursor.execute('''CREATE TABLE IF NOT EXISTS tables (table_data TEXT)''')
        tables = data_extractor.extract_tables(file_path)
        for table in tables:
            table_data = str(table)
            cursor.execute('''INSERT INTO tables (table_data) VALUES (?)''', (table_data,))

        conn.commit()
        conn.close()
