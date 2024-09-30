#put your code here
import numpy as np
import pandas as pd
def q04():
    # Change the Path to the location of your file
    df = pd.read_csv('C:\\Users\\pranu\\Downloads\\02-student.csv')
    # put your code here

    # Print an average score of students who have score higher than 75th percentile.
    df2 = df[['score']]
    #print(df2)
    percent75 = np.percentile(df2, 75)
    #print(percent75)
    df3 = df2.query("score > " + str(percent75))
    print(np.mean(df3))
    # 4 points

    print('q04')