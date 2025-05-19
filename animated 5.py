import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parámetros de los planetas: (radio, velocidad angular)
planetas = [
    (1, 0.1),  # Planeta 1
    (2, 0.07), # Planeta 2
    (3, 0.05), # Planeta 3
]

# Crear figura
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_title("Sistema Planetario Simple")

# Estrella en el centro
ax.plot(0, 0, 'yo', markersize=10)  # Estrella amarilla

# Inicializar puntos y trayectorias
puntos = [ax.plot([], [], 'o')[0] for _ in planetas]
trayectorias = [ax.plot([], [], '-', lw=1)[0] for _ in planetas]
trayectorias_data = [([], []) for _ in planetas]

# Función de actualización
def update(frame):
    for i, (radio, omega) in enumerate(planetas):
        x = radio * np.cos(omega * frame)
        y = radio * np.sin(omega * frame)
        puntos[i].set_data(x, y)

        # Guardar trayectoria
        trayectorias_data[i][0].append(x)
        trayectorias_data[i][1].append(y)
        trayectorias[i].set_data(trayectorias_data[i][0], trayectorias_data[i][1])
    return puntos + trayectorias

# Crear animación
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi*100, 1000), interval=30, blit=True)

plt.show()