import os
import pathlib

from crontab import CronTab

dir_path = pathlib.Path.cwd()
task_path = pathlib.Path(dir_path, 'schedule.py')
from classes.database import DBManager
from classes.engine_codeforses import EngineCF

params = {'user': os.getenv('USER'),
          'password': os.getenv('PASSWORD'),
          'host': os.getenv('HOST'),
          'port': os.getenv('PORT')}


def check_new_task(name_bd, params):
    engine = EngineCF()
    update_tasks = engine.get_result_data()
    db = DBManager(name_bd, params)
    all_tasks_numbers = db.get_all_numbers_tasks()
    for item in update_tasks:
        if item[0] not in all_tasks_numbers:
            db.single_insert_to_task(item)


my_cron = CronTab(user=True)
job = my_cron.new(command=f'python {task_path}')
job.minute.every(1)

my_cron.write()
