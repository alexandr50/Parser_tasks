import requests

from utils import get_correct_data, get_random_theme


class EngineCF:
    URL = 'https://codeforces.com/api/problemset.problems'

    def get_request_for_problems(self) -> dict:
        response = requests.get(self.URL)
        return response.json()['result']['problems']

    def get_check_new_task(self):
        lst = []
        response = self.get_request_for_problems()
        for item in response:
            number = f"{item.get('contestId')}{item.get('index')}"
            lst.append(number)
        return lst

    def get_request_for_problemstatistic(self) -> dict:
        response = requests.get(self.URL)
        return response.json()['result']['problemStatistics']

    def get_content_from_problems(self, content: dict) -> list:
        number = f"{content.get('contestId')}{content.get('index')}"
        name = content.get('name')
        rating = content.get('rating')
        theme = content.get('tags')
        if len(theme) > 1:
            theme = [get_random_theme(theme)]
        elif len(theme) == 0:
            theme = ['No theme']

        return [number, name, theme[0], rating]

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
        return list(map(lambda x: tuple(x), data))
