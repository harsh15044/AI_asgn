import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate some random sample data for x and y
np.random.seed(0)
x = np.linspace(0, 10, 50)  # Input values
y = 2 * x + 3 + np.random.normal(0, 1, 50)  # y = 2x + 3 with some noise

# Define the loss function for a given w0, w1
def loss_function(w0, w1, x, y):
    return np.sum((y - (w1 * x + w0))**2)

# Create a grid of w0 and w1 values
w0_vals = np.linspace(0, 10, 100)
w1_vals = np.linspace(0, 2, 100)
W0, W1 = np.meshgrid(w0_vals, w1_vals)

# Calculate the loss for each combination of w0 and w1
Loss = np.array([[loss_function(w0, w1, x, y) for w0 in w0_vals] for w1 in w1_vals])

# Create a 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Generate a surface plot with a professional color scheme (e.g., 'cividis')
#surface = ax.plot_surface(W1, W0, Loss, cmap='cividis', edgecolor='black', alpha=0.8)
ax.plot_wireframe(W1, W0, Loss, color='red', linestyle=':', linewidth=0.5)

# Remove color bar
# fig.colorbar(surface, shrink=0.5, aspect=5)  # Commented out to remove the bar

# Remove axis tick values
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Adjust labels and title with a different font style
ax.set_xlabel('$w_1$', fontsize=12, labelpad=15)
ax.set_ylabel('$w_0$', fontsize=12, labelpad=15)
ax.set_zlabel('Loss', fontsize=12, labelpad=10)
ax.set_title('Professional 3D Plot of Loss Function', fontsize=15, pad=20)

# Set viewpoint to match the perspective of the original image
ax.view_init(elev=30, azim=120)

# Show the improved plot
plt.show()

