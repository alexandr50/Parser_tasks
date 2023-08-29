import requests

from utils import get_correct_data
#
# url = 'https://codeforces.com/api/problemset.problems'
#
# response = requests.get(url)
# print(response.json())
# for i, item in enumerate(response.json()['result']['problems']):
#     print(i, item)
# for i, item in enumerate(response.json()['result']):
#     print(i, item)

class EngineCF:

    URL = 'https://codeforces.com/api/problemset.problems'


    def get_request_for_problems(self) -> dict:
        response = requests.get(self.URL)
        return response.json()['result']['problems']

    def get_request_for_problemstatistic(self) -> dict:
        response = requests.get(self.URL)
        return response.json()['result']['problemStatistics']

    def get_content_from_problems(self, content: dict) -> list:
        number = f"{content.get('contestId')}{content.get('index')}"
        name = content.get('name')
        theme = content.get('tags')

        return [number, name, theme]

    def get_content_from_problemstatistic(self, content: dict) -> list:
        count_solutions = content.get('solvedCount')
        number = f"{content.get('contestId')}{content.get('index')}"
        return [number, count_solutions]

    def get_result_data(self):
        result_data_from_problems = []
        result_data_from_problemstatistics = []
        for item in self.get_request_for_problems():
            result_data_from_problems.append(self.get_content_from_problems(item))
        for item in self.get_request_for_problemstatistic():
            result_data_from_problemstatistics.append(self.get_content_from_problemstatistic(item))
        data = get_correct_data(result_data_from_problems, result_data_from_problemstatistics)
        return data
#
# e = EngineCF()
# print(e.get_result_data())




