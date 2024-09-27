import numpy as np

Z = np.random.rand(1000000)

Z_power_1 = Z ** 3

Z_power_2 = np.empty_like(Z)
for i in range(len(Z)):
    Z_power_2[i] = Z[i] ** 3

Z_power_3 = np.power(Z, 3)

print(Z_power_1[:5])  # Print first 5 results from method 1
print(Z_power_2[:5])  # Print first 5 results from method 2
print(Z_power_3[:5])  # Print first 5 results from method 3
