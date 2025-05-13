# 11. Filtrar productos vendidos en enero 2025
enero_2025 = df[df['Fecha'].str.startswith('2025-01')]
print("Ventas en enero 2025:")
print(enero_2025)
