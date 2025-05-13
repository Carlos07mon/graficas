# 12. Gráfica de barras por producto
ventas_por_producto = df.groupby('Producto')['Ventas'].sum()
ventas_por_producto.plot(kind='bar', color='orange')
plt.title('Ventas Totales por Producto')
plt.xlabel('Producto')
plt.ylabel('Total Ventas')
plt.grid(True)
plt.show()