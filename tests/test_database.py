import os
import unittest

from classes.database import DBManager

params = {'user': os.getenv('USER'),
          'password': os.getenv('PASSWORD'),
          'host': os.getenv('HOST'),
          'port': os.getenv('PORT')}


class DBManagerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.db = DBManager('parser_db', params)

    def test_get_all_numbers_tasks(self):
        res = self.db.get_all_numbers_tasks()
        self.assertEqual(res[-1], '1A')

    def test_get_all_theme(self):
        res = self.db.get_all_theme()
        self.assertEqual(res[-1][0], 'dp')

    def test_get_all_rating(self):
        res = self.db.get_all_rating()
        self.assertEqual(res[-1][0], 1400)
