import sqlite3 
conn = sqlite3.connect('autopilot.db3')
from pydoc import describe
from xml.etree.ElementTree import tostring
import pandas as pd
df = pd.read_csv('Export_2015-01-01_2022-03-31.csv',sep=";")
cur = conn.cursor() 

strSql = """
INSERT INTO ImportTimeSheet(
    Login,
    Nom,
    Prenom,
    Date,
    Clients,
    ProjetRegie,
    PhaseMission,
    TempsPasse,
    Unite
) 
VALUES(?,?,?,?,?,?,?,?,?)"""


for index, row in df.iterrows():
    for column in df:
        print("colum name : " + column + " -> " + str(type(row[column])) + " -> " + str(row[column])) 
    cur.execute(strSql, row)
    print(row)
    print('-----------------------------------')
cur.close()
conn.commit()