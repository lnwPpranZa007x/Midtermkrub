import pandas as pd
import numpy as np
def q08():
    # data transaction2
    df = pd.read_csv('C:\\Users\\pranu\\Downloads\\04-transaction2.csv')
    # Group the data into two groups
    # the first group categories: 'insurance','finance','utilities'
    # the second group: <the records that is not in the first group>
    # Display total balance of first group and second group

    #use only transaction amount and transaction_category

    df2 = df[['transaction_category','transaction_amount']]
    df3 = df2.query("transaction_category in ('utilities','finance','insurance')").sum()
    df4 = df2.query("transaction_category not in ('utilities','finance','insurance')").sum()
    total3 = df3[['transaction_amount']].sum()
    print(total3)
    total = df2[['transaction_amount']].sum()
    print(total - total3)
    total4 = df4[['transaction_amount']].sum()
    print(total4)
    print('q08')