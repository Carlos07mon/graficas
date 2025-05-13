# 2. Gráfico de barras
cursos = ['A', 'B', 'C', 'D', 'E']
cantidad = [30, 25, 40, 20, 35]
plt.figure()
plt.bar(cursos, cantidad, color='skyblue')
plt.title('Cantidad de Estudiantes por Curso')
plt.xlabel('Curso')
plt.ylabel('Cantidad')
plt.show()