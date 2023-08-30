import os

import psycopg2


class DBManager:

    def __init__(self, name_bd: str, params: dict):
        self.name_db = name_bd
        self.params = params

    def create_database(self):
        """Метод создания базы данных и одной таблицы"""
        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True

        with conn.cursor() as cur:
            cur.execute(f"""DROP DATABASE IF EXISTS {self.name_db}""")
            cur.execute(f"""CREATE DATABASE {self.name_db}""")

        with psycopg2.connect(dbname=self.name_db, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""CREATE TABLE IF NOT EXISTS tasks (
                                    task_id INT PRIMARY KEY,
                                    number VARCHAR(10) UNIQUE NOT NULL,
                                    name VARCHAR(50),
                                    theme VARCHAR(20),
                                    rating INT,
                                    count_solutions INT);
                                """)
# params =  {'user': os.getenv('USER'),
#            'password': os.getenv('PASSWORD'),
#            'host': os.getenv('HOST'),
#             'port': os.getenv('POSRT')}
# db = DBManager('parser_db', params)
# db.create_database()