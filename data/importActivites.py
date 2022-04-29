import sqlite3 
conn = sqlite3.connect('autopilot.db3')
from pydoc import describe
from xml.etree.ElementTree import tostring
import pandas as pd
df = pd.read_csv('Rapport_sur_les_activite.csv',sep=";")
#print(df)

cur = conn.cursor() 
#cur.execute('SELECT * FROM consultant')
#for row in cur:
#   print(row)


strSql = """
INSERT INTO RapportActivite(
    NomComplet,
    Departement,
    CodeClient,
    NomClient,
    CodeProjetRegie,
    NomProjetRegie,
    CodePhaseMission,
    NomPhaseMission,
    CodeTacheMission,
    NomTacheMission,
    DateDebut,
    DateFin,
    TempImpute
) 
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)"""
#print(strSql)
cur.execute(strSql, ("Test", "Departement", 12, "Nom Client", "CodeProjet","NomProjet","CodePhaseMission","NomPhaseMission","CodeTache","NomTach",100000,10000,2))

def printChamp(strChamp):
    if type(row[strChamp]) == "string":
        print(strChamp+ " -> " + row[strChamp])
    else:
        print(strChamp + " -> " + row[strChamp].to_string())

for index, row in df.iterrows():
    a = {} 
    for column in df:
        print("colum name : " + column + " -> " + str(type(row[column])) + " -> " + str(row[column])) 
        a=row
    cur.execute(strSql, row)
    print(a)
    print('-----------------------------------')
#    print("Nom Complet -> "+ row["Département"])
#Code Clients;Nom Clients;Code Projet/Régie;Nom Projet/Régie;Code Phase/Mission;Nom Phase/Mission;Code Tâche;Nom Tâche;Date de début;Date de fin;Temps imputé (Jours) 
cur.close()
conn.commit()