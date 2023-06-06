import pandas as pd
import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt

df_temp = pd.read_csv(r'tempYearly.csv')
df_rain = pd.read_csv(r'rainYearly.csv')

#print(df_temp)
#print(df_rain)

#Filter
df_temp_f = df_temp.query('Temperature < 40 & Temperature > 0')
#df_temp_f.plot.scatter(x='Year', y="Temperature", label = 'Temperature and Year')

#plt.show()

df_rain_f = df_rain.query('Rainfall < 6 & Rainfall > 0')
#df_rain_f.plot.scatter(x='Year', y='Rainfall', label='Rainfall and Year')

#plt.show()

#merge
df_merge = pd.merge(df_temp_f, df_rain_f, on='Year', how='inner')

#sort
print(df_merge.sort_values(by='Temperature'))
print(df_merge.sort_values(by='Temperature', ascending=False))
print(df_merge.sort_values(by='Rainfall'))
print(df_merge.sort_values(by='Rainfall', ascending=False))

#config window size of plot in seaborn
sns.set(rc={'figure.figsize':(12,6)})

#regression plot
sns.jointplot('Rainfall', 'Temperature', data = df_merge, kind = 'reg')

#ploting
plt.show()