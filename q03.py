# put you code here
import numpy as np
import pandas as pd


def q03():
    # Change the Path to the location of your file
    df = pd.read_csv('C:\\Users\\pranu\\Downloads\\01-worker.csv')
    # put your code here
    df2 = pd.DataFrame(df)
    #print(df2)

    # standard deviation of worker's hour rate
    df3 = (df2[['hours_cost']])
    print(np.std(df3['hours_cost']))
    # 4 points
    print('q03')