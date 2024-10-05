import numpy as np
import matplotlib.pyplot as plt

def threshold(x):
    return np.where(x >= 0, 1, 0)

x = np.linspace(-6,6,400)

fig, (ax1) = plt.subplots(1,figsize=(7,5))

#threshold plotting
ax1.plot(x, threshold(x), color='green', linewidth=4)
ax1.set_title('Threshold Function', loc='center')
ax1.set_ylim([0,1])
ax1.set_xlim([-6,6])

plt.tight_layout()
plt.savefig('plot1.png', format='png', bbox_inches='tight')
plt.show()
