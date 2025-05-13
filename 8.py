# 8. Histograma con NumPy
data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Histograma de Distribución Normal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()