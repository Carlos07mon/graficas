# 7. Operaciones entre arrays
a = np.random.uniform(0, 100, 100)
b = np.random.uniform(0, 100, 100)
suma_total = (a + b).sum()
valor_max = max(a.max(), b.max())
desviacion = np.std(np.concatenate([a, b]))
print("Suma total:", suma_total)
print("Valor máximo:", valor_max)
print("Desviación estándar:", desviacion)
