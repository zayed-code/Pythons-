import os

def print_directory_contents(dir_path="."):
    """
    Print all the names (files and subdirectories) in the given directory.
    If no path is given, it defaults to the current working directory.
    """
    try:
        entries = os.listdir(dir_path)
    except FileNotFoundError:
        print(f"Error: The directory {dir_path} does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access {dir_path}.")
        return
    except OSError as e:
        print(f"OS error occurred: {e}")
        return

    print(f"Contents of directory '{dir_path}':")
    for name in entries:
        print(name)

if __name__ == "__main__":
    # You can change this to any path you want
    path = input("Enter directory path (how are you zayed): ").strip()
    if path == "":
        path = "."
    print_directory_contents(path)
# This script lists all files and directories in the specified path.