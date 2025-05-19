import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros
num_puntos = 100
limite = 10
paso = 0.2  # tamaño del movimiento aleatorio por frame

# Posiciones iniciales
x = np.random.uniform(-limite, limite, num_puntos)
y = np.random.uniform(-limite, limite, num_puntos)

# Crear figura
fig, ax = plt.subplots()
scat = ax.scatter(x, y)
ax.set_xlim(-limite, limite)
ax.set_ylim(-limite, limite)
ax.set_title("Puntos moviéndose aleatoriamente")

# Función de actualización
def update(frame):
    global x, y
    x += np.random.uniform(-paso, paso, num_puntos)
    y += np.random.uniform(-paso, paso, num_puntos)
    scat.set_offsets(np.c_[x, y])
    return scat,

# Animación
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()