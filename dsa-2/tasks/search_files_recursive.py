import os


def search_files_in_directory(current_dir_name, list_files=None):
    if list_files is None:
        list_files = []

    for dir_name in os.listdir(current_dir_name):
        abs_path = os.path.join(current_dir_name, dir_name)

        if os.path.isdir(abs_path):
            search_files_in_directory(abs_path, list_files)
        if os.path.isfile(abs_path):
            list_files.append(abs_path)
    return list_files


def search_all_files_in_directory(dir_name):
    return search_files_in_directory(dir_name)

