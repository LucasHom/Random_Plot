import matplotlib.pyplot as plt

xvlue = [num for num in range(1, 1001)]
yvlue = [num**2 for num in xvlue]
plt.scatter(xvlue, yvlue, c=yvlue, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squared Value", fontsize=14)
plt.tick_params(axis = 'both', labelsize=14)
plt.title("Scattered Dots", fontsize=28)
plt.axis([0,1100,0,1100000])

plt.savefig("squares_plot.png", bbox_inches='tight')
#plt.show()
