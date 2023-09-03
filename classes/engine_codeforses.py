import requests

from utils import get_correct_data, get_random_theme


class EngineCF:
    URL = 'https://codeforces.com/api/problemset.problems'

    def get_request_for_problems(self) -> dict:
        """Возвращает данные по ключу problems"""

        response = requests.get(self.URL)
        return response.json()['result']['problems']

    def get_check_new_task(self):
        """Возвращает все уникальные номера задач"""

        lst = []
        response = self.get_request_for_problems()
        for item in response:
            number = f"{item.get('contestId')}{item.get('index')}"
            lst.append(number)
        return lst

    def get_request_for_problemstatistic(self) -> dict:
        """Возвращает данные по ключу problemStatistics"""

        response = requests.get(self.URL)
        return response.json()['result']['problemStatistics']

    def get_content_from_problems(self, content: dict) -> list:
        """Возвращает данные в списке по одной задаче  по ключу problems"""

        number = f"{content.get('contestId')}{content.get('index')}"
        name = content.get('name')
        rating = content.get('rating')
        if rating == None:
            rating = 0
        theme = content.get('tags')
        if len(theme) > 1:
            theme = [get_random_theme(theme)]
        elif len(theme) == 0:
            theme = ['No theme']

        return [number, name, theme[0], rating]

    def get_content_from_problemstatistic(self, content: dict) -> list:
        """Возвращает данные в списке по одной задаче  по ключу problemStatistics"""

        count_solutions = content.get('solvedCount')
        number = f"{content.get('contestId')}{content.get('index')}"
        return [number, count_solutions]

    def get_result_data(self):
        """Возвращает список кортежей задач для записи в бд"""
        result_data_from_problems = []
        result_data_from_problemstatistics = []
        for item in self.get_request_for_problems():
            result_data_from_problems.append(self.get_content_from_problems(item))
        for item in self.get_request_for_problemstatistic():
            result_data_from_problemstatistics.append(self.get_content_from_problemstatistic(item))
        data = get_correct_data(result_data_from_problems, result_data_from_problemstatistics)
        return list(map(lambda x: tuple(x), data))

e = EngineCF()
print(e.get_request_for_problems())