# 1. Gráfico de línea simple
valores = [3, 7, 1, 5, 12]
plt.figure()
plt.plot(valores, marker='o')
plt.title('Gráfico de Línea Simple')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.show()