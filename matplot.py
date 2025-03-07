import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]  #Eje X

y = [10, 20, 25, 30, 40] #Eje Y

plt.plot(x, y, marker='o', linestyle='-', color='b')

plt.xlabel("Eje x")
plt.ylabel("Eje Y")
plt.title("Grafico de lineas")
plt.grid()
plt.show()