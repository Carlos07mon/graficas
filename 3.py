# 3. Gráfico de dispersión
x = np.random.rand(50)
y = np.random.rand(50)
plt.figure()
plt.scatter(x, y, color='green')
plt.title('Gráfico de Dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()