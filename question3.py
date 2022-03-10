import pandas as pd
from sqlalchemy import create_engine
from connectpostgress import *


#engine = create_engine("postgresql+psycopg2://postgres:yashyash@localhost:5432/postgres")




def adddb(data, file):
    try:
        if data == 'Q2':
            df = pd.read_excel(file, 'Q2')
            df.to_sql(name='compensation_details', con=engine, if_exists='append', index=False)

    except:
        print("db uploading new table error ")
        logging.error("There is an error... in uploading table to sql")

    finally:
        print("Successful uploading table to db")
        logging.info("Issues found=0")


with pd.ExcelFile('/Users/somalayashwanthreddy/Downloads/q2.xlsx') as xls:
    for sheet_name in xls.sheet_names:
        adddb(sheet_name, xls)
