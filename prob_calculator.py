import random 
import copy

class Hat:

    def __init__(self, **kwargs):
        self.contents =  []
        for item in kwargs:
            for i in range(0, kwargs[item]):
                self.contents.append(item)
    
    def draw (self, number_of_balls):
        draw_itens = []
        if number_of_balls > len(self.contents):
            return self.contents
        for i in range(number_of_balls):
          draw_item = self.contents.pop(random.choice(range(len(self.contents))))
  
          draw_itens.append(draw_item)
        return draw_itens
             
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # Generating the draw
    for experiment in range(0, num_experiments):
        success = 0
        draws = hat.draw(num_balls_drawn)
        draws_dict = {}
        # Transforming the draw in dictionary
        for draw in draws:
            check = 0
            if draw not in draws_dict:
                draws_dict[draw] = 1
            elif draw in draws_dict:
                draws_dict[draw] += 1
            # Checking if the keys and values are the same 
            for key in draws_dict:
                if key in expected_balls:
                    if draws_dict[key] == expected_balls[key]:
                        check += 1
            if check == num_balls_drawn:
                success += 1
    probability = success / num_experiments
    return probability

hat = Hat(blue=3,red=2,green=6)
print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))
       