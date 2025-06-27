"""
File_Name: archive_utility.py

Desc:
This file is created to provide archiving related operations utility
You can consider this class as wrapper class for tarfile

__copyright__ = "Copyright (c) 2022 by Waters Corporation, all rights reserved."
"""
import os
import re
import tarfile

from utilities.stopwatch import stopwatch
from utilities.logger import Logger

logger = Logger(os.path.basename(__file__))


def make_archive(archive_name, source_dir, skip_directories):
    """
    Folder gets archived.
    @param archive_name: The name of the archive to be created.
    @param source_dir: The path of the folder to be archived.
    @type skip_directories: List of folder names to skip
    """

    logger.debug(f"Archiving local path '{source_dir}' to '{archive_name}'...")
    tmr = stopwatch().start()

    skip_directories.append(archive_name)
    excludes = r'|'.join(skip_directories)

    def filter_function(tarinfo: tarfile.TarInfo):
        """
        Checks if folder is declared to be skipped from being archived
        """
        if re.match(excludes, tarinfo.name[2:]):
            logger.debug(f"Found exclusion filter, skipping folder: {tarinfo.name}")
            return None
        return tarinfo

    if os.path.exists(archive_name):
        os.remove(archive_name)

    # Open for gzip compressed writing
    with tarfile.open(os.path.join(source_dir, archive_name), "w:gz") as tar:
        tar.add(source_dir, arcname='.', filter=filter_function)

    logger.debug(f"Finished archiving local path in {tmr.elapsed()} seconds")


def extract_tar_archive(archive_path: str, destination_dir: str):
    """
    Extract an archive.
    @param archive_path: The path of the archive to be created.
    @param destination_dir: The path of the folder to be archived.
    """
    logger.debug(f"Extracting archive '{archive_path}' to  '{destination_dir}'")
    tmr = stopwatch().start()

    try:
        with tarfile.open(archive_path, 'r:gz') as file:
            file.extractall(destination_dir)
    except Exception as e:
        logger.error(f"Something went wrong when extracting: {e}")
        raise e from None

    logger.debug(f"Finished extracting archive in {tmr.elapsed()} seconds")
