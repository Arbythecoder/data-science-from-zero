# Week 3, Day 3: Real-World Visualization Project

## 📚 What You'll Build Today

- Complete COVID-19 data analysis dashboard
- Multi-panel professional visualizations
- Time series analysis with trends
- Comparative analysis across countries
- Export-ready publication graphics

---

## 🎯 The Project: COVID-19 Global Impact Analysis

**Your Mission**: Create a comprehensive visual analysis of COVID-19 data to understand:
1. How cases evolved over time globally
2. Which countries were most affected
3. Vaccination progress across regions
4. Trends and patterns in the pandemic

**Skills you'll use**:
- Everything from Day 1 (Matplotlib)
- Everything from Day 2 (Seaborn)
- Real-world messy data
- Professional data storytelling

---

## 📊 Project Structure

We'll build **4 main visualizations**:

1. **Global Trend Line Chart** - Cases over time
2. **Country Comparison Bar Chart** - Total cases by country
3. **Correlation Heatmap** - Relationships between variables
4. **Distribution Analysis** - Case distribution patterns

---

## 💻 Part 1: Setup and Data Loading

### Step 1: Import Libraries

```python
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
```

### Step 2: Create Sample COVID-19 Data

```python
# For this project, we'll create realistic sample data
# In real projects, you'd load from CSV or API

np.random.seed(42)

# Create date range
dates = pd.date_range(start='2020-03-01', end='2021-03-01', freq='D')

# Simulate COVID cases for different countries
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

print("Data shape:", covid_df.shape)
print("\nFirst few rows:")
print(covid_df.head())
print("\nData summary:")
print(covid_df.describe())
```

---

## 📈 Part 2: Visualization 1 - Global Trend Analysis

### Multi-Country Time Series

```python
# Create figure
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
plt.gcf().autofmt_xdate()  # Rotate date labels

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
plt.show()
```

**What this shows**:
- Different countries had peaks at different times
- India had the highest daily cases
- Multiple waves visible in some countries

---

## 📊 Part 3: Visualization 2 - Total Impact Comparison

### Bar Chart with Statistical Context

```python
# Calculate total cases for each country
total_cases = covid_df.sum().sort_values(ascending=False)

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
avg_cases = covid_df.mean().sort_values(ascending=False)
axes[1].barh(avg_cases.index, avg_cases.values, color='coral')
axes[1].set_title('Average Daily Cases',
                  fontsize=16, fontweight='bold')
axes[1].set_xlabel('Average Daily Cases', fontsize=12)

# Add value labels
for i, (country, value) in enumerate(avg_cases.items()):
    axes[1].text(value, i, f'{value:.0f}',
                va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('covid_country_comparison.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## 🔥 Part 4: Visualization 3 - Correlation Heatmap

### Understanding Variable Relationships

```python
# Calculate correlation between countries
correlation = covid_df.corr()

# Create heatmap
plt.figure(figsize=(10, 8))

sns.heatmap(correlation,
            annot=True,          # Show numbers
            fmt='.2f',           # 2 decimal places
            cmap='coolwarm',     # Color scheme
            center=0,            # Center colormap at 0
            square=True,         # Square cells
            linewidths=2,        # White lines between cells
            cbar_kws={'label': 'Correlation Coefficient'})

