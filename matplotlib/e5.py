import matplotlib.pyplot as plt
etiquetas = ["A", "B", "C", "D"]
valores = [15, 30, 45, 10]

plt.pie(valores, labels=etiquetas, autopct="%1.1f%%")
plt.title("Ejercicio 5: Pie Chart")
plt.show()
