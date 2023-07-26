import os

some_string = '''
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
    velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
    est laborum".
'''


def create_file(some_string: str):
    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Create a new directory at the same level as the script
    new_directory_name = 'output_files'
    new_directory_path = os.path.join(current_directory, new_directory_name)
    os.makedirs(new_directory_path, exist_ok=True)

    file_path = os.path.join(new_directory_path, 'lorem.txt')
    with open(file_path, 'w') as file:
        file.write(some_string)

create_file(some_string)

def copy_file_upper():
    # Get the absolute path of the script's directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the file paths using the absolute path
    output_directory = os.path.join(current_directory, 'output_files')
    file_path = os.path.join(output_directory, 'lorem.txt')
    upper_file_path = os.path.join(output_directory, 'upper_lorem.txt')

    with open(file_path, 'r') as file:
        some_string = file.read()
        upper_string = some_string.upper()

    with open(upper_file_path, 'w') as file:
        file.write(upper_string)

copy_file_upper()
