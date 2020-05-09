#!/usr/bin/env python
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#os.chdir("D:\\Smst2\\IBI1B\\IBI1_2019-20\\Practical7\\")
covid_data = pd.read_csv("full_data.csv")
# Print all colums and every third row between (and including) 0 and 15
print(covid_data.iloc[0:16:3,:])
all_countries=list(covid_data.iloc[:,1])
# A Boolean to show “total cases” for all rows corresponding to Afghanistan.
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
# Mean and median of new cases for the entire world.
print(np.mean(world_new_cases))
print(np.median(world_new_cases))
# Both new cases and new deaths worldwide.
plt.title("Both new cases and new deaths worldwide.")
plt.xlabel("Date")
plt.ylabel("Number")
plt.plot(world_dates, world_new_cases, 'r',label="World new cases")
plt.plot(world_dates, world_new_deaths, 'b',label="World new deaths")
plt.xticks(world_dates,rotation=90)
legend = plt.legend(loc='upper right', shadow=True)
plt.show()
plt.close()
# Boxplot of new cases worldwide.
plt.title("New cases worldwide.")
plt.xlabel("Date")
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
plt.title("Both new cases and total cases in Spain.")
plt.xlabel("Date")
plt.ylabel("Number")
plt.plot(S_dates, S_new, 'r',label="Spain new cases")
plt.plot(S_dates, S_all, 'b',label="Spain total cases")
plt.xticks(S_dates,rotation=90)
legend = plt.legend(loc='upper right', shadow=True)
plt.show()
plt.close()
