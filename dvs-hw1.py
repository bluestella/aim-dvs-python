import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import Papa as ppparse

df = pd.read_csv('./docs/Netflix Data Assessment.csv')

def getfirstcountry():
    firstCountry = ["USA", "India", "UK", "Canada", "Japan", "France", "S. Korea", "Spain", "Mexico"]
    return df[df['first_country'].isin(firstCountry)]


filteredData = getfirstcountry()

print(filteredData['first_country'].value_counts())
df_movies_count = filteredData.groupby(['first_country', 'target_ages']).size().reset_index(name="movie_count")
df_movies_count['total_country'] = df_movies_count.groupby('first_country')['movie_count'].transform('sum')
df_movies_count['percent_country'] = df_movies_count['movie_count'] / df_movies_count['total_country'] * 100

print(df_movies_count)



# Pivot the data for a stacked bar chart
pivot_df = df_movies_count.pivot(index='first_country', columns='target_ages', values='percent_country').fillna(0)

# Plot a horizontal stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))
pivot_df.plot(kind='barh', stacked=True, ax=ax)

# Add labels on each bar segment
for i, country in enumerate(pivot_df.index):
    cumulative = 0
    for j, age_group in enumerate(pivot_df.columns):
        value = pivot_df.loc[country, age_group]
        if value > 0:  # Only add label if value is greater than 0
            # Position label in the middle of the bar segment
            label_position = cumulative + value / 2
            # Show whole number percentage
            ax.text(label_position, i, f'{int(round(value))}%', 
                   ha='center', va='center', fontweight='bold', fontsize=9, color='#fff')
        cumulative += value

plt.title('Movie Count by First Country and Target Ages')
plt.xlabel('Percentage (%)')
plt.ylabel('First Country')
plt.legend(title='Target Ages', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
