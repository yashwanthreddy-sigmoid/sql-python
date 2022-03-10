import pandas as pd
from sqlalchemy import create_engine
from connectpostgress import *


engine = create_engine("postgresql+psycopg2://postgres:yashyash@localhost:5432/postgres")

def adddb1(data, file):
    try:
        if data == 'Q2':
            df = pd.read_excel(file, 'Q2')
            return df

    except:
        print("reading a table error ")
        logging.error("There is an error...")

    finally:
        print("reading a table succesful")
        logging.info("Issues found=0")



def excelconversion(df):
    writer = pd.ExcelWriter('/Users/somalayashwanthreddy/Downloads/q4.xlsx')
    df.to_excel(writer, sheet_name='Q4', index=False)
    writer.save()

with pd.ExcelFile('/Users/somalayashwanthreddy/Downloads/q2.xlsx') as xls:
    for sheet_name in xls.sheet_names:
        df1=adddb1(sheet_name, xls)

df2 = df1.groupby(['Dept Name', 'Dept Number']).agg(
    Total_Compensation=pd.NamedAgg(column='Total Compensation', aggfunc="sum")
).reset_index()


excelconversion(df2)