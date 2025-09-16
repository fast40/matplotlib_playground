import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1337)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3)

image = np.random.randn(128, 128, 3)
ax1.imshow(image)
ax1.axis('off')

ax3.imshow(np.tile(np.arange(100, dtype=np.uint8), (100, 1)))

ax2.plot(np.arange(1000), np.arange(1000) ** 2)

plt.show()
