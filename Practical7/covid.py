#!/usr/bin/env python
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r"C:\Users\Admin\Documents\Smst2\IBI\IBI Prac\IBI1_2019-20\Practical7")
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:16:3,:])

all_countries=list(covid_data.iloc[:,1])
country_Bool=[]
for country in all_countries:
    if country =="Afghanistan":
        country_Bool.append(True)
    else:
        country_Bool.append(False)
print(covid_data.iloc[country_Bool,:])

country_Bool=[]
for country in all_countries:
    if country =="World":
        country_Bool.append(True)
    else:
        country_Bool.append(False)
world_dates=covid_data.iloc[country_Bool,0]
world_new_cases=covid_data.iloc[country_Bool,2]
world_new_deaths=covid_data.iloc[country_Bool,3]
print(np.mean(world_new_cases))
print(np.median(world_new_cases))
plt.plot(world_dates, world_new_cases, 'r+')
plt.plot(world_dates, world_new_deaths, 'r+')
plt.show()
plt.close()
plt.boxplot(world_new_cases)
plt.show()
plt.close()
S_Bool=[]
for country in all_countries:
    if country =="Spain":
        S_Bool.append(True)
    else:
        S_Bool.append(False)
S_new=list(covid_data.iloc[S_Bool,2])
S_all=list(covid_data.iloc[S_Bool,4])
S_dates=covid_data.iloc[S_Bool,0]
plt.plot(S_dates, S_new, 'r+')
plt.plot(S_dates, S_all, 'r+')
plt.show()
plt.close()