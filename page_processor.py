'''
PageProcessor
This class is responsible for processing the page and extracting the required information.
v0.0.1
'''

import os
import markdown
import yaml
import sqllite3

class pageProcessor:
    def __init__(self):
        pass

    def get_page(self, inpath):
        '''
        Get the page from the markdown file.
        '''
        with open(inpath, 'r') as f:
            page = f.read()
        return page
    
    def get_extension(self, inpath):
        '''
        Get the extension of the file.
        '''
        ext_index = inpath.find(".")
        return inpath[ext_index+1:]
    
    def savepagetotext(self, page, db_path):
        '''
        Save the page to the database.
        '''
        sqliteConnection = sqlite3.connect(db_path)
        cursor = sqliteConnection.cursor()
        print("Successfully connected to SQLite")
        cursor.execute("INSERT INTO pages (page) VALUES (?)", (page,))
        sqliteConnection.commit()
        cursor.close()
    


