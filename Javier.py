"""
Nombre: Javier
Carnet: 20159
"""

# Cargando el csv con pandas.
import pandas as pd

df = pd.read_csv("movies.csv", encoding='ISO-8859-1')

# Imprimendo todas las columnas.
print(df.columns)