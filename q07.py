# put your code here
# put your code here
import numpy as np
import pandas as pd
def q07():

    # Change the Path to the location of your file
    df = pd.read_csv('C:\\Users\\pranu\\Downloads\\04-transaction2.csv')
    # put your code here


    df2 = df.groupby('payment_type')['transaction_amount'].sum().reset_index()
    df2.index = df2.index+1
    print("Total balance of transaction by payment type:\n", df2)


    # Print total balance of
    # cash transaction
    # credit_card transaction

    # 3 points


    print('q07')