import os
import pandas as pd
from sqlalchemy import create_engine
import logging
import time 

os.chdir("/Users/nipunchauhan/Desktop/Projects/DA Project")
print(os.getcwd())

logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level = logging.DEBUG,
    format ='%(asctime)s - %(levelname)s - %(message)s',
    filemode = "w"
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    """This function will ingest dataframe into database table"""
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():
    """This function loads the CSVs as dataframes and ingests them into db"""
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:
            df = pd.read_csv('data/' + file)
            logging.info(f"Ingesting {file} in db")
            ingest_db(df, file[:-4], engine)
    end = time.time()
    total_time = (end - start)/60  # time in minutes
    logging.info("------------------Ingestion complete------------------")
    logging.info(f"Total time taken {total_time} minutes")
if __name__ == "__main__":
    load_raw_data()