import os

from classes.database import DBManager
from classes.engine_codeforses import EngineCF


params = {'user': os.getenv('USER'),
          'password': os.getenv('PASSWORD'),
          'host': os.getenv('HOST'),
          'port': os.getenv('PORT')}


def run():
    db = DBManager('parser_db', params)
    db.create_database()
    e = EngineCF()
    result = e.get_result_data()
    db.insert_to_tasks(result)

    os.system(f'python {os.getcwd()}/bot/telegram_bot.py')


if __name__ == '__main__':
    run()
