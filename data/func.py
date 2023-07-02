import csv
import json

from data.full_vac import Vacancy


def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


def all_vacancy():
    all_vac = []
    with open('save_file/hh.ru.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for vacancy in data:
        vac = Vacancy(vacancy['name'], vacancy['alternate_url'], vacancy['salary']['from'])
        all_vac.append(vac)

    with open('save_file/sj.ru.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        vac = Vacancy(i['profession'], i['link'], i['payment_from'])
        all_vac.append(vac)

    return all_vac


def create_file_csv():
    for vacancy in sorted(all_vacancy(), reverse=True):
        with open('save_file/all_vacancy.csv', 'a', encoding='utf-8') as file:
            data = csv.writer(file)
            data.writerow((vacancy.name, vacancy.url, vacancy.zp))


def clear_file_csv():
    with open('save_file/all_vacancy.csv', 'w', encoding='utf-8') as file:
        data = csv.writer(file)
        data.writerow(
            ["Вакансия",
             "Ссылка на вакансию",
             "Указанная зарплата"
             ]
        )


def print_top_vac(n=None):
    sort_vac = sorted(all_vacancy(), reverse=True)
    return [print(i) for i in sort_vac[:n]]


