import numpy as np, matplotlib.pyplot as plt

X = np.linspace(-2, 1, 1000)
Y = np.linspace(-1.5, 1.5, 1000)
C = X[:, None] + 1j * Y
Z = np.zeros_like(C, dtype=complex)
M = np.zeros(C.shape, dtype=int)

for i in range(50):  
    Z = Z**2 + C  
    M[np.abs(Z) < 2] = i  

plt.imshow(M.T, cmap='inferno', extent=[-2, 1, -1.5, 1.5])
plt.axis("off")
plt.show()
