# 5. Graficar y = x² - 3x + 2
x = np.linspace(-10, 10, 400)
y = x**2 - 3*x + 2
plt.figure()
plt.plot(x, y)
plt.title('Función Cuadrática: y = x² - 3x + 2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()