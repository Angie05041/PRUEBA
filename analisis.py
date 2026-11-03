pd.set_option("display.max_columns",None)
pd.set_option("display.width",200)

Import unicodedata
Import pandas as pd 
Import matplotlib.pyplot as plt

df= pd.read_cvs("Datos/cybersegurity_attrack.cvs")

print ("Filas:", dfshape[0],"|Columnas:",df.shape[1])
print (df.dtypess)
print (df.head())

nulos=df.isnull().sum()
print (pd.DataFrame({"nulos":nulos,"%": (nulos/len(df)*100).round(2)})) 



