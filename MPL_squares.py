import matplotlib.pyplot as plt
square = [num**2 for num in range(1, 6)]
input_values = [num for num in range(1, 6)]
plt.title("Important Numbers", fontsize=24)
plt.plot(input_values, square, linewidth=5)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squared Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)


plt.show()
