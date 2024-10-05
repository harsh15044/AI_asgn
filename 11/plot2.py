import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.linspace(-6,6,400)

fig, (ax2) = plt.subplots(1,figsize=(7,5))


#Sigmoid plotting
ax2.plot(x,sigmoid(x), color='green', linewidth=4)
ax2.set_title('Sigmoid Function', loc='center')
ax2.set_ylim([0,1])
ax2.set_xlim([-6,6])

plt.tight_layout()
plt.savefig('plot2.png', format='png', bbox_inches='tight')
plt.show()
