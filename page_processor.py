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
        doc_ext, doc_raw, doc_length) VALUES (?, ?, ?, ?, ?, ? )',
        (doc_id, "corpus", doc_path, extension, page, doc_length) )
        sqliteConnection.commit()
        cursor.close()

        if extension == "md":
            metadata = page.split("---")[1]
            raw_page = page.split("---")[2]
            yml_metadata = yaml.load(metadata, Loader=yaml.FullLoader)

            sqliteConnection = sqlite3.connect(db_path)
            cursor = sqliteConnection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute('INSERT INTO body (doc_id, body_text) VALUES ( ?, ? )',
            (doc_id, raw_page) )
            sqliteConnection.commit()
            cursor.close()

            try:
                title = yml_metadata["title"]
            except KeyError:
                title = ""
            try:
                meta_description = yml_metadata["description"]
            except KeyError:
                meta_description = ""
            try:
                author = yml_metadata["author"]
            except KeyError:
                author = ""
            try:
                ms_author = yml_metadata["ms.author"]
            except KeyError:
                ms_author = ""
            try:
                ms_service = yml_metadata["ms.service"]
            except KeyError:
                ms_service = ""
            try:
                ms_topic = yml_metadata["ms.topic"]
            except KeyError:
                ms_topic = ""
            try:
                ms_date = yml_metadata["ms.date"]
            except KeyError:
                ms_date = ""

            sqliteConnection = sqlite3.connect(db_path)
            cursor = sqliteConnection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute('INSERT INTO metadata (doc_id, metadata_raw, title, meta_description, author, ms_author, ms_service, ms_topic, ms_date ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )',
            (doc_id, metadata, title, meta_description, author, ms_author, ms_service, ms_topic, ms_date) )
            sqliteConnection.commit()
            cursor.close()

        elif extension == "yaml":
            raw_yaml = yaml.load(page, Loader=yaml.FullLoader)
            try:
                yml_metadata = raw_yaml["metadata"]
            except KeyError:
                metadata = ""

            sqliteConnection = sqlite3.connect(db_path)
            cursor = sqliteConnection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute('INSERT INTO body (doc_id, body_text) VALUES ( ?, ? )',
            (doc_id, str(raw_yaml)) )
            sqliteConnection.commit()
            cursor.close()

            try:
                title = yml_metadata["title"]
            except KeyError:
                title = ""
            try:
                meta_description = yml_metadata["description"]
            except KeyError:
                meta_description = ""
            try:
                author = yml_metadata["author"]
            except KeyError:
                author = ""
            try:
                ms_author = yml_metadata["ms.author"]
            except KeyError:
                ms_author = ""
            try:
                ms_service = yml_metadata["ms.service"]
            except KeyError:
                ms_service = ""
            try:
                ms_topic = yml_metadata["ms.topic"]
            except KeyError:
                ms_topic = ""
            try:
                ms_date = yml_metadata["ms.date"]
            except KeyError:
                ms_date = ""
            
            sqliteConnection = sqlite3.connect(db_path)
            cursor = sqliteConnection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute('INSERT INTO metadata (doc_id, metadata_raw, title, meta_description, author, ms_author, ms_service, ms_topic, ms_date ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ? )',
            (doc_id, metadata, title, meta_description, author, ms_author, ms_service, ms_topic, ms_date) )
            sqliteConnection.commit()
            cursor.close()

            try:
                title = yml_metadata["title"]
            except KeyError:
                title = ""
            try:
                meta_description = yml_metadata["meta_description"]
            except KeyError:
                meta_description = ""
            try:
                author = yml_metadata["author"]
            except KeyError:
                author = ""
            try:
                ms_author = yml_metadata["ms_author"]
            except KeyError:
                ms_author = ""
            try:
                ms_service = yml_metadata["ms_service"]
            except KeyError:
                ms_service = ""
            try:
                ms_topic = yml_metadata["ms_topic"]
            except KeyError:
                ms_topic = ""
            try:
                ms_date = yml_metadata["ms_date"]
            except KeyError:
                ms_date = ""

            sqliteConnection = sqlite3.connect(db_path)
            cursor = sqliteConnection.cursor()
            print("Successfully connected to SQLite")
            cursor.execute('INSERT INTO metadata (doc_id, metadata_raw, title, meta_description, author, ms_author, ms_service, ms_topic, ms_date ) VALUES ( ?, ?, ?, ?, ?, ?, ? )',
            (doc_id, metadata, title, meta_description, author, ms_author, ms_service, ms_service, ms_service, ms_topic, ms_date) )
            sqliteConnection.commit()
            cursor.close()