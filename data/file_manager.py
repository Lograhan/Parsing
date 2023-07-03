import json


class File_manager:
    """

    """

    @staticmethod
    def open_file(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def add_vac(file_name, data):
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data))
