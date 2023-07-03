import sys

from data.func import create_file_csv, clear_file_csv, print_top_vac
from data.class_hh import HH_api
from data.class_superjob import SuperJ
from data.file_manager import File_manager


def main():
    user_input_1 = input('Доброго времени суток!\n'
                         'Перед началом работы, рекомендуется очистить файл "all_vacancy.csv"\n'
                         'Для очистки введите "yes": ')

    if user_input_1 == 'yes':
        clear_file_csv()
        print('файл успешно очищен')

    keyword = 'python'  # input('Введите профессию: ')

    hh = HH_api(keyword)
    sj = SuperJ(keyword)

    hh_file = File_manager.add_vac('save_file/hh.ru.json', hh.get_api())
    sj_file = File_manager.add_vac('save_file/sj.ru.json', sj.get_api())

    print(f'\nДанные по ключевому слову "{keyword}" собраны!')
    print('Для отображения всего списка вакансий нажмите "Enter"'
          '\nДля вывода определённого количества вакансий введите значение')

    while True:
        user_choice = input()
        if user_choice == '':
            print_top_vac()
            break
        elif user_choice:
            print_top_vac(int(user_choice))
            break
        else:
            print('Выберите предложенные варианты')

    print('\nЕсли вы желаете сохранить список всех вакансий, введите "yes".\n'
          'Файл будет сохранен по пути "/save_file/all_vacancy.csv"\n'
          'Либо введите "stop" для завершения работы программы\n')

    while True:
        user_input = input()
        if user_input == 'stop':
            print('Конец программы.\n')
            break
        elif user_input == 'yes':
            create_file_csv()
            print('Файл успешно создан\n'
                  'Желаете повторить и перевыбрать другую профессию?'
                  '\nyes/stop: ')

            while True:
                user_inp = input()
                if user_inp == 'yes':
                    main()
                elif user_inp == 'stop':
                    print(("конец программы"))
                    sys.exit()
                else:
                    print('Введите нужный вариант Введите нужный вариант')
        else:
            print('Введите нужный вариант')

    user_input_2 = input('Желаете очистить файл "all_vacancy.csv"? ("yes"): ')
    if user_input_2 == 'yes':
        clear_file_csv()
        print('файл успешно очищен')
    else:
        print('Конец программы.\n')


if __name__ == "__main__":
    main()
