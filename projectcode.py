import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from getpass import getpass

conn = sqlite3.connect('proj.db')
cursor = conn.cursor()



# Execute SQL queries and load results into Pandas DataFrames

# 1. tech m

# Data Analysis:

# 5. Analyze the percentage of deliverable volume for all stocks:
df_analysis_1 = pd.read_sql_query("SELECT Date, Perc_Deliverable FROM techm", conn)
print(df_analysis_1)

# 6. Study the number of trades executed for all stocks:
df_analysis_2 = pd.read_sql_query("SELECT Date, COUNT(*) AS num_trades FROM techm ", conn)
print(df_analysis_2)

# 7. Explore the relationship between trading volume and stock price movements for all stocks:
df_analysis_3 = pd.read_sql_query("SELECT Date, volume, close FROM techm ORDER BY Date", conn)
print(df_analysis_3)

# 8. Perform a comparative analysis of multiple stocks' VWAP:
df_analysis_4 = pd.read_sql_query("SELECT AVG(VWAP) AS avg_vwap FROM techm", conn)
print(df_analysis_4)

# 9. Calculate the daily turnover for all stocks:
df_aggregation_5 = pd.read_sql_query("SELECT Date, SUM(turnover) AS daily_turnover FROM techm GROUP BY Date", conn)
print(df_aggregation_5)




# 2.tcs

# Data Analysis:

# 5. Analyze the percentage of deliverable volume for all stocks:
df_analysis_7 = pd.read_sql_query("SELECT Date, Perc_Deliverable FROM tcs", conn)
print(df_analysis_7)

# 6. Study the number of trades executed for all stocks:
df_analysis_8 = pd.read_sql_query("SELECT Date, COUNT(*) AS num_trades FROM tcs ", conn)
print(df_analysis_8)

# 7. Explore the relationship between trading volume and stock price movements for all stocks:
df_analysis_9 = pd.read_sql_query("SELECT Date, volume, close FROM tcs ORDER BY Date", conn)
print(df_analysis_9)

# 8. Perform a comparative analysis of multiple stocks' VWAP:
df_analysis_10 = pd.read_sql_query("SELECT AVG(VWAP) AS avg_vwap FROM tcs", conn)
print(df_analysis_10)

# 9. Calculate the daily turnover for all stocks:
df_aggregation_11 = pd.read_sql_query("SELECT Date, SUM(turnover) AS daily_turnover FROM tcs GROUP BY Date", conn)
print(df_aggregation_11)





# Comparision by using visualization


# A.Data Analysis

# 1. Analyze the percentage of deliverable volume for all stocks:
# import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Convert 'date' column to datetime format
df_analysis_1['Date'] = pd.to_datetime(df_analysis_1['Date'])
df_analysis_7['Date'] = pd.to_datetime(df_analysis_7['Date'])

# Group by year and calculate the mean (or any other aggregation) for each year
da1_yearly = df_analysis_1.groupby(df_analysis_1['Date'].dt.year)['Perc_Deliverable'].mean()
da2_yearly = df_analysis_7.groupby(df_analysis_7['Date'].dt.year)['Perc_Deliverable'].mean()


# Plotting the relationship year-wise
plt.figure(figsize=(10, 6))

plt.plot(da1_yearly.index, da1_yearly.values, label='TECH M', marker='o', linestyle='-', linewidth=2)
plt.plot(da2_yearly.index, da2_yearly.values, label='TCS', marker='o', linestyle='-', linewidth=2)

plt.xlabel('Year')
plt.ylabel('Average Perc_Deliverable')
plt.title('Relationship between Year and Average Perc_Deliverable')
plt.legend()
plt.grid(True)

plt.show()


# 2. Study the number of trades executed for all stocks:

# import pandas as pd
# import matplotlib.pyplot as plt

# # Convert 'Date' columns to datetime format with the correct format
# df_analysis_2['Date'] = pd.to_datetime(df_analysis_2['Date'], format="%d-%m-%Y", errors='coerce')
# df_analysis_8['Date'] = pd.to_datetime(df_analysis_8['Date'], format="%d-%m-%Y", errors='coerce')

# # Create a new column 'Year'
# df_analysis_2['Year'] = df_analysis_2['Date'].dt.year
# df_analysis_8['Year'] = df_analysis_8['Date'].dt.year

# # Group by 'Year' and calculate the sum for each year
# df_analysis_2_grouped = df_analysis_2.groupby('Year')['num_trades'].sum()
# df_analysis_8_grouped = df_analysis_8.groupby('Year')['num_trades'].sum()

# # Plotting the comparative line plot for 'num_trades'
# plt.figure(figsize=(10, 6))

# plt.plot(df_analysis_2_grouped.index, df_analysis_2_grouped, label='techm', marker='o', linestyle='-', linewidth=2)
# plt.plot(df_analysis_8_grouped.index, df_analysis_8_grouped, label='tcs', marker='o', linestyle='-', linewidth=2)

