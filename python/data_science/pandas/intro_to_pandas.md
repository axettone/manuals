# Intro su Pandas

Alcuni esempi di base

Il dataset è stato acquisito da https://raw.githubusercontent.com/Nlabbert/HR-Analytics/master/HR%20Analytics/HR_comma_sep.csv

```
import pandas as pd

# Leggo il file dati
dataFile = pd.read_csv('path_to_csv_file.csv')

# Per determinare il formato (righe e colonne)
dataFile.shape

# Per determinare le colonne
dataFile.columns

# Per stampare le prime n righe e l'intestazione
dataFile.head(5)

# Per stampare le ultime n righe e l'intestazione
dataFile.tail(5)

# Per avere info sui dati (tipologia, elementi non nulli)
dataFile.info()

# Per avere una descrizione statistica dei dati
dataFile.describe()

# Per mostrare una colonna
dataFile["satisfaction_level"]

# Per selezionare più colonne
dataFile2 = dataFile[["satisfaction_level", "salary]]
dataFile2

# Per esportare in un csv
dataFile2.to_csv('nomefile.csv')

# Per ottenere un sottinsieme (rigainizio:rigafine, colonnainizio:colonafine).
# (supporta indici nei soliti formati python)

dataFile.iloc[0:10,0:0]

# Posso creare al volo una colonna e assegnare massivamente un valore
dataFile["nuova_colonna"] = 1

# Posso creare una colonna ottenuta come calcolo di altre colonne
dataFile["impact"] = dataFile["satisfaction_level"] * datafile["number_project"]

# Per cancellare una colonna
del dataFile["column_name"]

# Creare un nuovo dataset ottenuto da espressione condizionale
# Le condizioni si possonon combinare anche con delle parentesi
# e le varie combinazioni logiche logiche (& |)

new_dataFile = dataFile[ dataFile ["number_project"] > 4 ]

# Per ottenere una lista dei valori di una colonna
dataFile["salary"].unique()

# Effettuare un ordinamento, anche multicolonna e specifcando il tipo
dataFile.sort_values(["impact", "number_project"], ascending=[0,1])

# Ottenere nuovo dataset come aggregazione da colonne
# (si può anche fare multicolonna)
dg = dataFile.groupby(["salary"], as_index=False)["satisfaction_level"].sum()


```
