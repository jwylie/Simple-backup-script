"""
Script:   backup.py
Desc:     A basic script used for backing up directories
Created by: Jordan Wylie
Last Modified: 7th of June 2018
"""
import os
from zipfile import ZipFile
from datetime import datetime

def zipDirectory(directory, zipPath):
    """
    Arguments: directory - path to directory that is to be zipped
               zipPath - path to where the .zip file is to be placed
    Description: goes through a directory and adds each file and directory after the zipPath to a zip file
    """
    with ZipFile(zipPath, 'w') as zip:
        for root, dirs, files in os.walk(directory):
            for file in files:
                zip.write(os.path.join(root, file))

def main():
    directories = [None] # Folders to be backed up, Absolute paths required
    backupLocation = None # Path to where your backups are to be stored. Example format: "E:/Drive Backups/"
    for directory in directories:
        time = datetime.now()
        timestamp = str(time.day).zfill(2) + "-" + str(time.month).zfill(2) + "-" + str(time.year).zfill(2) + "_" + str(time.hour).zfill(2) + "-" + str(time.minute).zfill(2)
        zipName = backupLocation + timestamp + ".zip"
        zipDirectory(directory, zipName)
    
if __name__ == '__main__':
    main()