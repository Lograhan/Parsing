from data.file_manager import File_manager
from data.abs_class import Api
import requests


class HH_api(Api, File_manager):
    """
    Класс для работы с HH.ru. В атрибут принимает желаемую профессию.
    """
    def __init__(self, keyword, page=0):
        self.par = {
            'text': keyword,
            'page': page}

    def get_api(self):
        """
        Метод для получения списка вакансий.
        Возвращает отсортированный список, в котором исключены вакансии без ЗП, и в качестве валюты указаны RUR
        """
        data = requests.get('https://api.hh.ru/vacancies', self.par).json()
        all_vac = []
        for i in data['items']:
            if i['salary'] != None:
                if i['salary']['currency'] == 'RUR':
                    all_vac.append(i)
        for i in all_vac:  # Замена значения зп None на 0 для адекватной фильтрации. Можно переделать через Try/Except.
            if i['salary']['from'] is None:
                i['salary']['from'] = 0

        all_vac.sort(key=lambda x: x['salary']['from'], reverse=True)
        return all_vac



# def name(self):
#     self.name = HH_api.get_api(self)['items'][0]['name']  # наименование вакансии
#     return self.name
#
# def id(self):
#     self.id = HH_api.get_api(self)['items'][0]['id']  # id вакансии
#     return self.id
#
# def url(self):
#     self.url = f'http://hh.ru/vacancy/{self.id}?from=main'  # ссылка на вакансию
#     return self.url
#
# def zp(self):
#     self.zp = HH_api.get_api(self)['items'][0]['salary']  # зарплата
#     return self.zp
#
# def responsibilities(self):
#     self.responsibilities = HH_api.get_api(self)['items'][0]['snippet']["responsibility"]  # обязанности
#     return self.responsibilities
#
# def requirements(self):
#     self.requirements = HH_api.get_api(self)['items'][0]['snippet']['requirement']  # требования
#     return self.requirements
