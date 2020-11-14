import matplotlib.pyplot as plt
from random_walk import Random_Walk

while True:
    walking = Random_Walk(50000)
    walking.fill_walk()
    point_numbers = list(range(walking.num_points))
    plt.scatter(walking.xValues, walking.yValues, c=point_numbers, cmap = plt.cm.Blues,
    edgecolor='none', s=1)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #plt.figure(figsize=(10,6))


    plt.show()
    q = input("Stop the program?")
    if q.lower() == "yes":
        break
