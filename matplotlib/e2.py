import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

plt.plot(x, y1, label="Cuadrados")
plt.plot(x, y2, label="Lineal")

plt.title("Ejercicio 2: Varias líneas")
plt.xlabel("X")
plt.ylabel("Valores")
plt.legend()  # muestra las etiquetas
plt.show()
