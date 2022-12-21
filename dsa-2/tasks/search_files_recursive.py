import os


def search_files_in_directory(current_dir_name, list_files):
    current_list_files = list_files

    for dir_name in os.listdir(current_dir_name):
        abs_path = os.path.join(current_dir_name, dir_name)

        if os.path.isdir(abs_path):
            search_files_in_directory(abs_path, current_list_files)
        if os.path.isfile(abs_path):
            list_files.append(abs_path)
    return current_list_files


def search_all_files_in_directory(dir_name):
    """
    Функция рекурсивного поиска файлов в заданной директории,
    включая вложенные каталоги
    """
    return search_files_in_directory(dir_name, [])
