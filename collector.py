'''
Collector
Collector module is responsible for collecting data from the files.
v0.0.1
'''

import os
import threading
import sqlite3
import yaml

class Collector:
    def __init__(self):
        pass

    def get_config(self, file):
        '''
        Get the config file form the yaml file.
        '''
        with open(file, 'r') as f:
            config = f.read()
        return config
    
    def create_db(self, db_name):
        '''
        Create a database with the given name.
        '''
        sqliteConnection = sqlite3.connect(db_name)
        cursor = sqliteConnection.cursor()
        print("Successfully connected to SQLite")

        with open('corpus.sql', 'r') as sqlite_file:
            sql_script = sqlite_file.read()
        cursor.executescript(sql_script)
        print("SQLite script executed successfully")
        cursor.close()

    def get_files(self, inpath):
        '''With the directory path, returns a list of markdown file paths.'''
        outlist = []
        for (path, dirs, files) in os.walk(inpath):
            for filename in files:
                ext_index = filename.find(".")
                if filename[ext_index+1:] == "md":
                    entry = path + "\\" + filename
                    outlist.append(entry)
        return outlist
    
    def batch(self, inpath):
        '''Divides the list of files into 4 sections.'''
        n = len(inpath)
        section_size = n // 4
        sections = [array[i*section_size:(i+1)*section_size] for i in range(4)]
        if n % 4 != 0:
            sections[-1].extend(array[4*section_size:])
        return sections

    def process_batch(self, sections):
        '''Processes the batch of files.'''
        threads = []
        for i in range(4):
            th = threading.Thread(target=get_links_from_page, args=(sections[i][0], sections[i][1], link_report, pdf))
            th.start()
            threads.append(th)
        [th.join() for th in threads]
        link_report.sort(key=operator.itemgetter(0))
        link_report.insert(0, ["page", "uri", "status", "request-error"])
        return link_report