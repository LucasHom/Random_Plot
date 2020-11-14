from random import choice

class Random_Walk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.xValues = [0]
        self.yValues = [0]

    def fill_walk(self):
        #x_step = get_step()
        #y_step = get_step()
        while len(self.xValues) < self.num_points:
            x_direction = choice([1])
            x_distance = choice([num for num in range(0, 10)])
            x_step = x_direction*x_distance

            y_direction = choice([1, -1])
            y_distance = choice([num for num in range(0, 10)])
            y_step = y_direction*y_distance

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.xValues[-1] + x_step
            next_y = self.yValues[-1] + y_step
            self.xValues.append(next_x)
            self.yValues.append(next_y)



    #def get_step(self):
