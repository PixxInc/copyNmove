import os
import shutil
import sys

def copy_file(source_path, destination_path):
    """Copy a file from source to destination."""
    try:
        shutil.copy2(source_path, destination_path)
        print(f"File copied from '{source_path}' to '{destination_path}' successfully.")
    except Exception as e:
        print(f"Failed to copy file: {str(e)}")

def move_file(source_path, destination_path):
    """Move a file from source to destination."""
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved from '{source_path}' to '{destination_path}' successfully.")
    except Exception as e:
        print(f"Failed to move file: {str(e)}")

if __name__ == "__main__":
    action = os.getenv('ACTION')
    source_path = os.getenv('SOURCE_PATH')
    destination_path = os.getenv('DESTINATION_PATH')

    if not action or not source_path or not destination_path:
        print("Error: 'ACTION', 'SOURCE_PATH', and 'DESTINATION_PATH' environment variables are required.")
        sys.exit(1)

    if action == "copy":
        copy_file(source_path, destination_path)
    elif action == "move":
        move_file(source_path, destination_path)
    else:
        print("Error: Invalid 'ACTION'. Use 'copy' or 'move'.")
        sys.exit(1)
