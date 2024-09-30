# put your code here
import numpy as np
import pandas as pd
def q06():
    # Change the Path to the location of your file
    df = pd.read_csv('C:\\Users\\pranu\\Downloads\\03-member2.csv')
    data = pd.DataFrame(df)
    # put your code here
    df2 = df[['city']]
    cities = []

    for x in df2.index:
        cities.append(df.at[x, 'city'])

    cities2 = list(dict.fromkeys(cities))
    print(cities2)

    for x in cities2:
        df3 = df2[df2['city'] == x]
        num = len(df3)
        print(x + ": " + str(num))
        # count number of members by the City
    # 3 points
    print('q06')

    df4 = data.groupby('city')['city'].count
    print(df4)
