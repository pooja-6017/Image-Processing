from turtle import color
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
ipl=pd.read_csv('data.csv')
'''print(ipl.head())
s=ipl.shape
print(s)
wonpl=ipl['player_of_match'].value_counts()
print(wonpl)
dis_top_pl=(ipl['player_of_match'].value_counts()[0:11])
print(dis_top_pl)
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), (ipl['player_of_match'].value_counts()[0:5]), color='purple')
plt.title("Top 5 players")
plt.show()
print(ipl['result'].value_counts())
print(ipl['toss_winner'].value_counts())'''
first_bat=ipl[ipl['win_by_runs']!=0]
print(first_bat.head())
#plt.hist(first_bat['win_by_runs'])
#plt.title("Histogram of Batting First")
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()), ipl['win_by_runs'].value_counts()[0:5].key(), color='pink')
plt.title("Bar of Batting First")

sec_bat=(ipl['win_by_wickets'].value_counts())
print(sec_bat)
plt.show()