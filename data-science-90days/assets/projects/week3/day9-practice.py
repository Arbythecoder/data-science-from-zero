"""
Week 3, Day 3 Practice: Real-World COVID-19 Visualization Project
Complete implementation of COVID-19 data analysis dashboard

Topics covered:
- Time series visualization
- Multi-country comparison
- Correlation analysis
- Distribution analysis
- Moving averages
- Annotations and highlights
- Complete dashboard design
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# Set styling
sns.set_style('whitegrid')
sns.set_palette('husl')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

print("=" * 70)
print("WEEK 3, DAY 3 - COVID-19 GLOBAL IMPACT ANALYSIS PROJECT")
print("=" * 70)

# =============================================================================
# PART 1: DATA GENERATION
# =============================================================================

print("\n" + "=" * 70)
print("PART 1: GENERATING COVID-19 DATA")
print("=" * 70)

np.random.seed(42)

# Create date range
dates = pd.date_range(start='2020-03-01', end='2021-03-01', freq='D')

def generate_covid_data(country, peak_date, peak_cases, base_rate=100):
    """Generate realistic COVID-19 case progression"""
    cases = []
    for date in dates:
        days_from_start = (date - dates[0]).days
        days_from_peak = abs((date - peak_date).days)

        # Exponential growth then decline
        case_count = base_rate + (peak_cases * np.exp(-days_from_peak/30)) + \
                     np.random.normal(0, peak_cases * 0.1)
        case_count = max(0, case_count)  # No negative cases
        cases.append(case_count)

    return cases

# Generate data for 5 countries
countries_data = {
    'USA': generate_covid_data('USA', pd.Timestamp('2020-07-15'), 70000, 5000),
    'UK': generate_covid_data('UK', pd.Timestamp('2020-11-01'), 40000, 2000),
    'India': generate_covid_data('India', pd.Timestamp('2020-09-15'), 90000, 3000),
    'Brazil': generate_covid_data('Brazil', pd.Timestamp('2020-08-01'), 60000, 4000),
    'Germany': generate_covid_data('Germany', pd.Timestamp('2020-12-15'), 30000, 1500)
}

# Create DataFrame
covid_df = pd.DataFrame(countries_data, index=dates)
covid_df.index.name = 'Date'

print("\n✓ COVID-19 data generated successfully!")
print(f"  - Date range: {dates[0].date()} to {dates[-1].date()}")
print(f"  - Countries: {len(covid_df.columns)}")
print(f"  - Total days: {len(covid_df)}")
print(f"\nData preview:")
print(covid_df.head().to_string())
print(f"\nSummary statistics:")
print(covid_df.describe().to_string())

# =============================================================================
# PART 2: GLOBAL TREND ANALYSIS
# =============================================================================

print("\n" + "=" * 70)
print("PART 2: GLOBAL TREND LINE CHART")
print("=" * 70)

plt.figure(figsize=(14, 8))

# Plot each country
for country in covid_df.columns:
    plt.plot(covid_df.index, covid_df[country],
             label=country, linewidth=2, alpha=0.8)

# Customize
plt.title('COVID-19 Daily Cases: Global Comparison',
          fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Daily Cases', fontsize=14)
plt.legend(loc='upper right', fontsize=12)
plt.grid(True, alpha=0.3)

# Format x-axis dates
plt.gcf().autofmt_xdate()

# Add annotation for peak
max_country = covid_df.max().idxmax()
max_value = covid_df.max().max()
max_date = covid_df[max_country].idxmax()

plt.annotate(f'Peak: {max_country}\n{max_value:.0f} cases',
             xy=(max_date, max_value),
             xytext=(max_date - timedelta(days=60), max_value + 20000),
             arrowprops=dict(arrowstyle='->', color='red', lw=2),
             fontsize=12, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.savefig('covid_global_trends.png', dpi=300, bbox_inches='tight')

print("\n✓ Global trend chart created!")
print(f"  - Peak country: {max_country}")
print(f"  - Peak value: {max_value:.0f} cases")
print(f"  - Peak date: {max_date.date()}")
print("  - Saved as: covid_global_trends.png")
plt.show()

# =============================================================================
# PART 3: COUNTRY COMPARISON
# =============================================================================

print("\n" + "=" * 70)
print("PART 3: COUNTRY COMPARISON BAR CHARTS")
print("=" * 70)

# Calculate total and average cases
total_cases = covid_df.sum().sort_values(ascending=False)
avg_cases = covid_df.mean().sort_values(ascending=False)

# Create figure with two subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Subplot 1: Total Cases
colors = sns.color_palette('rocket', len(total_cases))
axes[0].bar(total_cases.index, total_cases.values, color=colors)
axes[0].set_title('Total COVID-19 Cases by Country',
                  fontsize=16, fontweight='bold')
axes[0].set_ylabel('Total Cases', fontsize=12)
axes[0].tick_params(axis='x', rotation=45)

# Add value labels on bars
for i, (country, value) in enumerate(total_cases.items()):
    axes[0].text(i, value, f'{value/1000:.0f}K',
                ha='center', va='bottom', fontweight='bold')

# Subplot 2: Average Daily Cases
axes[1].barh(avg_cases.index, avg_cases.values, color='coral')
axes[1].set_title('Average Daily Cases',
                  fontsize=16, fontweight='bold')
axes[1].set_xlabel('Average Daily Cases', fontsize=12)

# Add value labels
for i, (country, value) in enumerate(avg_cases.items()):
    axes[1].text(value, i, f' {value:.0f}',
                va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('covid_country_comparison.png', dpi=300, bbox_inches='tight')

print("\n✓ Country comparison charts created!")
print("\nTOTAL CASES RANKING:")
for i, (country, cases) in enumerate(total_cases.items(), 1):
    print(f"  {i}. {country}: {cases:,.0f} total cases")

print("\nAVERAGE DAILY CASES:")
for country, avg in avg_cases.items():
    print(f"  {country}: {avg:.0f} cases/day")

print("  - Saved as: covid_country_comparison.png")
plt.show()

# =============================================================================
# PART 4: CORRELATION HEATMAP
# =============================================================================

print("\n" + "=" * 70)
print("PART 4: CORRELATION ANALYSIS")
print("=" * 70)

# Calculate correlation
correlation = covid_df.corr()

# Create heatmap
plt.figure(figsize=(10, 8))

sns.heatmap(correlation,
            annot=True,
            fmt='.2f',
            cmap='coolwarm',
            center=0,
            square=True,
            linewidths=2,
            cbar_kws={'label': 'Correlation Coefficient'})

plt.title('COVID-19 Case Correlation Between Countries',
          fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('covid_correlation_heatmap.png', dpi=300, bbox_inches='tight')

print("\n✓ Correlation heatmap created!")
print("\nCORRELATION MATRIX:")
print(correlation.to_string())

# Find strongest correlations
print("\nSTRONGEST CORRELATIONS:")
corr_pairs = correlation.unstack()
corr_pairs = corr_pairs[corr_pairs < 1].sort_values(ascending=False)
for (c1, c2), corr in list(corr_pairs.items())[:5]:
    print(f"  {c1} ↔ {c2}: {corr:.3f}")

print("  - Saved as: covid_correlation_heatmap.png")
plt.show()

# =============================================================================
# PART 5: DISTRIBUTION ANALYSIS
# =============================================================================

print("\n" + "=" * 70)
print("PART 5: DISTRIBUTION ANALYSIS")
print("=" * 70)

# Prepare data for seaborn (need long format)
covid_long = covid_df.reset_index().melt(id_vars='Date',
                                          var_name='Country',
                                          value_name='Cases')

# Create figure with subplots
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# Subplot 1: Box Plot
sns.boxplot(data=covid_long, x='Country', y='Cases',
            palette='Set2', ax=axes[0])
axes[0].set_title('Case Distribution by Country - Box Plot',
                  fontsize=16, fontweight='bold')
axes[0].set_ylabel('Daily Cases', fontsize=12)
axes[0].set_xlabel('')

# Subplot 2: Violin Plot
sns.violinplot(data=covid_long, x='Country', y='Cases',
               palette='muted', ax=axes[1])
axes[1].set_title('Case Distribution by Country - Violin Plot',
                  fontsize=16, fontweight='bold')
axes[1].set_ylabel('Daily Cases', fontsize=12)
axes[1].set_xlabel('Country', fontsize=12)

plt.tight_layout()
plt.savefig('covid_distribution_analysis.png', dpi=300, bbox_inches='tight')

print("\n✓ Distribution analysis created!")

# Calculate quartiles for each country
print("\nDISTRIBUTION STATISTICS:")
for country in covid_df.columns:
    data = covid_df[country]
    print(f"\n{country}:")
    print(f"  Median: {data.median():.0f}")
    print(f"  Q1 (25%): {data.quantile(0.25):.0f}")
    print(f"  Q3 (75%): {data.quantile(0.75):.0f}")
    print(f"  IQR: {data.quantile(0.75) - data.quantile(0.25):.0f}")

print("\n  - Saved as: covid_distribution_analysis.png")
plt.show()

# =============================================================================
# PART 6: MOVING AVERAGES
# =============================================================================

print("\n" + "=" * 70)
print("PART 6: 7-DAY MOVING AVERAGES")
print("=" * 70)

# Calculate 7-day moving average
covid_df_ma = covid_df.rolling(window=7).mean()

plt.figure(figsize=(14, 7))

for country in ['USA', 'India', 'Brazil']:
    # Original data (light)
    plt.plot(covid_df.index, covid_df[country],
             alpha=0.3, linewidth=1, color='gray')

    # Moving average (bold)
    plt.plot(covid_df_ma.index, covid_df_ma[country],
             label=f'{country} (7-day avg)', linewidth=3)

plt.title('COVID-19 Cases: 7-Day Moving Average',
          fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Cases', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig('covid_moving_averages.png', dpi=300, bbox_inches='tight')

print("\n✓ Moving average chart created!")
print("  - Smooths daily fluctuations")
print("  - Shows clearer trends")
print("  - Saved as: covid_moving_averages.png")
plt.show()

# =============================================================================
# PART 7: COMPLETE DASHBOARD
# =============================================================================

print("\n" + "=" * 70)
print("PART 7: COMPREHENSIVE DASHBOARD")
print("=" * 70)

# Create comprehensive dashboard
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Panel 1: Time Series (top, full width)
ax1 = fig.add_subplot(gs[0, :])
for country in covid_df.columns:
    ax1.plot(covid_df.index, covid_df[country], label=country, linewidth=2)
ax1.set_title('COVID-19 Timeline: Daily Cases', fontsize=16, fontweight='bold')
ax1.set_ylabel('Daily Cases', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, alpha=0.3)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# Panel 2: Total Cases Bar Chart
ax2 = fig.add_subplot(gs[1, 0])
total = covid_df.sum().sort_values(ascending=False)
colors_palette = sns.color_palette('viridis', len(total))
ax2.bar(range(len(total)), total.values, color=colors_palette)
ax2.set_xticks(range(len(total)))
ax2.set_xticklabels(total.index, rotation=45)
ax2.set_title('Total Cases by Country', fontsize=14, fontweight='bold')
ax2.set_ylabel('Total Cases', fontsize=11)

# Panel 3: Correlation Heatmap
ax3 = fig.add_subplot(gs[1, 1])
sns.heatmap(covid_df.corr(), annot=True, fmt='.2f',
            cmap='coolwarm', center=0, square=True,
            cbar_kws={'label': 'Correlation'}, ax=ax3)
ax3.set_title('Country Correlation', fontsize=14, fontweight='bold')

# Panel 4: Peak Cases Comparison
ax4 = fig.add_subplot(gs[2, 0])
peak_cases = covid_df.max().sort_values(ascending=True)
ax4.barh(range(len(peak_cases)), peak_cases.values, color='crimson')
ax4.set_yticks(range(len(peak_cases)))
ax4.set_yticklabels(peak_cases.index)
ax4.set_title('Peak Daily Cases', fontsize=14, fontweight='bold')
ax4.set_xlabel('Cases', fontsize=11)

# Panel 5: Average Cases with Error Bars
ax5 = fig.add_subplot(gs[2, 1])
means = covid_df.mean()
stds = covid_df.std()
ax5.bar(range(len(means)), means.values, yerr=stds.values,
        capsize=5, color='skyblue', edgecolor='navy', linewidth=2)
ax5.set_xticks(range(len(means)))
ax5.set_xticklabels(means.index, rotation=45)
ax5.set_title('Average Daily Cases (±1 SD)', fontsize=14, fontweight='bold')
ax5.set_ylabel('Cases', fontsize=11)

# Overall title
fig.suptitle('COVID-19 Global Impact Analysis Dashboard',
             fontsize=20, fontweight='bold', y=0.995)

plt.savefig('covid_complete_dashboard.png', dpi=300, bbox_inches='tight')

print("\n✓ Complete dashboard created!")
print("  - 5-panel comprehensive analysis")
print("  - Time series, comparisons, correlations")
print("  - Publication-ready quality")
print("  - Saved as: covid_complete_dashboard.png")
plt.show()

# =============================================================================
# PART 8: KEY INSIGHTS SUMMARY
# =============================================================================

print("\n" + "=" * 70)
print("KEY INSIGHTS & ANALYSIS SUMMARY")
print("=" * 70)

# 1. Peak analysis
print("\n1. PEAK ANALYSIS:")
for country in covid_df.columns:
    peak_value = covid_df[country].max()
    peak_date = covid_df[country].idxmax()
    print(f"   {country}: {peak_value:.0f} cases on {peak_date.date()}")

# 2. Total impact
print("\n2. TOTAL IMPACT (Cumulative Cases):")
for country, total in total_cases.items():
    percentage = (total / total_cases.sum()) * 100
    print(f"   {country}: {total:,.0f} ({percentage:.1f}% of total)")

# 3. Trend analysis
print("\n3. TREND ANALYSIS:")
for country in covid_df.columns:
    # Compare first month vs last month average
    first_month = covid_df[country].iloc[:30].mean()
    last_month = covid_df[country].iloc[-30:].mean()
    trend = "↑ Increasing" if last_month > first_month else "↓ Decreasing"
    change = ((last_month - first_month) / first_month) * 100
    print(f"   {country}: {trend} ({change:+.1f}%)")

# 4. Variability
print("\n4. VARIABILITY (Coefficient of Variation):")
for country in covid_df.columns:
    cv = (covid_df[country].std() / covid_df[country].mean()) * 100
    stability = "Stable" if cv < 50 else "Variable" if cv < 100 else "Highly Variable"
    print(f"   {country}: {cv:.1f}% - {stability}")

# =============================================================================
# SUMMARY
# =============================================================================

print("\n" + "=" * 70)
print("PROJECT COMPLETE! 🎉")
print("=" * 70)

print("\nVisualization files created:")
print("  1. covid_global_trends.png - Time series comparison")
print("  2. covid_country_comparison.png - Bar charts")
print("  3. covid_correlation_heatmap.png - Correlation matrix")
print("  4. covid_distribution_analysis.png - Box & violin plots")
print("  5. covid_moving_averages.png - Smoothed trends")
print("  6. covid_complete_dashboard.png - Comprehensive 5-panel dashboard")

print("\n" + "=" * 70)
print("SKILLS DEMONSTRATED")
print("=" * 70)
print("✓ Time series visualization")
print("✓ Multi-country comparative analysis")
print("✓ Statistical correlation analysis")
print("✓ Distribution analysis (box plots, violin plots)")
print("✓ Moving averages for trend smoothing")
print("✓ Professional multi-panel dashboards")
print("✓ Data-driven insights and storytelling")
print("✓ Publication-quality graphics")

print("\n" + "=" * 70)
print("NEXT STEPS")
print("=" * 70)
print("✓ Week 3 complete!")
print("→ Move to Week 4: Exploratory Data Analysis")
print("→ Apply these visualization skills to real datasets")
print("→ Build your own projects with your data")

print("\n" + "=" * 70)
print("CONGRATULATIONS! YOU'RE NOW A DATA VISUALIZATION PRO! 📊")
print("=" * 70)
