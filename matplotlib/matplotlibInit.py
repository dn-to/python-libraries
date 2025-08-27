import pandas
import matplotlib.pyplot as plt

data = {
    "Empleado": ["Ana", "Luis", "Carla", "Pedro", "Marta", "Diego", "Sofía", "Juan", "Daniela", "Jesus"],
    "Departamento": ["Ventas", "Ventas", "IT", "IT", "Recursos Humanos", "IT", "Ventas", "Recursos Humanos", "IT", "Externo"],
    "Edad": [23, 34, 29, 41, 38, 27, 25, 45, 24, 19],
    "Salario": [12000, 18000, 25000, 27000, 22000, 23000, 15000, 26000, 30000,400],
    "Ciudad": ["CDMX", "Monterrey", "Guadalajara", "CDMX", "Puebla", "Monterrey", "CDMX", "Guadalajara", "CDMX", " "]
}
df = pandas.DataFrame(data)

ndf = df.groupby("Ciudad")["Empleado"].count()
print(ndf)

#ndf.plot(kind="bar")

#plt.title("Employees per city")  # título
#plt.xlabel("City") # etiqueta eje X
#plt.ylabel("Employees") # etiqueta eje Y
#plt.show()

#ndf.plot(kind="pie", autopct="%1.1f%%")

plt.title("Distribución de personas por ciudad")
plt.ylabel("")  # para quitar el texto de la izquierda
plt.show()
print("Se está llevando acabo el proceso de crear la gráfica")
