import random
import os

def create_files_and_summary():
    summary_data = []

    # Get the directory of the current script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Create a new directory at the same level as the script
    new_directory_name = 'output_files'
    new_directory_path = os.path.join(current_directory, new_directory_name)
    os.makedirs(new_directory_path, exist_ok=True)

    # Create the summary file inside the new directory
    summary_file_path = os.path.join(new_directory_path, 'summary.txt')
    summary_file = open(summary_file_path, 'w')


    for num in range(1, 27):
        file_name = ''.join(chr(num + 64)) + '.txt'
        random_number = random.randint(1, 100)

        # Write the random number to the file inside the new directory
        file_path = os.path.join(new_directory_path, file_name)
        with open(file_path, 'w') as file:
            file.write(str(random_number))

        # Append the filename and random number to the summary_data list
        summary_data.append(f'{file_name}: {random_number}')

    # Write the summary_data to the summary file
    summary_file.write('\n'.join(summary_data))

    # Close the summary file
    summary_file.close()


create_files_and_summary()