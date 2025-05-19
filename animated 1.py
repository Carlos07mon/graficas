import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Crear figura y ejes
fig, ax = plt.subplots()
x = np.linspace(0, 4 * np.pi, 1000)
line, = ax.plot(x, np.sin(x))

# Límites de la gráfica
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(0, 4 * np.pi)
ax.set_title("Onda seno animada: sin(x + t)")

# Función de animación
def update(t):
    y = np.sin(x + t)
    line.set_ydata(y)
    return line,

# Crear animación
ani = FuncAnimation(fig, update, frames=np.linspace(0, 4 * np.pi, 128), interval=50, blit=True)

plt.show()