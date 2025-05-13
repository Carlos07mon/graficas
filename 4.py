
# 4. Subplots
x_vals = np.linspace(0, 2*np.pi, 100)
fig, axs = plt.subplots(2)
axs[0].plot(x_vals, np.sin(x_vals), 'b')
axs[0].set_title('Seno')
axs[1].plot(x_vals, x_vals**2, 'r')
axs[1].set_title('Cuadrática')
plt.tight_layout()
plt.show()