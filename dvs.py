import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data
df = pd.read_csv('docs/Netflix Data Assessment.csv')

# Define top countries to analyze
top_countries = ['USA', 'India', 'UK', 'Canada', 'Japan', 
                 'France', 'S. Korea', 'Spain', 'Mexico']

# Calculate proportions for each country
viz_data = []
for country in top_countries:
    country_df = df[df['first_country'] == country]
    total = len(country_df)
    
    age_counts = country_df['target_ages'].value_counts()
    
    viz_data.append({
        'Country': country,
        'Total': total,
        'Kids': (age_counts.get('Kids', 0) / total * 100),
        'Older Kids': (age_counts.get('Older Kids', 0) / total * 100),
        'Teens': (age_counts.get('Teens', 0) / total * 100),
        'Adults': (age_counts.get('Adults', 0) / total * 100)
    })

result_df = pd.DataFrame(viz_data)

# Sort by adult content percentage for better visualization
result_df = result_df.sort_values('Adults', ascending=True)

# Create the first visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Define age groups and colors
age_groups = ['Kids', 'Older Kids', 'Teens', 'Adults']
colors = ['#8dd3c7', '#bebada', '#fb8072', '#80b1d3']

# Create horizontal stacked bar chart
countries = result_df['Country']
y_pos = np.arange(len(countries))
left = np.zeros(len(countries))

for idx, age_group in enumerate(age_groups):
    values = result_df[age_group]
    bars = ax.barh(y_pos, values, left=left, height=0.7, 
                   label=age_group, color=colors[idx], 
                   edgecolor='white', linewidth=1.5)
    
    # Add percentage labels for segments >= 10%
    for i, (val, l) in enumerate(zip(values, left)):
        if val >= 10:
            ax.text(l + val/2, i, f'{val:.0f}%', 
                   ha='center', va='center', 
                   fontsize=10, fontweight='bold', color='white')
    
    left += values

# Formatting
ax.set_yticks(y_pos)
ax.set_yticklabels(countries, fontsize=11)
ax.set_xlabel('Percentage of Content (%)', fontsize=12, fontweight='bold')
ax.set_xlim(0, 100)
ax.set_xticks(range(0, 101, 10))
ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=0.5)
ax.set_axisbelow(True)

# Title and subtitle
fig.suptitle('Netflix Content by Target Age Group Across Countries', 
             fontsize=16, fontweight='bold', y=0.98)
ax.text(0.5, 1.02, 'Countries ordered by adult content proportion (Spain and Mexico are heavily adult-focused, India is teen-focused)', 
        transform=ax.transAxes, ha='center', fontsize=10, 
        style='italic', color='#666666')

# Legend
ax.legend(title='Target Age Group', loc='upper right', 
         frameon=True, fontsize=10, title_fontsize=11)

# Add sample size annotations
for i, (country, total) in enumerate(zip(countries, result_df['Total'])):
    ax.text(102, i, f'n={total}', ha='left', va='center', 
           fontsize=9, color='#666666')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('netflix_target_ages_improved.png', dpi=300, bbox_inches='tight')
plt.show()

# Additional analysis: Create a grouped bar chart for direct comparison
fig2, ax2 = plt.subplots(figsize=(14, 8))

# Set width of bars
bar_width = 0.2
x = np.arange(len(age_groups))

# Plot bars for each country (focusing on key comparison)
comparison_countries = ['USA', 'UK', 'India', 'Japan', 'Spain']
comparison_colors = ['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e', '#9467bd']

for idx, country in enumerate(comparison_countries):
    country_data = result_df[result_df['Country'] == country]
    values = [country_data[ag].values[0] for ag in age_groups]
    offset = (idx - len(comparison_countries)/2) * bar_width + bar_width/2
    bars = ax2.bar(x + offset, values, bar_width, 
                   label=country, color=comparison_colors[idx], alpha=0.8)
    
    # Add value labels on bars
    for bar, val in zip(bars, values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{val:.0f}%', ha='center', va='bottom', fontsize=9)

# Formatting
ax2.set_ylabel('Percentage of Content (%)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Target Age Group', fontsize=12, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(age_groups, fontsize=11)
ax2.set_ylim(0, 90)
ax2.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.5)
ax2.set_axisbelow(True)

# Title
fig2.suptitle('Direct Comparison: Content Distribution by Target Age', 
              fontsize=16, fontweight='bold', y=0.98)
ax2.text(0.5, 1.02, 'USA and UK show similar patterns with balanced distribution, while India heavily targets teens and Spain targets adults', 
         transform=ax2.transAxes, ha='center', fontsize=10, 
         style='italic', color='#666666')

# Legend
ax2.legend(title='Country', loc='upper right', frameon=True, 
          fontsize=10, title_fontsize=11, ncol=2)

# Remove top and right spines
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('netflix_target_ages_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n=== SUMMARY INSIGHTS ===")
print("\nKey Patterns:")
print("1. Adult-Focused Markets: Spain (82%), Mexico (77%), France (62%)")
print("2. Teen-Focused Markets: India (56%)")
print("3. Balanced Markets: USA, UK, Canada (roughly 50% adults, rest distributed)")
print("\nThe visualization principle applied:")
print("- Horizontal bars for easy comparison")
print("- Sequential ordering to reveal patterns")
print("- Muted, distinguishable colors")
print("- Direct labeling to reduce cognitive load")
print("- Clean, minimal design focusing on data")