'''
This script is used to run the collector. It will collect the data from the API and store it in the database.
'''

import time
import collector as COL

def main():
    '''
    Main function to run the collector.
    '''
    col = COL.Collector()
    start_time = time.perf_counter()
    print("Processing....")

    try:
        config = col.get_config('config.yml')
        db_path = config['dbname']
    except FileNotFoundError:
        print('Config file not found.')
        return

    try:
        col.create_db(db_path)
        print('Database created successfully.')
    except FileNotFoundError:
        print('Database not found.')
        return
    
    try:
        files = col.get_files(config["corpora"][0]["path"])
        print('Files collected successfully.')
    except Exception as e:
        print('Error collecting files:', e)
        return

    try:
        col.process_pages(files, db_path)
        print('Pages processed successfully.')
    except Exception as e:
        print('Error processing pages:', e)
        return

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"The collection took {elapsed_time} seconds to run.")

if __name__ == "__main__":

    main()