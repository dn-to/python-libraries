import pandas

#----->Retrieving the file
dataFrame = pandas.read_csv("./file.txt", sep='\t')
#print(dataFrame)

#------>Retrieving only 5 first lines
#print(dataFrame.head(5))

#------>Retrieving specific columns
#print(dataFrame.columns)
#print(dataFrame[["Objeto" , "Nombre"]])

#------>Retrieving rows with specific conditions
print(dataFrame[dataFrame["Edad"]<20])

#------>Retrieving rows ordering by count
gbDF=dataFrame.groupby("Gustos")["Nombre"].count()
#print(gbDF)
#print(gbDF.sort_values(ascending=False))

#------>Retrieving rows with certain Gusto and Edad>20
