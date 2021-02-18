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
path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/06_november_generator_2020.csv'
df = call_file(path)

print(df.columns)

# print(df['Technology'].value_counts())


# create new dataframe for coal power plants that retired after 2005
df = df[df['Technology'] == 'Conventional Steam Coal']
# df = df[df['Retirement Year'] >= 2005]


# remove commas and remove spaces
col = ['Net Winter Capacity (MW)', 'Net Summer Capacity (MW)',
       'Nameplate Capacity (MW)']

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

    if n1 == None:
        print('enter')

    if pd.isna(n1) == True:
        df.loc[i, 'Net Winter Capacity (MW)'] = df.loc[i,
                                                       'Nameplate Capacity (MW)']
    if pd.isna(n2) == True:
        df.loc[i, 'Net Summer Capacity (MW)'] = df.loc[i,
                                                       'Nameplate Capacity (MW)']


year = np.arange(2005, 2021)
retire = np.zeros(len(year))

for i in range(len(df)):
    n = df.loc[i, 'Retirement Year']
    index = np.where(year == n)

    capacity = df.loc[i, 'Net Summer Capacity (MW)']

    # retire[index[0][0]] = retire[index[0][0]] + float(capacity)


df['Age'] = df['Retirement Year'] - df['Operating Year']

age = []
capacity = []


year1 = 2002
year2 = 2020

for i in range(year1, year2 + 1):
    df_new = df[df['Retirement Year'] == i]
    print(i)
    print(df_new['Age'].describe())
    age.append(df_new['Age'].tolist())
    capacity.append(df_new['Nameplate Capacity (MW)'].tolist())

print(age)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 6))


ax1.boxplot(age)
ax2.boxplot(capacity)

ax1.set_xticklabels(np.arange(year1, year2 + 1))

plt.show()


# # plot figure
# fig, ax = plt.subplots(sharex=True, figsize=(12, 6))

# lw = 3

# m_size = 15
# l_size = 12

# source = 'Source: EIA           * 2020 Retirements as of Nov 2020'

# ax.bar(year, retire / 1000, color='black')
# ax.set_facecolor('#ECECEC')

# title = 'US Annual Coal Capacity Retirements\n'
# ax.set_title(title, fontsize=20)

# ax.set_ylabel('Capacity Retirements (GW)',
#               fontsize=m_size)

# plt.xticks(fontsize=l_size)
# plt.yticks(fontsize=l_size)

# ax.set_xlim([2004.5, 2020.5])
# ax.set_xticks(np.arange(2005, 2021, 1))

# plt.text(0.128, 0.01, source, fontsize=l_size,
#          transform=plt.gcf().transFigure)
# plt.text(0.894, 0.085, '*', fontsize=10, transform=plt.gcf().transFigure)


# plt.show()
