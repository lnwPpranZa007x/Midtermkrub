# put your code here
import pandas as pd
import numpy as np

def q05():
    # Change the Path to the location of your file
    df = pd.read_csv('C:\\Users\\pranu\\Downloads\\03-member2.csv')
    # put your code here

    # replace the '-' with text: 'No '
    # 5 points
    df2 = pd.DataFrame(df)
    df3 = df2.query("gender not in ('-','--')")
    print(df3)
    print('q05')