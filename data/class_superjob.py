
import json

from data.abs_class import Api
import requests


class SuperJ(Api):
    def __init__(self, keyword, page=1):
        self.par = {
            'keywords': keyword,
            'page': page}
        self.headers = {
            'X-Api-App-Id': 'v3.r.115217111.f35c58645f2a860b45ea7e6eb703f4d594d8a883.25e952936abc3c0666afbeb30b5db4f05a3c172e'}

    def get_api(self):
        data = requests.get("https://api.superjob.ru/2.0/vacancies/", headers=self.headers, params=self.par).json()
        all_vac = []
        for i in data['objects']:
            all_vac.append(i)
        all_vac.sort(key=lambda x: x['payment_from'], reverse=True)
        return all_vac

    def sj_save_file(self):
        with open('save_file/sj.ru.json', 'w') as file:
            file.write(json.dumps(SuperJ.get_api(self)))

# printj(sj.get_api()['objects'][0]['profession']) # name
# printj(sj.get_api()['objects'][0]['id']) # id
# printj(sj.get_api()['objects'][0]['link']) # url
# printj(sj.get_api()['objects'][0]['candidat']) # opisanie
# printj(sj.get_api()['objects'][0]['payment_from']) # zp




# with open('../save_file/sj.ru.json', 'r', encoding="utf-8") as file:
#     data = json.load(file)

