from data.file_manager import File_manager
from data.abs_class import Api
import requests


class SuperJ(Api, File_manager):
    """
    Класс для работы с Api SuperJob.ru. В атрибут принимает желаемую профессию.
    """
    def __init__(self, keyword, page=1):
        self.par = {
            'keywords': keyword,
            'page': page}
        self.headers = {
            'X-Api-App-Id': 'v3.r.115217111.f35c58645f2a860b45ea7e6eb703f4d594d8a883.25e952936abc3c0666afbeb30b5db4f05a3c172e'}

    def get_api(self):
        """
        Метод для получения данных.
        Возвращает отсортированный по ЗП список, от большей к меньшей.
        """
        data = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=self.headers, params=self.par).json()
        all_vac = []
        for i in data['objects']:
            all_vac.append(i)
        all_vac.sort(key=lambda x: x['payment_from'], reverse=True)
        return all_vac


# printj(sj.get_api()['objects'][0]['profession']) # name
# printj(sj.get_api()['objects'][0]['id']) # id
# printj(sj.get_api()['objects'][0]['link']) # url
# printj(sj.get_api()['objects'][0]['candidat']) # opisanie
# printj(sj.get_api()['objects'][0]['payment_from']) # zp