# plt.xlabel('Year')
# plt.ylabel('Number of Trades')
# plt.title('Comparative Number of Trades between techm and tcs (Grouped by Year)')
# plt.legend()
# plt.grid(True)

# plt.show()


# 3. Explore the relationship between trading volume and stock price movements for all stocks:

# import pandas as pd
# import matplotlib.pyplot as plt

# # Convert 'Date' columns to datetime format with the correct format
# df_analysis_3['Date'] = pd.to_datetime(df_analysis_3['Date'], format="%d-%m-%Y", errors='coerce')
# df_analysis_9['Date'] = pd.to_datetime(df_analysis_9['Date'], format="%d-%m-%Y", errors='coerce')

# # Create a new column 'Year'
# df_analysis_3['Year'] = df_analysis_3['Date'].dt.year
# df_analysis_9['Year'] = df_analysis_9['Date'].dt.year

# # Group by 'Year' and calculate the mean for each year
# df_analysis_3_grouped = df_analysis_3.groupby('Year').mean()
# df_analysis_9_grouped = df_analysis_9.groupby('Year').mean()

# # Plotting the relationship year-wise
# plt.figure(figsize=(10, 6))

# plt.plot(df_analysis_3_grouped.index, df_analysis_3_grouped['Volume'], label='TECH M', marker='o', linestyle='-', linewidth=2)
# plt.plot(df_analysis_9_grouped.index, df_analysis_9_grouped['Volume'], label='TCS', marker='o', linestyle='-', linewidth=2)

# plt.xlabel('Year')
# plt.ylabel('Average Volume')
# plt.title('Comparative Relationship between Year and Average Volume')
# plt.legend()
# plt.grid(True)

# plt.show()

# # Plotting the comparative line plot for 'close'
# plt.figure(figsize=(10, 6))

# plt.plot(df_analysis_3_grouped.index, df_analysis_3_grouped['Close'], label='TECH M', marker='o', linestyle='-', linewidth=2)
# plt.plot(df_analysis_9_grouped.index, df_analysis_9_grouped['Close'], label='TCS', marker='o', linestyle='-', linewidth=2)

# plt.xlabel('Year')
# plt.ylabel('Average Close')
# plt.title('Comparative Relationship between Year and Average Close')
# plt.legend()
# plt.grid(True)

# plt.show()


# 4. Perform a comparative analysis of multiple stocks' VWAP:

# import pandas as pd
# import matplotlib.pyplot as plt

# # Group by the existing index (assumed to be 'Year')
# df_analysis_4_grouped = df_analysis_4.groupby(df_analysis_4.index).mean()
# df_analysis_10_grouped = df_analysis_10.groupby(df_analysis_10.index).mean()

# # Plotting the comparative line plot for 'avg_vwap'
# plt.figure(figsize=(10, 6))

# plt.plot(df_analysis_4_grouped.index, df_analysis_4_grouped['avg_vwap'], label='techm', marker='o', linestyle='-', linewidth=2)
# plt.plot(df_analysis_10_grouped.index, df_analysis_10_grouped['avg_vwap'], label='tcs', marker='o', linestyle='-', linewidth=2)

# plt.xlabel('Year')
# plt.ylabel('Average VWAP')
# plt.title('Comparative Average VWAP between techm and tcs (Grouped by Year)')
# plt.legend()
# plt.grid(True)

# plt.show()





# 5. Calculate the daily turnover for all stocks:

# import pandas as pd
# import matplotlib.pyplot as plt

# # Convert 'Date' columns to datetime format with the correct format
# df_aggregation_5['Date'] = pd.to_datetime(df_aggregation_5['Date'], format="%d-%m-%Y", errors='coerce')
# df_aggregation_11['Date'] = pd.to_datetime(df_aggregation_11['Date'], format="%d-%m-%Y", errors='coerce')

# # Group by year and sum the daily turnover for both DataFrames
# df_aggregation_5_grouped = df_aggregation_5.groupby(df_aggregation_5['Date'].dt.year)['daily_turnover'].sum()
# df_aggregation_11_grouped = df_aggregation_11.groupby(df_aggregation_11['Date'].dt.year)['daily_turnover'].sum()

# # Plotting the comparative line plot
# plt.figure(figsize=(10, 6))

# plt.plot(df_aggregation_5_grouped.index, df_aggregation_5_grouped, label='techm', marker='o', linestyle='-', linewidth=2)
# plt.plot(df_aggregation_11_grouped.index, df_aggregation_11_grouped, label='tcs', marker='o', linestyle='-', linewidth=2)

# plt.xlabel('Year')
# plt.ylabel('Total Daily Turnover')
# plt.title('Comparative Daily Turnover between techm and tcs')
# plt.legend()
# plt.grid(True)

# plt.show()


