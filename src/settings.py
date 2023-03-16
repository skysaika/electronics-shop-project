import csv


def take_from_csv() -> list:
    """Получение данных из файла csv"""
    data_list = []
    with open('../src/items.csv', 'r', encoding='windows-1251') as csvfile:
        data_csv = csv.reader(csvfile, delimiter=',')
        for elem in data_csv:
            if elem[0] == 'name':
                continue
            else:
                data_list.append(elem)
        return data_list
