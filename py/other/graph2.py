import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.text as mtext

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 100)

# call file function


def call_file(path):
    data = pd.read_csv(path)
    return pd.DataFrame(data)


# call file
path = '/Users/nathanoliver/Desktop/Python/Rhodium/csv/06_november_generator_2020.csv'
path2 = '/Users/nathanoliver/Desktop/Python/Coal_Retirements/csv/november_generator_2020_active.csv'
df = call_file(path)
df2 = call_file(path2)

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


col = ['Net Winter Capacity (MW)', 'Net Summer Capacity (MW)',
       'Nameplate Capacity (MW)', 'Planned Retirement Year']

for i in col:
    df2[i] = df2[i].replace(',', '', regex=True)
    df2[i] = df2[i].replace(' ', '', regex=True)
    df2[i] = pd.to_numeric(df2[i], downcast="float")


# determine the total capacity requirements for each year
df2 = df2.reset_index(drop=True)


# replace null values with Nameplate Capacity
for i in range(len(df2)):
    n1 = df2.loc[i, 'Net Winter Capacity (MW)']
    n2 = df2.loc[i, 'Net Summer Capacity (MW)']

    if pd.isna(n1) == True:
        df2.loc[i, 'Net Winter Capacity (MW)'] = df2.loc[i,
                                                         'Nameplate Capacity (MW)']
    if pd.isna(n2) == True:
        df2.loc[i, 'Net Summer Capacity (MW)'] = df2.loc[i,
                                                         'Nameplate Capacity (MW)']


df2 = df2[df2['Technology'] == 'Conventional Steam Coal']

print(df2)

print(df2['Planned Retirement Year'].value_counts())

# for i in range(2020, 2041):
# df_ne2 = df[df['Net Summer Capacity (MW)'] == 53]

# n = len(df_new)
# print(i, total, total / n)


df['Age'] = df['Retirement Year'] - df['Operating Year']
df2['Age'] = df2['Planned Retirement Year'] - df2['Operating Year']

age = []
capacity = []

age_min = []
age_25 = []
age_mean = []
age_75 = []
age_max = []

capacity_min = []
capacity_25 = []
capacity_mean = []
capacity_75 = []
capacity_max = []

age_min_future = []
age_25_future = []
age_mean_future = []
age_75_future = []
age_max_future = []

capacity_min_future = []
capacity_25_future = []
capacity_mean_future = []
capacity_75_future = []
capacity_max_future = []


year1 = 2002
year2 = 2020

for i in range(year1, year2 + 1):
    df_new = df[df['Retirement Year'] == i]
    print(i)
    print(df_new['Age'].describe())
    print(df_new['Nameplate Capacity (MW)'].describe())

    age_min.append(df_new['Age'].describe()['min'])
    age_25.append(df_new['Age'].describe()['25%'])
    age_mean.append(df_new['Age'].describe()['50%'])
    age_75.append(df_new['Age'].describe()['75%'])
    age_max.append(df_new['Age'].describe()['max'])

    capacity_min.append(df_new['Nameplate Capacity (MW)'].describe()['min'])
    capacity_25.append(df_new['Nameplate Capacity (MW)'].describe()['25%'])
    capacity_mean.append(df_new['Nameplate Capacity (MW)'].describe()['50%'])
    capacity_75.append(df_new['Nameplate Capacity (MW)'].describe()['75%'])
    capacity_max.append(df_new['Nameplate Capacity (MW)'].describe()['max'])


for i in range(2020, 2026):
    df_new = df2[df2['Planned Retirement Year'] == i]
    # total = df_new['Nameplate Capacity (MW)'].sum()

    age_25_future.append(df_new['Age'].describe()['25%'])
    age_mean_future.append(df_new['Age'].describe()['50%'])
    age_75_future.append(df_new['Age'].describe()['75%'])

    capacity_25_future.append(
        df_new['Nameplate Capacity (MW)'].describe()['25%'])
    capacity_mean_future.append(
        df_new['Nameplate Capacity (MW)'].describe()['50%'])
    capacity_75_future.append(
        df_new['Nameplate Capacity (MW)'].describe()['75%'])

year = np.arange(year1, year2 + 1)
year2 = np.arange(2020, 2026)


fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 6))

colors = ['red', 'black', 'blue']

# ax1.plot(year, age_min)


ax1.plot(year, age_mean, color=colors[1])
ax1.fill_between(year, age_25, age_75, color='grey', alpha=0.2)


ax1.plot(year2, age_mean_future, color=colors[0])
ax1.fill_between(year2, age_25_future, age_75_future, color='red', alpha=0.2)


ax2.plot([], [], alpha=0, label='Median')

a = ax2.plot(year, capacity_mean, color=colors[1], label='Retired')
b = ax2.fill_between(year, capacity_25, capacity_75,
                     color='grey', alpha=0.2, label='Retired')


c = ax2.plot(year2, capacity_mean_future,
             color=colors[0], label='Planned Retirements')
ax2.plot([], [], alpha=0, label='Quartile Range')
d = ax2.fill_between(year2, capacity_25_future, capacity_75_future,
                     color='red', alpha=0.2, label='Planned Retirements')


ax1.set_xlim(2002, 2025)
ax2.set_xlim(2002, 2025)

ax2.set_ylim(0, 650)

ax1.set_title('US Coal Power Plant Retirement Age and Capacity\n', size=18)

ax1.set_ylabel('Retirement Age (Years)', size=13)
ax2.set_ylabel('Retirement Capacity (MW)', size=13)

ax1.set_yticks(np.arange(40, 80, 10))
ax1.set_yticklabels(np.arange(40, 80, 10), size=13)
ax2.set_xticks(np.arange(2005, 2030, 5))
ax2.set_xticklabels(np.arange(2005, 2030, 5), size=13)
ax2.set_yticklabels(np.arange(0, 700, 100), size=13)


plt.text(0.748, 0.08, '*', fontsize=13, transform=plt.gcf().transFigure)
plt.text(0.1, 0.01, 'Source: EIA        * 2020 includes retired power plants and planned retirements, data as of Nov 2020', fontsize=10,
         transform=plt.gcf().transFigure)


ax2.legend(fontsize=11)


# ax1.fill_between(year, capacity_25, capacity_75, color=colors[2], alpha=0.2)


# ax2.plot(year, capacity_max)

# ax1.set_xticks(np.arange(year1, year2 + 1))


# handler_map={basestring: LegendTitle({'fontsize': 18})}
# ax2.legend([f, a, c, d, d, e, f])

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
