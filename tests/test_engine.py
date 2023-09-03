import pathlib
import unittest

from classes.engine_codeforses import EngineCF

dir_path = pathlib.Path.cwd()
path = pathlib.Path(dir_path, 'tests/get_request_for_problems.json')


class EngineCFTest(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = EngineCF()
        self.res_problem = self.engine.get_request_for_problems()
        self.res_problemstatistic = self.engine.get_request_for_problemstatistic()

    def test_get_request_for_problems(self):
        self.assertEqual(self.res_problem[-1]["contestId"], 1)
        self.assertEqual(self.res_problem[-1]['tags'], ["math"])

    def test_get_request_for_problemstatistic(self):
        self.assertEqual(self.res_problemstatistic[-1]['contestId'], 1)
        self.assertEqual(self.res_problemstatistic[-1]['index'], 'A')

    def test_get_result_data(self):
        res = self.engine.get_result_data()
        print(res)
        self.assertEqual(res[-1][0], '1A')
        self.assertEqual(res[-1][1], 'Theatre Square')
