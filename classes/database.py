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
                                    number VARCHAR(10) UNIQUE NOT NULL,
                                    name VARCHAR(100),
                                    theme VARCHAR(100),
                                    rating INT,
                                    count_solutions INT);
                                """)

    def insert_to_tasks(self, data: list):
        """Метод внесения данных в таблицу employers"""
        with psycopg2.connect(dbname=self.name_db, **self.params) as conn:
            with conn.cursor() as cur:
                cur.executemany(f"""INSERT INTO tasks (number, name, theme, rating, count_solutions)
                                VALUES(%s, %s, %s, %s, %s)""", data)

    def get_all_numbers_tasks(self):
        with psycopg2.connect(dbname=self.name_db, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""SELECT number from tasks""")
                result = cur.fetchall()
        return list(map(lambda x: x[0], result))

    def single_insert_to_task(self, data: tuple):
        with psycopg2.connect(dbname=self.name_db, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""INSERT into tasks (number, name, theme, rating, count_solutions)
                            VALUES(%s, %s, %s, %s, %s)""", data)
