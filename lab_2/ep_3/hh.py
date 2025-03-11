import numpy as np
import matplotlib.pyplot as plt

file_path = "C:/Users/Михаил/Desktop/хрюникс/4сем/2laba/3/3.dat"
u0 = np.loadtxt(file_path)


N = len(u0)
T = np.linspace(0, 10, N)


A = np.eye(N, k=-1) - 0.5 * np.eye(N)
A[0, 0] = 1
A[0, 1:] = 0
A[-1, -1] = 1
A[-1, :-1] = 0


u = np.linalg.solve(A, u0)

# только файл содержит вроде 50 шагов а не 255
plt.figure(figsize=(10, 5))
plt.plot(T, -u)
plt.legend()
plt.grid()
plt.show()
