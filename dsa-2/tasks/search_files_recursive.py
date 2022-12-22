import os


def search_files_in_directory(current_dir_name):
    """
    Функция рекурсивного поиска файлов в заданной директории,
    включая вложенные каталоги
    """
    list_files = []
    for dir_name in os.listdir(current_dir_name):
        abs_path = os.path.join(current_dir_name, dir_name)

        if os.path.isdir(abs_path):
            list_files.extend(search_files_in_directory(abs_path))
        if os.path.isfile(abs_path):
            list_files.append(abs_path)
    return list_files


for file in search_files_in_directory('.'):
    print(file)
print('count_files -', len(search_files_in_directory('.')))