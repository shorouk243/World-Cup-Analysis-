#!/usr/bin/env python
# coding: utf-8

# In[13]:


# !pip install matplotlib


# # Import Library 

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# In[3]:


df = pd.read_csv("/Users/shero/Documents/Artificial Intelligence/Machine Learning/World Cup Analysis/CWC23_all_innings.csv")


# In[4]:


df


# # Data Cleaning 

# In[5]:


duplicate = df [df.duplicated()]
duplicate 


# In[6]:


df.info()


# In[7]:


df.isnull().all()


# In[8]:


df.fillna(0, inplace=True)


# In[9]:


df['runs'] = df['runs'].astype(float)
df['bb_bf'] = df['bb_bf'].astype(float)
df['inns'] = df['inns'].astype(float)


# In[10]:


df.info()


# In[11]:


df


# In[12]:


df.isnull().sum()


# # Tasks

# **1.Team Performance Analysis:

# **Explore team-wise performance metrics.

# In[14]:


df["team"].value_counts()


# In[35]:


team_runs = df.groupby("team")["runs"].sum()
team_runs.sort_values(ascending = False).plot(kind='bar', color='skyblue')
plt.title('Total Runs Scored by Each Team')
plt.xlabel("Team")
plt.ylabel("Total Runs")
plt.show()
team_runs = df.groupby("team")["runs"].max()
print(team_runs)


# In[36]:


team_runs_avg = df.groupby("team")["runs"].mean()
team_runs_avg.sort_values(ascending = False).plot(kind='bar', color='skyblue')
plt.title('Average Runs per Match for Each Team')
plt.xlabel("Team")
plt.ylabel("Total Runs")
plt.show()
print(team_runs_avg)


# In[47]:


team_wickets = df.groupby("team")["wkts"].sum()
team_wickets.sort_values(ascending = False).plot(kind='bar', color='skyblue')
plt.title('Total wickets taken by each team')
plt.xlabel("Team")
plt.ylabel("Total wickets")
plt.show()
team_wickets = df.groupby("team")["wkts"].max()
print(team_wickets)


# In[21]:


import pandas as pd
team_group = df.groupby('team')
Total_runs = team_group['runs'].sum()
Average_runs = team_group['runs'].mean()
Highest_score = team_group['runs'].max()
team_performance = pd.DataFrame({
    'Total Runs': Total_runs,
    'Average Runs': Average_runs,
    'Highest Score':Highest_score
})
print(team_performance)


# **Analyze runs scored, wickets taken, and batting/bowling styles.**

# In[48]:


plt.figure(figsize=(10, 6))
team_runs.sort_values(ascending = False).plot(kind='bar', color='skyblue')
# plt.hist(team_runs, bins=30 , color ='maroon')
plt.title('Maximum Runs by Each Team')
plt.xlabel('Team')
plt.ylabel('Total runs')
plt.show()


# In[51]:


# plt.hist(team_wickets, bins=30 , color ='maroon')
team_wickets.sort_values(ascending = False).plot(kind='bar', color='skyblue')
plt.title('Maximum wickets')
plt.xlabel('Team')
plt.ylabel('Total wickets')
plt.show()


# In[25]:


total_runs = df['runs'].sum()
average_runs_per_match = df['runs'].mean()
total_wickets = df['wkts'].sum()

batting_style = df.groupby('bat_or_bowl')['runs'].agg(['sum', 'mean'])
batting_style.columns = ['Total Runs', 'Average Runs']

bowling_style = df.groupby('bat_or_bowl')['wkts'].agg(['sum', 'mean'])
bowling_style.columns = ['Total Runs', 'Average Runs']

print("\nBatting Style:")
print(batting_style)
print("\nBowling Style:")
print(bowling_style)

print("\t")
print("Overall Analysis:")
print(f"Total Runs: {total_runs}")
print(f"Average Runs per Match: {average_runs_per_match}")
print(f"Total Wickets Taken: {total_wickets}")


# **Identify Top-performing Teams and Their Strengths

# In[65]:


team_group = df.groupby('team')
total_runs = team_group['runs'].sum()
total_wickets = team_group['wkts'].sum()

batting_average = total_runs / team_group.size()
bowling_average = total_wickets / team_group.size()

top_runs = total_runs.nlargest(5) 
top_wickets = total_wickets.nlargest(5) 
top_batting_average = batting_average.nlargest(5)
top_bowling_average = bowling_average.nlargest(5)


print("Top performing teams based on total runs:")
print(top_runs)
print("\nTop performing teams based on total wickets taken:")
print(top_wickets)
print("\nTop performing teams based on batting average:")
print(top_batting_average)
print("\nTop performing teams based on bowling average:")
print(top_bowling_average)


# **2.Player Performance Analysis:

# **Evaluate individual player statistics for both batting and bowling.

# In[157]:


batting_stats = df.groupby('player')['runs'].agg(['sum', 'mean', 'max'])
bowling_stats = df.groupby('player')['wkts'].agg(['sum', 'mean', 'max'])

batting_stats.columns = ['Total Runs', 'Average Runs', 'Highest Score']
bowling_stats.columns = ['Total Wickets', 'Average Wickets', 'Best Highest ']

