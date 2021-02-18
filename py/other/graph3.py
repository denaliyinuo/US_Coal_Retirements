import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file
path = '/Users/nathanoliver/Desktop/Python/Coal_Retirements/csv/november_generator_2020_active.csv'
df = call_file(path)

print(df.columns)

# print(df.columns)

# print(df['Technology'].value_counts())
# print(df['Energy Source Code'].value_counts())


# remove commas and remove spaces
col = ['Net Winter Capacity (MW)', 'Net Summer Capacity (MW)',
       'Nameplate Capacity (MW)', 'Planned Retirement Year']

for i in col:
    df[i] = df[i].replace(',', '', regex=True)
    df[i] = df[i].replace(' ', '', regex=True)
    df[i] = pd.to_numeric(df[i], downcast="float")


# determine the total capacity requirements for each year
df = df.reset_index(drop=True)


# replace null values with Nameplate Capacity
for i in range(len(df)):
    n1 = df.loc[i, 'Net Winter Capacity (MW)']
    n2 = df.loc[i, 'Net Summer Capacity (MW)']

    if pd.isna(n1) == True:
        df.loc[i, 'Net Winter Capacity (MW)'] = df.loc[i,
                                                       'Nameplate Capacity (MW)']
    if pd.isna(n2) == True:
        df.loc[i, 'Net Summer Capacity (MW)'] = df.loc[i,
                                                       'Nameplate Capacity (MW)']


df = df[df['Technology'] == 'Conventional Steam Coal']

print(df)

print(df['Planned Retirement Year'].value_counts())

for i in range(2020, 2041):
    # df_ne2 = df[df['Net Summer Capacity (MW)'] == 53]
    df_new = df[df['Planned Retirement Year'] == i]
    total = df_new['Nameplate Capacity (MW)'].sum()
    n = len(df_new)
    print(i, total, total / n)
