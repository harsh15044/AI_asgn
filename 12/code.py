import numpy as np
import matplotlib.pyplot as plt

# Define the range for the x-axis
x = np.linspace(-6, 6, 400)

# Define the functions
sigmoid = 1 / (1 + np.exp(-x))
relu = np.maximum(0, x)
softplus = np.log1p(np.exp(x))  # Softplus function
tangent = np.tanh(x)

# Create the figure and subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot (a) Sigmoid Function
axs[0].plot(x, sigmoid, color='grey')
axs[0].set_xlim([-6, 6])
axs[0].set_ylim([-0.1, 1.1])
axs[0].set_xticks(np.arange(-6, 7, 2))
axs[0].set_yticks(np.arange(0, 1.1, 0.1))
axs[0].set_title('Sigmoid function', loc='center')
axs[0].grid(True)

# Plot (b) ReLU and Softplus
axs[1].plot(x, relu, color='green', label='ReLU')
axs[1].plot(x, softplus, color='brown', linestyle='--', label='softplus')
axs[1].set_xlim([-6, 6])
axs[1].set_ylim([-1, 8])
axs[1].set_xticks(np.arange(-6, 7, 2))
axs[1].set_yticks(np.arange(0, 9, 1))
axs[1].set_title('ReLU and Softplus function', loc='center')
axs[1].legend()
axs[1].grid(True)

# Plot (c) Tangent Function
axs[2].plot(x, tangent, color='blue')
axs[2].set_xlim([-6, 6])
axs[2].set_ylim([-1.1, 1])
axs[2].set_xticks(np.arange(-6, 7, 2))
axs[2].set_yticks(np.arange(-1, 2, 0.2))
axs[2].set_title('tanh function', loc='center')
axs[2].grid(True)

# Adjust layout to avoid overlap
plt.tight_layout()
plt.savefig('plot.png', bbox_inches='tight')
plt.show()

