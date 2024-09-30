import numpy as np
import pandas as pd
def q01():
    print('q01')
    sum = 0
    my_list01 = [12, 'Flower of Life', 'Plume of Death', 5, 'Sands of Eon',
               'Goblet of Eonothem', 'Goblet of Eonothem', 13, 'Circlet of Logos', 7, 32]

    # put your code here
    my_list02 = []

    for x in my_list01:
        if not isinstance(x , str):
            my_list02.append(x)
    print(np.sum(my_list02))
    # Print the total of number element(s) in the above list (Ignore text elements)
    # 3 points
