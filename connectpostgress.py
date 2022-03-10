
import psycopg2
import xlsxwriter
import pandas as pd
import logging
from sqlalchemy import create_engine
engine=None
cur=None

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s: %(levelname)s --> %(funcName)s() --> %(message)s')

def connection():
    try:
        global cur
        connection = psycopg2.connect(database="postgres", user="postgres", password="yashyash",
                                      host="localhost",
                                      port=5432)
        logging.info("Database Connected....")
        print("Database Connected")
        cur = connection.cursor()

        return connection


    except:
        logging.error("Connection error")

    finally:
        logging.info("Isssues found=0")


def create_enginenow():
    global engine
    try:
        engine= create_engine("postgresql+psycopg2://postgres:yashyash@localhost:5432/postgres")

        return engine

    except:
        logging.error("error in creating engine")
        print('eror')

    finally:
        logging.info('engine created succuesfully')

connection()

create_enginenow()