'''
Collector
Collector module is responsible for collecting data from the files.
v0.0.1
'''

import os
from concurrent.futures import ThreadPoolExecutor
import sqlite3
import yaml

import page_processor as PP

class Collector:
    def __init__(self):
        pass

    def get_config(self, infile):
        '''
        Get the config file form the yaml file.
        '''
        with open(infile, 'r') as file:
            data = yaml.safe_load(file)
        return data

    def create_db(self, db_name, script_path='corpus.sql'):
        '''
        Create a database with the given name and initialize it using a SQL script.
        '''
        try:
            conn = sqlite3.connect(db_name)
            print("Successfully connected to SQLite")

            with open(script_path, 'r') as sqlite_file:
                sql_script = sqlite_file.read()

            cursor = conn.cursor()
            cursor.executescript(sql_script)
            print("SQLite script executed successfully")
        except Exception as e:
            print("An error occurred: {e}".format(e))


    def get_files(self, inpath):
        '''With the directory path, returns a list of markdown file paths.'''
        outlist = []
        for (path, dirs, files) in os.walk(inpath):
            for filename in files:
                ext_index = filename.find(".")
                if filename[ext_index+1:] == "md":
                    entry = path + "\\" + filename
                    outlist.append(entry)
                elif filename[ext_index+1:] == "yml":
                    entry = path + "\\" + filename
                    outlist.append(entry)
        return outlist


    def process_file(self, f, db_path, numberof):
        print(f"Processing page {f[0]+1} of {numberof}")
        pp = PP.pageProcessor()
        page = pp.get_page(f[1])
        extension = pp.get_extension(f[1]).lower()
        if extension in ["md", "yml"]:
            pp.savepagetotext(f[1], page, extension, db_path)
        else:
            print("File is not of markdown or YAML type.")

    def process_pages(self, files, db_path):
        numberof = len(files)
        files_with_index = list(enumerate(files))
        
        # Use ThreadPoolExecutor to create and manage a pool of threads
        with ThreadPoolExecutor(max_workers=4) as executor:
            executor.map(self.process_file, files_with_index, [db_path]*numberof, [numberof]*numberof)

    