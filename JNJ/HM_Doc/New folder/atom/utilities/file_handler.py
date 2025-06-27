import os
import shutil
from itertools import islice

from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


def get_file_lines_count(filename):
    """
    Returns the number of lines a file has
    @param: filename
    @return: Number of lines in file. If 0, file is empty or does not exist
    """
    lines = 0
    if os.path.exists(filename):
        with open(filename) as f:  # encoding="utf-8") as f:
            for _ in f:
                lines += 1
    return lines


def copy_trimmed_file(source_file, destination_file, start_from_line):
    """
    Copies part of whole file content to given file on localhost
    @param: read_file_path, write_file_path, current_log_length
    @return: None
    """
    if not os.path.exists(source_file):
        raise ValueError(f"File not found: [{source_file}]")
    target_folder = os.path.dirname(destination_file)
    os.makedirs(name=target_folder, exist_ok=True)
    if start_from_line > 0:
        with open(source_file, encoding="utf-8") as source, open(destination_file, 'a') as destination:
            lines = list(islice(source, start_from_line, None))
            destination.writelines(lines)
        return

    shutil.copy(source_file, destination_file)


def create_folder(folder, delete_if_exists=False):
    """
    Creates a new folder
    @param: folder
    @return: none
    """
    if delete_if_exists:
        delete_folder(folder)
    if not os.path.isdir(folder):
        os.mkdir(folder)


def delete_folder(folder):
    """
    Deletes a folder
    @param: folder
    @return: none
    """
    if os.path.isdir(folder):
        try:
            change_folder_permissions(folder, 0o777)
            shutil.rmtree(folder)
            logger.debug(f"Removed folder '{folder}'.")
        except shutil.Error as shutilError:
            logger.error(f"Failed to delete '{folder}' folder: {shutilError}")
        except PermissionError as permissionError:
            logger.error(f"Failed to delete '{folder}' folder: {permissionError}")


def change_folder_permissions(folder, permission):
    """
    Changes folder, subfolders and files permission
    @param: folder, permission
    @return: none
    """
    os.chmod(folder, permission)
    for root, dirs, files in os.walk(folder):
        for _dir in dirs:
            os.chmod(os.path.join(root, _dir), permission)
        for file in files:
            os.chmod(os.path.join(root, file), permission)
    logger.debug(f"Changed permissions to all files from '{folder}'.")


def trim_file(filepath, start_index=None, end_index=None):
    """
    Trims file lines between a start_index and end_index
    @param: filepath, start_index, end_index
    @return: None
    """
    with open(filepath, 'r', encoding="utf-8") as fin:
        data = fin.readlines()[start_index:end_index]
    with open(filepath, 'w', encoding="utf-8") as fin:
        fin.writelines(data)


def copy_folder(source, destination):
    """
    Copies a folder with content
    @param: source, destination
    @return: none
    """
    create_folder(destination)

    try:
        os.system('cp -R "%s" "%s"' % (source, destination))
    except OSError as osError:
        logger.error("Files copy failed: %s" % osError)
        raise