print("Batting Analysis:")
print(batting_stats)

print("\nBowling Analysis:")
print(bowling_stats)


# **Identify leading run-scorers and wicket-takers.

# In[166]:


player = df.groupby('player')
ptotal_runs = player['runs'].sum().nlargest(5) 
ptotal_wickets = player['wkts'].sum().nlargest(5) 

print("Top performing players based on total Run-scorers:")
print(ptop_runs)
print("\nTop performing players based on total Wicket-takers:")
print(ptop_wickets)


# **Assess the impact of players on their team's performance.

# In[67]:


team_totals = df.groupby('team').agg({'runs': 'sum', 'wkts': 'sum'})
team_averages = df.groupby('team').agg({'runs': 'mean', 'wkts': 'mean'})

df['RelativeRuns'] = df['runs'] / team_totals.loc[df['team'], 'runs'].values * 100
df['RelativeWickets'] = df['wkts'] / team_totals.loc[df['team'], 'wkts'].values * 100

player_impact = df.groupby('player').agg({'RelativeRuns': 'mean', 'RelativeWickets': 'mean'})

print("Player Impact on Team Performance:")
print(player_impact)


# **3.Opposition and Ground Analysis:

# **Investigate how teams and players perform against different oppositions.

# In[213]:


team_performance = df.groupby(['team', 'opposition']).agg({'runs': 'sum', 'wkts': 'sum'})
player_performance = df.groupby(['player', 'opposition']).agg({'runs': 'sum', 'wkts': 'sum'})

print("Team Performance against Different Oppositions:")
print(team_performance)
print("\nPlayer Performance against Different Oppositions:")
print(player_performance)


# **Examine performance variations across different playing grounds.

# In[212]:


team_performance = df.groupby(['team', 'ground']).agg({'runs': 'sum', 'wkts': 'sum'})
player_performance = df.groupby(['player', 'ground']).agg({'runs': 'sum', 'wkts': 'sum'})

print("Team Performance against Different Ground:")
print(team_performance)
print("\nPlayer Performance against Different Ground:")
print(player_performance)


# **Identify if there are specific teams or players that excel in certain conditions.

# In[72]:


team_performance = df.groupby(['team', 'ground']).agg({'runs': 'sum', 'wkts': 'sum'})
top_scoring_teams = team_performance.groupby('ground')['runs'].idxmax()
top_wicket_taking_teams = team_performance.groupby('ground')['wkts'].idxmax()

player_performance = df.groupby(['player', 'ground']).agg({'runs': 'sum', 'wkts': 'sum'})
top_scoring_players = player_performance.groupby('ground')['runs'].idxmax()
top_wicket_taking_players = player_performance.groupby('ground')['wkts'].idxmax()

teams_excelling = pd.DataFrame({
    'Top Runs Team': top_scoring_teams.str[0],
    'Top Wicket-Taking Team': top_wicket_taking_teams.str[0]
}, index=top_scoring_teams.index)

players_excelling = pd.DataFrame({
    'Top Runs Player': top_scoring_players.str[0],
    'Top Wicket-Taking Player': top_wicket_taking_players.str[0]
}, index=top_scoring_players.index)

print("Teams in Specific Conditions:")
print(teams_excelling)
print("\nPlayers in Specific Conditions:")
print(players_excelling)


# **4.Temporal Analysis:

# **Study performance trends over time, considering start dates and overs played.

# In[257]:


performance_trends_over_time = df.groupby('start_date')['overs'].mean()

performance_trends_over_time.plot(kind='line', figsize=(10, 6) , color ='maroon')
plt.title('performance trends over time')
plt.xlabel('Start Date')
plt.ylabel('Overs Played')
plt.show()


# **Identify any temporal patterns or changes in team and player performance.

# In[259]:


df['start_date'] = pd.to_datetime(df['start_date'])

df = df.sort_values('start_date')

team_performance = df.groupby(['start_date', 'team']).agg({'runs': 'sum', 'wkts': 'sum'})

player_performance = df.groupby(['start_date', 'player']).agg({'runs': 'sum', 'wkts': 'sum'})

average_runs_per_day_teams = team_performance.groupby('start_date')['runs'].mean()

average_wickets_per_day_teams = team_performance.groupby('start_date')['wkts'].mean()

average_runs_per_day_players = player_performance.groupby('start_date')['runs'].mean()

average_wickets_per_day_players = player_performance.groupby('start_date')['wkts'].mean()

average_runs_per_day_teams.plot(kind='line', figsize=(10, 6), xlabel='Start Date', ylabel='Average Runs Scored',
                               title='Average Runs Scored per Day for Teams')

average_wickets_per_day_teams.plot(kind='line', figsize=(10, 6), xlabel='Start Date', ylabel='Average Wickets Taken',
                                  title='Average Wickets Taken per Day for Teams')

average_runs_per_day_players.plot(kind='line', figsize=(10, 6), xlabel='Start Date', ylabel='Average Runs Scored',
                                  title='Average Runs Scored per Day for Players')

average_wickets_per_day_players.plot(kind='line', figsize=(10, 6), xlabel='Start Date', ylabel='Average Wickets Taken',
                                     title='Average Wickets Taken per Day for Players')

plt.show()

