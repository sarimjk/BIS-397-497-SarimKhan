# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:24:15 2020

@author: skhan
"""

import datetime
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# read in file
File = pd.read_csv("us-states.csv")

# convert formats
File['date'] = pd.to_datetime(File['date'],infer_datetime_format=True)
pd.set_option('display.float_format', lambda x: '%.0f' % x)


# Filter only PA
File['PA'] = File['state'] == "Pennsylvania"
File = File[File.PA == True]



# Adjusting April 21 and 22
File['Month'] = File['date'].dt.month
File['Day'] = File['date'].dt.day
File['adjusted_deaths'] = File['deaths']
File['adjusted_deaths'] = np.where((File['Month'] == 4) & (File['Day'] == 21),
                                   File['deaths']-282,File['deaths'] )
File['adjusted_deaths'] = np.where((File['Month'] == 4) & (File['Day'] == 22),
                                   File['adjusted_deaths']-297,File['adjusted_deaths'] )
File[['deaths','adjusted_deaths','date']]



# Plotting
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(15,7))
plt.bar(File.date,File.adjusted_deaths, color = 'red')
#plt.bar(File.date,File.deaths, color = 'red')
#set ticks every week
ax.xaxis.set_major_locator(mdates.WeekdayLocator())
#format date
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.set_title('PA Coronovirus Deaths')
ax.set_ylabel('Adjusted Deaths')
ax.set_xlabel('Date')
ax.set_title('PA Coronovirus Deaths')




""" Alternate way of plotting
plt.style.use('ggplot')
plt.bar(File['date'], File['adj_deaths'])
plt.grid(axis='y', alpha=0.75)
plt.xticks(fontsize=7)
plt.yticks(fontsize=10)
plt.ylabel('Adjusted deaths')
plt.xlabel('Date', fontsize = 10)
plt.title('PA Coronoavirus Deaths', fontsize = 15)
plt.show()

"""
