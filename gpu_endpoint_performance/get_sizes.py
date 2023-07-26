import os


def get_file_sizes(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            print(f"{file_path},{size}")


get_file_sizes("test_data")
