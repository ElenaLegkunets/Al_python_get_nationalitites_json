import sqlite3
conn = sqlite3.connect('my.db')
#Если такой базы нет, то она создается автоматически. Расширение базы можете ставить и такое my.sqlite. Чтобы подключиться к базе через SQLite Manager, нужно просто указать где она лежит.
#Сейчас я покажу код создания базы данных и таблиц, но лучше делать это через SQLite Manager.

# -*- coding: utf-8 -*-
import sqlite3
#Подключение к базе
conn = sqlite3.connect('my.sqlite')
#Создание курсора
c = conn.cursor()
#Создание таблицы
c.execute('''CREATE TABLE users (id int auto_increment primary key,name varchar, password varchar)''')
#Наполнение таблицы
c.execute("INSERT INTO users (name,password) VALUES ('admin','123')")
#Подтверждение отправки данных в базу
conn.commit()
#Завершение соединения
c.close()
conn.close()