plt.title('COVID-19 Case Correlation Between Countries',
          fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('covid_correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()
```

**Insights**:
- Positive correlation = countries had similar timing
- Negative correlation = opposite patterns
- Helps understand if pandemic waves were global or regional

---

## 📉 Part 5: Visualization 4 - Distribution Analysis

### Box Plot & Violin Plot Comparison

```python
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
plt.show()
```

**What you learn**:
- Median daily cases (line in box)
- Variability (box height)
- Outliers (dots)
- Distribution shape (violin width)

---

## 🎨 Part 6: The Complete Dashboard

### Professional Multi-Panel Report

```python
# Create comprehensive dashboard
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Panel 1: Time Series (top, full width)
ax1 = fig.add_subplot(gs[0, :])
for country in covid_df.columns:
    ax1.plot(covid_df.index, covid_df[country], label=country, linewidth=2)
ax1.set_title('COVID-19 Timeline: Daily Cases', fontsize=16, fontweight='bold')
ax1.set_ylabel('Daily Cases', fontsize=12)
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

# Panel 2: Total Cases Bar Chart
ax2 = fig.add_subplot(gs[1, 0])
total = covid_df.sum().sort_values(ascending=False)
colors = sns.color_palette('viridis', len(total))
ax2.bar(range(len(total)), total.values, color=colors)
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
plt.show()
```

---

## 💡 Advanced Techniques

### 1. Adding Moving Averages (Smoothing Trends)

```python
plt.figure(figsize=(14, 7))

# 7-day moving average
covid_df_ma = covid_df.rolling(window=7).mean()

for country in ['USA', 'India', 'Brazil']:
    # Original data (light)
    plt.plot(covid_df.index, covid_df[country],
             alpha=0.3, linewidth=1)

    # Moving average (bold)
    plt.plot(covid_df_ma.index, covid_df_ma[country],
             label=f'{country} (7-day avg)', linewidth=3)

plt.title('COVID-19 Cases: 7-Day Moving Average',
          fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Cases', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()
```

**Why moving averages?**
- Smooths out daily fluctuations
- Shows clearer trends
- Reduces noise from reporting irregularities

---

### 2. Highlighting Specific Periods

```python
plt.figure(figsize=(14, 7))

plt.plot(covid_df.index, covid_df['USA'], linewidth=2, label='USA')

# Highlight peak period
peak_start = pd.Timestamp('2020-06-15')
peak_end = pd.Timestamp('2020-08-15')
plt.axvspan(peak_start, peak_end, alpha=0.3, color='red',
            label='Peak Period')

# Add horizontal line at average
avg = covid_df['USA'].mean()
plt.axhline(avg, color='green', linestyle='--', linewidth=2,
            label=f'Average: {avg:.0f}')

plt.title('USA COVID-19 Cases with Highlighted Peak Period',
          fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Cases', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.show()
```

---

## 🎯 Your Turn: Final Project

### Build Your Own Analysis Dashboard

Choose ONE of these datasets to visualize:

#### Option 1: Sales Data Dashboard
Analyze monthly sales across regions and products.

#### Option 2: Website Analytics Dashboard
Visualize page views, bounce rate, and conversions over time.

#### Option 3: Stock Market Dashboard
Compare multiple stocks with technical indicators.

#### Option 4: Weather Data Dashboard
Analyze temperature, rainfall, and seasonal patterns.

### Requirements:

Your dashboard must include:
1. **Time series plot** - Show trends over time
2. **Comparison chart** - Bar or box plot comparing categories
3. **Correlation heatmap** - Show relationships
4. **Distribution plot** - Histogram or violin plot

**Deliverables**:
- Python script with complete code
- 4 individual visualization PNG files
- 1 comprehensive dashboard PNG
- Brief written insights (3-5 bullet points)

---

## 🎓 What You Accomplished Today

✅ Built a complete data visualization project from scratch
✅ Created professional multi-panel dashboards
✅ Analyzed real-world time series data
✅ Used advanced techniques (moving averages, annotations, highlights)
✅ Exported publication-quality graphics
✅ Developed data storytelling skills

---

## 💡 Pro Tips for Real Projects

### 1. Data Preparation
- Clean data before visualizing
- Handle missing values
- Check for outliers
- Ensure proper data types

### 2. Visual Design
- Consistent color schemes
- Clear, informative titles
- Labeled axes with units
- Legends for multi-line plots
- Appropriate figure sizes

### 3. Storytelling
- Start with a question
- Guide the viewer's eye
- Highlight key insights
- Use annotations strategically
- End with actionable conclusions

### 4. Technical Excellence
- High DPI for print (300)
- Proper file formats (PNG for web, PDF for print)
- Reproducible code
- Comment your code
- Version control

---

## 🚀 What's Next?

**Week 4: Exploratory Data Analysis (EDA)**

You'll learn:
- Statistical summaries and descriptive analysis
- Finding patterns and anomalies
- Feature engineering
- Hypothesis testing
- Complete EDA workflows

**You now have the visualization skills to explore ANY dataset!** 📊

---

## ✅ Week 3 Checklist

Make sure you can:
- [ ] Create line plots for time series
- [ ] Build scatter plots for relationships
- [ ] Design bar charts for comparisons
- [ ] Generate histograms and box plots
- [ ] Create correlation heatmaps
- [ ] Build multi-panel dashboards
- [ ] Customize plots professionally
- [ ] Export high-quality graphics
- [ ] Tell stories with data

**Practice file**: See `assets/projects/week3/day9-practice.py` for the complete COVID dashboard code!

---

## 📚 Additional Project Ideas

1. **Climate Change Visualization** - Temperature trends over decades
2. **Sports Analytics Dashboard** - Player performance comparisons
3. **Social Media Metrics** - Engagement analysis over time
4. **Financial Portfolio Tracker** - Investment performance visualization
5. **Health Data Analysis** - Heart rate, steps, sleep patterns

**Pick one and build it this week to solidify your skills!**

---

**Congratulations on completing Week 3!** 🎉

You can now create professional data visualizations that communicate insights effectively. This skill is crucial for every data science project!

**Next**: [Week 4, Day 1 - Introduction to Exploratory Data Analysis](../week4/Day1.md)
