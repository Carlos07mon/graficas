import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear figura y ejes
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_title("Punto girando en círculo")

# Punto móvil y trayectoria
punto, = ax.plot([], [], 'ro')  # punto rojo
trayectoria, = ax.plot([], [], 'b-', lw=1)  # línea azul

# Datos para la trayectoria (cola)
x_data, y_data = [], []

# Función de inicialización
def init():
    punto.set_data([], [])
    trayectoria.set_data([], [])
    return punto, trayectoria

# Función de actualización
def update(t):
    x = np.cos(t)
    y = np.sin(t)
    punto.set_data(x, y)
    x_data.append(x)
    y_data.append(y)
    trayectoria.set_data(x_data, y_data)
    return punto, trayectoria

# Animación
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 200),
                    init_func=init, interval=50, blit=True)

plt.show()