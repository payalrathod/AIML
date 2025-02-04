import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


cs1 = pd.read_csv('Consultation2015 2016.csv')
cs2 = pd.read_csv('Consultation2016 2017.csv')
cs3 = pd.read_csv('Consultation2017 2018.csv')
cs = pd.read_csv('Consultation2018 2019bypayal.csv')
cs4 = pd.read_csv('Consultation2019 2020.csv')
cs5 = pd.read_csv('Consultation2020 2021.csv')
#print(cs)
#print(cs1)
# cs = pd.read_csv('Consultation2018 2019bypayal.csv', usecols=[1, 3, 5, 6, 7, 8])
# print(type(cs))
# print(cs.info())
# print(cs.head())

#cf = pd.melt(cs, id_vars=['Season', 'Region', 'Country', 'Clinical syndrome', 'YearWeek'], var_name='Fixed', value_name='Effect')
#print(cf.head())
#cg = cf.pivot_table(index=['Season', 'Region', 'Country', 'Clinical syndrome', 'YearWeek'], columns='Fixed', values='Effect')
# resetindex()
#print(cg)
#cs['id'] = range(len(cs))
#cs1['id'] = range(len(cs1))
#print(pd.concat([cs, cs1]))
#combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

df = pd.concat([cs1,cs2,cs3,cs,cs4,cs5],axis=0,ignore_index=False)
df.reset_index(inplace=True)
df.to_csv('ConsultationCleaned.csv')

m1 = pd.read_csv('ConsultationCleaned.csv')
#print(m1)
df1 = pd.melt(m1)
print(df1)

#print(cs)
#ch = cs.merge(cs1)
#print(ch)
# ch = cg.drop_duplicates()
# print(ch)

matplotlib.pyplot.show()
