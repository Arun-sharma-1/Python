import numpy as np
from numpy.core.fromnumeric import sort
import pandas as pd
# used to create dataFrame

user_data = {
    'Marks A': np.random.randint(1, 100, 5),
    'Marks B': np.random.randint(1, 100, 5),
    'Marks C': np.random.randint(1, 100, 5)
}

df = pd.DataFrame(user_data, dtype=np.float64)
# print(df)

#df= df.coloums

# print(df['two'])
# del df['one']


# df.pop('two')

df = df.head(n=4)
# df = df.tail(n=3)
# print(df)

df.to_csv('marks.csv')  # create csv file
# READ CSV
MY_DATA = pd.read_csv('marks.csv')
MY_DATA = MY_DATA.drop(columns=['Unnamed: 0'])
print(MY_DATA)

# print(MY_DATA.describe())
print('#'*50)

# ACCESS ROW
print(MY_DATA.iloc[3])

# ACESS ROW AND COL
print(MY_DATA.iloc[3, 1])

# FIND INDEX
idx = df.columns.get_loc('Marks B')
print(idx)


# to select row in a dataframe
print(df.loc['b'])

# PRIINTING VALUES TOGETHER
idx = [df.columns.get_loc('Marks B'), df.columns.get_loc('Marks C')]
print(df.iloc[3, idx])


# SLICING IS ALSO POSSIBLE
print(df.iloc[:3, idx])


# SORTING DATA
df = df.sort_values(by=['Marks A'], ascending=True)
print(df)

# to add rows in a dataframe
df = pd.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
df1 = pd.DataFrame([[5, 6], [7, 8]], columns=['a', 'b'])
df = df.append(df1)

# delete a row
print(df.drop(0))
