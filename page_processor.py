'''
PageProcessor
This class is responsible for processing the page and extracting the required information.
v0.0.1
'''

import os
import markdown
import yaml
import sqlite3
import uuid

class pageProcessor:
    def __init__(self):
        pass

    def get_page(self, inpath):
        '''
        Get the page from the markdown file.
        '''
        try:
            with open(inpath, 'r') as f:
                page = f.read()
        except Exception as e:
            page = str(e)
        return page
    
    def get_extension(self, inpath):
        '''
        Get the extension of the file.
        '''
        ext_index = inpath.find(".")
        return inpath[ext_index+1:]
    
    def create_corpus(self, repository, db_path):
        '''
        Save the corpus to the database.
        '''
        corpus_id = str(uuid.uuid4())
        sqliteConnection = sqlite3.connect(db_path)
        cursor = sqliteConnection.cursor()
        print("Successfully connected to SQLite")
        cursor.execute("INSERT INTO corpus ({}, {}) VALUES (?, ?)".format(corpus_id, repository), (corpus_id, corpus_name))
        sqliteConnection.commit()
        cursor.close()
        return corpus_id


    def savepagetotext(self, doc_path, page, extension, db_path):
        '''
        Save the page to the database.
        '''
        doc_id = str(uuid.uuid4())
        doc_length = page.count("\n")
        sqliteConnection = sqlite3.connect(db_path)
        cursor = sqliteConnection.cursor()
        print("Successfully connected to SQLite")
        cursor.execute('INSERT INTO document (doc_id, corpus_id, doc_path, \
        doc_ext, doc_text, doc_raw, doc_length) VALUES ( ?, ?, ?, ?, ?, ?, ? )',
        (doc_id, "corpus", doc_path, extension, page, page, doc_length) )
        sqliteConnection.commit()
        cursor.close()