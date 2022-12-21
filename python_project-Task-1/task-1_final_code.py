import os
import sys

files_name_with_extension_and_no_path = []
PYTHON_FILE_EXTENSION = ".py"

def get_python_files_list_with_path(path_to_python_files_folder):
    get_file_names_with_path = []
    for root, dirs, files in os.walk(path_to_python_files_folder):
        for file in files:
            get_file_names_with_path.append(file)
        break
    return get_file_names_with_path

def get_files_name_with_no_extension_and__no_path(files_with_path_and_extension, to_strip):
    files_name_with_no_extension_and__no_path = []
    for path in files_with_path_and_extension:
        path_with_no_filename_and_extension, file_name_with_extension_and_no_path = os.path.split(path)
        files_name_with_extension_and_no_path.append(file_name_with_extension_and_no_path)
        file_name_with_no_extension_and_no_path = file_name_with_extension_and_no_path.replace(to_strip, "")
        files_name_with_no_extension_and__no_path.append(file_name_with_no_extension_and_no_path)
    return files_name_with_no_extension_and__no_path
    

def main(python_files_folder):
    cwd = os.getcwd()
    source = os.path.join(cwd, python_files_folder)

    python_files_with_path_and_extension = get_python_files_list_with_path(source)
    python_files_name_with_no_extension_and_no_path = get_files_name_with_no_extension_and__no_path(python_files_with_path_and_extension, PYTHON_FILE_EXTENSION)


    #print(files_name_with_no_extension)

if __name__ == "__main__":
    args = sys.argv

    if len(args) != 2:
        raise Exception("You must pass exactly two parameters")
    else:
        main(args[1])