import pandas

#----->Retrieving the file
dataFrame = pandas.read_csv("./file.txt", sep='\t')
#print(dataFrame)

#------>Retrieving only 5 first lines
#ndataFrame= dataFrame.head(5)
#print(ndataFrame.sort_values("Edad", ascending=False)) #sort

#------>Retrieving specific columns
#print(dataFrame.columns) #name of columns
#print(dataFrame[["Objeto" , "Nombre"]])
#print(dataFrame["Edad"].mean()) #average of "Edad"
dataFrame["Mayor_de_30"] = dataFrame["Edad"] > 30 #create new column
#print(dataFrame)

#------>Retrieving rows with specific conditions
#print(dataFrame[dataFrame["Edad"]<20])
#gbDF=(dataFrame[(dataFrame["Gustos"]=="Música")  & (dataFrame["Edad"]<20)])
#gbDF=(dataFrame[(dataFrame["Gustos"]=="Música")  | (dataFrame["Edad"]<20)])
#print(gbDF)

#------>Retrieving rows ordering by count
#gbDF=dataFrame.groupby("Gustos")["Nombre"].count()
#print((dataFrame.groupby("Gustos")["Edad"].mean()).sort_values(ascending=False))



dataFrame.to_csv("resultado.csv", index=False)
