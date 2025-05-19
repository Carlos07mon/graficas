import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Leer datos desde CSV
df = pd.read_csv("datos.csv")  # Asegúrate de tener un archivo llamado "datos.csv"

# Crear figura
fig, ax = plt.subplots()
barra = ax.bar(["Valor"], [0], color='green')
ax.set_ylim(0, df["Valor"].max() * 1.1)
titulo = ax.set_title("")

# Función de actualización
def update(frame):
    año = df["Año"][frame]
    valor = df["Valor"][frame]
    barra[0].set_height(valor)
    titulo.set_text(f"Año: {año}")
    return barra[0], titulo

# Crear animación
ani = FuncAnimation(fig, update, frames=len(df), interval=500, blit=True)

plt.show()


#  csv
# Año,Valor
# 2000,100
# 2001,120
# 2002,140
# 2003,160
# 2004,180