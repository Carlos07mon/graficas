# 10. Estadísticas básicas
total_ventas = df['Ventas'].sum()
promedio_precio = df['Precio'].mean()
producto_mas_vendido = df.groupby('Producto')['Ventas'].sum().idxmax()
print("Total de ventas:", total_ventas)
print("Promedio de precio:", promedio_precio)
print("Producto más vendido:", producto_mas_vendido)