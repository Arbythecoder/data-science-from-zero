"""
Week 3, Day 2 Practice: Seaborn & Statistical Visualizations
Complete solutions for all 3 exercises

Topics covered:
- Histograms with KDE
- Box plots for outlier detection
- Heatmaps for correlations
- Multi-panel dashboards
- Statistical distributions
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set style
sns.set_style('whitegrid')
sns.set_palette('husl')

print("=" * 60)
print("WEEK 3, DAY 2 PRACTICE - SEABORN STATISTICAL PLOTS")
print("=" * 60)

# =============================================================================
# EXERCISE 1: CUSTOMER AGE DISTRIBUTION (WARMUP)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE 1: CUSTOMER AGE DISTRIBUTION")
print("=" * 60)

# Customer ages (realistic distribution)
np.random.seed(123)
customer_ages = np.random.gamma(4, 8, 500)

# Calculate statistics
median_age = np.median(customer_ages)
mean_age = np.mean(customer_ages)
std_age = np.std(customer_ages)

# Create histogram with KDE
plt.figure(figsize=(12, 6))
sns.histplot(customer_ages, bins=25, kde=True, color='steelblue', edgecolor='black')

# Add vertical line at median
plt.axvline(median_age, color='red', linestyle='--', linewidth=2,
            label=f'Median: {median_age:.1f} years')
plt.axvline(mean_age, color='green', linestyle='--', linewidth=2,
            label=f'Mean: {mean_age:.1f} years')

# Customize
plt.title('Customer Age Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Age', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('exercise1_age_distribution.png', dpi=300, bbox_inches='tight')

# Analysis
print("\n✓ Histogram with KDE created successfully!")
print(f"\nAGE STATISTICS:")
print(f"  - Mean age: {mean_age:.2f} years")
print(f"  - Median age: {median_age:.2f} years")
print(f"  - Std deviation: {std_age:.2f} years")
print(f"  - Age range: {customer_ages.min():.1f} - {customer_ages.max():.1f} years")

# Find most common age range
percentile_25 = np.percentile(customer_ages, 25)
percentile_75 = np.percentile(customer_ages, 75)
print(f"\n  MOST CUSTOMERS: {percentile_25:.1f} - {percentile_75:.1f} years (middle 50%)")
print(f"  - Saved as: exercise1_age_distribution.png")

plt.show()

# =============================================================================
# EXERCISE 2: DEPARTMENT PERFORMANCE (APPLICATION)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE 2: DEPARTMENT SALES PERFORMANCE")
print("=" * 60)

# Sales data
np.random.seed(42)
dept_sales = pd.DataFrame({
    'Department': np.repeat(['Electronics', 'Clothing', 'Food', 'Home'], 60),
    'Daily_Sales': np.concatenate([
        np.random.normal(15000, 3000, 60),
        np.random.normal(8000, 2000, 60),
        np.random.normal(12000, 2500, 60),
        np.random.normal(10000, 2200, 60)
    ])
})

# Calculate statistics by department
dept_stats = dept_sales.groupby('Department')['Daily_Sales'].agg([
    'mean', 'median', 'std', 'min', 'max'
]).round(0)

# Create horizontal box plot
plt.figure(figsize=(12, 7))
sns.boxplot(data=dept_sales, y='Department', x='Daily_Sales',
            palette='Set2', orient='h')

plt.title('Sales Performance by Department', fontsize=16, fontweight='bold')
plt.xlabel('Daily Sales ($)', fontsize=12)
plt.ylabel('Department', fontsize=12)

# Add mean markers
for i, dept in enumerate(['Clothing', 'Electronics', 'Food', 'Home']):
    mean_val = dept_sales[dept_sales['Department'] == dept]['Daily_Sales'].mean()
    plt.plot(mean_val, i, 'D', markersize=10, color='red',
             label='Mean' if i == 0 else '')

plt.legend()
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('exercise2_department_performance.png', dpi=300, bbox_inches='tight')

print("\n✓ Box plot created successfully!")
print("\nDEPARTMENT STATISTICS:")
print("=" * 60)
print(dept_stats.to_string())

# Analyze consistency and outliers
print("\n" + "=" * 60)
print("BUSINESS INSIGHTS:")
print("=" * 60)

most_consistent = dept_stats['std'].idxmin()
least_consistent = dept_stats['std'].idxmax()
highest_avg = dept_stats['mean'].idxmax()

print(f"\n✓ Highest Average Sales: {highest_avg} (${dept_stats.loc[highest_avg, 'mean']:,.0f}/day)")
print(f"✓ Most Consistent: {most_consistent} (σ = ${dept_stats.loc[most_consistent, 'std']:,.0f})")
print(f"✓ Least Consistent: {least_consistent} (σ = ${dept_stats.loc[least_consistent, 'std']:,.0f})")

# Count outliers (values beyond 1.5 * IQR)
for dept in dept_stats.index:
    dept_data = dept_sales[dept_sales['Department'] == dept]['Daily_Sales']
    Q1 = dept_data.quantile(0.25)
    Q3 = dept_data.quantile(0.75)
    IQR = Q3 - Q1
    outliers = dept_data[(dept_data < Q1 - 1.5*IQR) | (dept_data > Q3 + 1.5*IQR)]
    if len(outliers) > 0:
        print(f"\n  {dept} has {len(outliers)} outlier(s) - investigate unusual days!")

print(f"\n  - Saved as: exercise2_department_performance.png")
plt.show()

# =============================================================================
# EXERCISE 3: MULTI-VARIABLE ANALYSIS DASHBOARD (REAL-WORLD)
# =============================================================================

print("\n" + "=" * 60)
print("EXERCISE 3: WEBSITE METRICS DASHBOARD")
print("=" * 60)

# Website metrics
np.random.seed(42)
web_data = pd.DataFrame({
    'Page_Views': np.random.poisson(500, 100),
    'Time_on_Site': np.random.normal(180, 60, 100),  # seconds
    'Bounce_Rate': np.random.beta(2, 5, 100) * 100,   # percentage
    'Conversions': np.random.poisson(15, 100)
})

# Create 2x2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Page Views Distribution (Histogram)
sns.histplot(web_data['Page_Views'], bins=20, kde=True,
             color='skyblue', ax=axes[0, 0])
axes[0, 0].set_title('Page Views Distribution', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Page Views')
axes[0, 0].axvline(web_data['Page_Views'].mean(), color='red',
                   linestyle='--', label=f'Mean: {web_data["Page_Views"].mean():.0f}')
axes[0, 0].legend()

# Plot 2: Time on Site vs Bounce Rate (Scatter)
scatter = axes[0, 1].scatter(web_data['Time_on_Site'],
                             web_data['Bounce_Rate'],
                             c=web_data['Conversions'],
                             s=100, alpha=0.6, cmap='viridis')
axes[0, 1].set_title('Time on Site vs Bounce Rate', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Time on Site (seconds)')
axes[0, 1].set_ylabel('Bounce Rate (%)')
plt.colorbar(scatter, ax=axes[0, 1], label='Conversions')
axes[0, 1].grid(True, alpha=0.3)

# Plot 3: Correlation Heatmap
correlation = web_data.corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, square=True, linewidths=2, ax=axes[1, 0],
            cbar_kws={'label': 'Correlation'})
axes[1, 0].set_title('Metrics Correlation', fontsize=14, fontweight='bold')

# Plot 4: Conversions Distribution (Box Plot)
sns.boxplot(y=web_data['Conversions'], color='lightcoral', ax=axes[1, 1])
axes[1, 1].set_title('Conversions Distribution', fontsize=14, fontweight='bold')
axes[1, 1].set_ylabel('Conversions')
axes[1, 1].axhline(web_data['Conversions'].mean(), color='green',
                   linestyle='--', label=f'Mean: {web_data["Conversions"].mean():.1f}')
axes[1, 1].legend()

plt.suptitle('Website Metrics Dashboard', fontsize=18, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('web_metrics_dashboard.png', dpi=300, bbox_inches='tight')

print("\n✓ Dashboard created successfully!")

# Display correlations
print("\nCORRELATION MATRIX:")
print("=" * 60)
print(correlation.to_string())

# Insights
print("\n" + "=" * 60)
print("KEY INSIGHTS FROM DASHBOARD:")
print("=" * 60)

strongest_corr = correlation.abs().unstack().sort_values(ascending=False)
strongest_corr = strongest_corr[strongest_corr < 1].iloc[0:3]

print("\nTop 3 Correlations:")
for idx, (pair, value) in enumerate(strongest_corr.items(), 1):
    print(f"{idx}. {pair[0]} ↔ {pair[1]}: {value:.3f}")

# Time on site analysis
avg_time = web_data['Time_on_Site'].mean()
high_time = web_data[web_data['Time_on_Site'] > avg_time]
low_time = web_data[web_data['Time_on_Site'] <= avg_time]

print(f"\nTime on Site Analysis:")
print(f"  - Average time: {avg_time:.1f} seconds")
print(f"  - High engagement sessions: {len(high_time)} ({len(high_time)}%)")
print(f"    → Avg conversions: {high_time['Conversions'].mean():.2f}")
print(f"  - Low engagement sessions: {len(low_time)} ({len(low_time)}%)")
print(f"    → Avg conversions: {low_time['Conversions'].mean():.2f}")

# Bounce rate analysis
avg_bounce = web_data['Bounce_Rate'].mean()
print(f"\nBounce Rate Analysis:")
print(f"  - Average bounce rate: {avg_bounce:.1f}%")
print(f"  - Sessions with <30% bounce: {len(web_data[web_data['Bounce_Rate'] < 30])}")
print(f"  - Sessions with >50% bounce: {len(web_data[web_data['Bounce_Rate'] > 50])}")

print(f"\n  - Saved as: web_metrics_dashboard.png")
plt.show()

# =============================================================================
# BONUS: ADVANCED VISUALIZATIONS
# =============================================================================

print("\n" + "=" * 60)
print("BONUS: PAIR PLOT FOR MULTIVARIATE ANALYSIS")
print("=" * 60)

# Create pair plot
pair_plot = sns.pairplot(web_data, diag_kind='kde', plot_kws={'alpha': 0.6})
pair_plot.fig.suptitle('Website Metrics - Pairwise Relationships',
                       y=1.02, fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('web_metrics_pairplot.png', dpi=300, bbox_inches='tight')

print("\n✓ Pair plot created!")
print("  - Shows all pairwise relationships at once")
print("  - Diagonal shows distributions")
print("  - Off-diagonal shows scatter plots")
print("  - Saved as: web_metrics_pairplot.png")
plt.show()

# =============================================================================
# BONUS 2: VIOLIN PLOT COMPARISON
# =============================================================================

print("\n" + "=" * 60)
print("BONUS 2: COMPARING DIFFERENT VISUALIZATION TYPES")
print("=" * 60)

# Create comparison of box vs violin for conversions
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Box plot
sns.boxplot(y=web_data['Conversions'], color='lightblue', ax=axes[0])
axes[0].set_title('Box Plot', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Conversions')

# Violin plot
sns.violinplot(y=web_data['Conversions'], color='lightgreen', ax=axes[1])
axes[1].set_title('Violin Plot', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Conversions')

# Histogram
sns.histplot(y=web_data['Conversions'], bins=15, kde=True,
             color='salmon', ax=axes[2])
axes[2].set_title('Histogram', fontsize=14, fontweight='bold')
axes[2].set_ylabel('Conversions')

plt.suptitle('Conversion Distribution: Different Visualizations',
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('comparison_plots.png', dpi=300, bbox_inches='tight')

print("\n✓ Comparison plots created!")
print("  - Box plot: Shows quartiles and outliers")
print("  - Violin plot: Shows full distribution shape")
print("  - Histogram: Shows frequency bins")
print("  - Saved as: comparison_plots.png")
plt.show()

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 60)
print("PRACTICE COMPLETE! 🎉")
print("=" * 60)

print("\nFiles created:")
print("  1. exercise1_age_distribution.png")
print("  2. exercise2_department_performance.png")
print("  3. web_metrics_dashboard.png")
print("  4. web_metrics_pairplot.png (bonus)")
print("  5. comparison_plots.png (bonus)")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("✓ Histograms show distribution shape")
print("✓ KDE curves smooth distribution visualization")
print("✓ Box plots identify outliers and quartiles")
print("✓ Heatmaps reveal correlations")
print("✓ Multi-panel dashboards tell complete stories")
print("✓ Seaborn provides beautiful defaults")
print("✓ Statistical visualizations support data-driven decisions")

print("\n" + "=" * 60)
print("READY FOR DAY 3: REAL-WORLD PROJECT!")
print("=" * 60)
