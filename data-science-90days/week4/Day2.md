# Week 4, Day 2: Advanced EDA Techniques

## 📚 What You'll Learn Today

- Feature engineering during EDA
- Handling categorical variables effectively
- Time series data exploration
- Multivariate analysis techniques
- Automated EDA tools (pandas-profiling, sweetviz)

---

## 🎯 The Story: The Hidden Patterns

**A marketing analyst is stuck.** They have customer data but can't figure out why some campaigns succeed and others fail. The raw data shows nothing obvious.

Then they discover: *"What if I combine features? What if I look at customer behavior over time instead of snapshots?"*

**Suddenly, patterns emerge.** Advanced EDA reveals:
- Weekend customers behave differently than weekday customers
- Customers who buy Product A within 7 days are 3x more likely to buy Product B
- Seasonal trends were hidden in daily noise

**Today you'll learn to find these hidden insights.**

---

## 📖 Core Concepts

### 1. Feature Engineering in EDA

**Feature engineering** = Creating new variables from existing ones to reveal patterns.

#### Example: From Date to Insights

```python
import pandas as pd
import numpy as np

# Sample transaction data
np.random.seed(42)
dates = pd.date_range('2023-01-01', periods=500, freq='D')
df = pd.DataFrame({
    'date': np.random.choice(dates, 1000),
    'amount': np.random.gamma(50, 2, 1000),
    'customer_id': np.random.randint(1, 100, 1000)
})

# Engineer time-based features
df['day_of_week'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.month_name()
df['is_weekend'] = df['date'].dt.dayofweek >= 5
df['quarter'] = df['date'].dt.quarter

print("Original data:")
print(df.head())

# Analyze by new features
print("\nAverage purchase by day of week:")
print(df.groupby('day_of_week')['amount'].mean().sort_values(ascending=False))

print("\nWeekend vs Weekday:")
print(df.groupby('is_weekend')['amount'].agg(['mean', 'count']))
```

**Common Feature Engineering Patterns:**

```python
# 1. From continuous to categorical (binning)
df['age_group'] = pd.cut(df['age'],
                          bins=[0, 18, 30, 50, 100],
                          labels=['Teen', 'Young Adult', 'Adult', 'Senior'])

# 2. Combining features
df['total_value'] = df['quantity'] * df['price']

# 3. Ratios and percentages
df['discount_pct'] = (df['original_price'] - df['sale_price']) / df['original_price'] * 100

# 4. Aggregations
# Customer's total spending
df['customer_total'] = df.groupby('customer_id')['amount'].transform('sum')

# Customer's purchase count
df['customer_purchase_count'] = df.groupby('customer_id')['customer_id'].transform('count')

# 5. Time-based features
df['days_since_first_purchase'] = (df['date'] - df.groupby('customer_id')['date'].transform('min')).dt.days
```

---

### 2. Handling Categorical Variables

#### Understanding Categories

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
df = pd.DataFrame({
    'product_category': ['Electronics', 'Clothing', 'Electronics', 'Food',
                         'Clothing', 'Electronics', 'Food'] * 50,
    'region': ['North', 'South', 'East', 'West'] * 87 + ['North', 'South', 'East'],
    'sales': np.random.uniform(100, 1000, 350)
})

# Frequency analysis
print("Category frequencies:")
print(df['product_category'].value_counts())

# Visual analysis
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Count plot
sns.countplot(data=df, x='product_category', ax=axes[0])
axes[0].set_title('Product Category Distribution')
axes[0].tick_params(axis='x', rotation=45)

# Box plot: Sales by category
sns.boxplot(data=df, x='product_category', y='sales', ax=axes[1])
axes[1].set_title('Sales by Category')
axes[1].tick_params(axis='x', rotation=45)

# Bar plot: Average sales by category
avg_sales = df.groupby('product_category')['sales'].mean().sort_values(ascending=False)
axes[2].bar(avg_sales.index, avg_sales.values)
axes[2].set_title('Average Sales by Category')
axes[2].tick_params(axis='x', rotation=45)
axes[2].set_ylabel('Average Sales ($)')

plt.tight_layout()
plt.show()
```

#### Cross-Tabulation Analysis

```python
# Create cross-tab: Category vs Region
crosstab = pd.crosstab(df['product_category'], df['region'], margins=True)
print("\nCross-tabulation:")
print(crosstab)

# Percentage breakdown
crosstab_pct = pd.crosstab(df['product_category'], df['region'], normalize='index') * 100
print("\nPercentage breakdown:")
print(crosstab_pct.round(2))

# Heatmap visualization
plt.figure(figsize=(10, 6))
sns.heatmap(crosstab.iloc[:-1, :-1], annot=True, fmt='d', cmap='YlOrRd')
plt.title('Product Category by Region Distribution')
plt.tight_layout()
plt.show()
```

---

### 3. Time Series EDA

#### Analyzing Trends Over Time

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate time series data
np.random.seed(42)
dates = pd.date_range('2022-01-01', '2023-12-31', freq='D')
# Add trend + seasonality + noise
trend = np.linspace(100, 200, len(dates))
seasonality = 20 * np.sin(np.arange(len(dates)) * 2 * np.pi / 365)
noise = np.random.normal(0, 10, len(dates))
values = trend + seasonality + noise

ts_df = pd.DataFrame({
    'date': dates,
    'value': values
})

# Set date as index
ts_df.set_index('date', inplace=True)

# Time series analysis
print("Time Series Summary:")
print(ts_df.describe())

# Visualize
fig, axes = plt.subplots(3, 1, figsize=(14, 10))

# Plot 1: Raw time series
axes[0].plot(ts_df.index, ts_df['value'], alpha=0.5, label='Daily')
axes[0].plot(ts_df.index, ts_df['value'].rolling(30).mean(),
             color='red', linewidth=2, label='30-day MA')
axes[0].set_title('Time Series with 30-Day Moving Average')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Plot 2: Monthly aggregation
monthly = ts_df.resample('M').mean()
axes[1].plot(monthly.index, monthly['value'], marker='o')
axes[1].set_title('Monthly Average')
axes[1].grid(True, alpha=0.3)

# Plot 3: Year-over-year comparison
ts_df['month'] = ts_df.index.month
ts_df['year'] = ts_df.index.year
pivot = ts_df.pivot_table(values='value', index='month', columns='year')
pivot.plot(ax=axes[2], marker='o')
axes[2].set_title('Year-over-Year Comparison')
axes[2].set_xlabel('Month')
axes[2].set_ylabel('Value')
axes[2].legend(title='Year')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Seasonal decomposition
print("\nMonthly statistics:")
print(ts_df.groupby('month')['value'].agg(['mean', 'std', 'min', 'max']).round(2))
```

---

### 4. Multivariate Analysis

#### Analyzing Multiple Variables Together

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create multivariate dataset
np.random.seed(42)
n = 300

df_multi = pd.DataFrame({
    'age': np.random.randint(18, 70, n),
    'income': np.random.normal(50000, 20000, n),
    'credit_score': np.random.randint(300, 850, n),
    'num_purchases': np.random.poisson(10, n),
    'customer_lifetime_value': np.random.gamma(100, 50, n)
})

# Make income positive
df_multi['income'] = df_multi['income'].abs()

print("Multivariate Analysis")
print("=" * 60)

# Correlation matrix
print("\nCorrelation Matrix:")
corr_matrix = df_multi.corr()
print(corr_matrix.round(3))

# Visualization: Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            fmt='.2f', square=True, linewidths=2)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# Pair plot (scatter matrix)
sns.pairplot(df_multi, diag_kind='kde', plot_kws={'alpha': 0.6})
plt.suptitle('Pairwise Relationships', y=1.01)
plt.tight_layout()
plt.show()

# Conditional analysis
# High income vs low income customers
high_income = df_multi[df_multi['income'] > df_multi['income'].median()]
low_income = df_multi[df_multi['income'] <= df_multi['income'].median()]

print("\nHigh Income Customers:")
print(high_income[['num_purchases', 'customer_lifetime_value']].describe())

print("\nLow Income Customers:")
print(low_income[['num_purchases', 'customer_lifetime_value']].describe())
```

---

### 5. Automated EDA Tools

#### Using pandas-profiling

```python
# Install: pip install pandas-profiling

import pandas as pd
import numpy as np
# from pandas_profiling import ProfileReport  # Uncomment to use

# Create sample data
np.random.seed(42)
df_auto = pd.DataFrame({
    'age': np.random.randint(18, 80, 500),
    'income': np.random.normal(60000, 25000, 500),
    'purchases': np.random.poisson(5, 500),
    'category': np.random.choice(['A', 'B', 'C'], 500)
})

# Generate profile report
# profile = ProfileReport(df_auto, title="Automated EDA Report")
# profile.to_file("eda_report.html")

print("✓ Automated EDA report generated!")
print("  - Opens comprehensive HTML report")
print("  - Includes distributions, correlations, missing values")
print("  - Identifies potential issues automatically")
```

#### Using Sweetviz

```python
# Install: pip install sweetviz

# import sweetviz as sv  # Uncomment to use

# Create comparison report
# report = sv.analyze(df_auto)
# report.show_html("sweetviz_report.html")

print("✓ Sweetviz report generated!")
print("  - Interactive HTML dashboard")
print("  - Beautiful visualizations")
print("  - Target analysis support")
```

---

## 💼 Real-World Example: Customer Churn Analysis

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create realistic customer churn dataset
np.random.seed(42)
n_customers = 1000

df_churn = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),
    'tenure_months': np.random.randint(1, 72, n_customers),
    'monthly_charges': np.random.uniform(20, 120, n_customers),
    'contract_type': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_customers),
    'payment_method': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n_customers),
    'has_tech_support': np.random.choice([0, 1], n_customers),
    'num_support_tickets': np.random.poisson(2, n_customers)
})

# Create target variable (churned) with logical relationships
churn_prob = 0.3 - (df_churn['tenure_months'] / 200) + \
             (df_churn['monthly_charges'] / 500) + \
             (df_churn['num_support_tickets'] / 20)
churn_prob = np.clip(churn_prob, 0, 1)
df_churn['churned'] = (np.random.random(n_customers) < churn_prob).astype(int)

# Feature engineering
df_churn['total_charges'] = df_churn['tenure_months'] * df_churn['monthly_charges']
df_churn['tenure_group'] = pd.cut(df_churn['tenure_months'],
                                   bins=[0, 12, 36, 72],
                                   labels=['New', 'Medium', 'Long-term'])

print("=" * 70)
print("CUSTOMER CHURN - ADVANCED EDA")
print("=" * 70)

# Churn rate
churn_rate = df_churn['churned'].mean() * 100
print(f"\nOverall churn rate: {churn_rate:.2f}%")

# Churn by tenure group
print("\nChurn rate by tenure group:")
churn_by_tenure = df_churn.groupby('tenure_group')['churned'].agg(['mean', 'count'])
churn_by_tenure['mean'] = churn_by_tenure['mean'] * 100
print(churn_by_tenure.round(2))

# Churn by contract type
print("\nChurn rate by contract type:")
churn_by_contract = df_churn.groupby('contract_type')['churned'].mean() * 100
print(churn_by_contract.sort_values(ascending=False).round(2))

# Create comprehensive dashboard
fig = plt.figure(figsize=(16, 12))
gs = fig.add_gridspec(3, 2, hspace=0.3, wspace=0.3)

# Plot 1: Churn rate by tenure group
ax1 = fig.add_subplot(gs[0, 0])
churn_by_tenure['mean'].plot(kind='bar', ax=ax1, color='coral')
ax1.set_title('Churn Rate by Tenure Group', fontweight='bold')
ax1.set_ylabel('Churn Rate (%)')
ax1.set_xlabel('Tenure Group')
ax1.tick_params(axis='x', rotation=0)

# Plot 2: Tenure distribution for churned vs not churned
ax2 = fig.add_subplot(gs[0, 1])
df_churn[df_churn['churned']==1]['tenure_months'].hist(bins=20, alpha=0.5, label='Churned', ax=ax2)
df_churn[df_churn['churned']==0]['tenure_months'].hist(bins=20, alpha=0.5, label='Not Churned', ax=ax2)
ax2.set_title('Tenure Distribution by Churn Status', fontweight='bold')
ax2.set_xlabel('Tenure (months)')
ax2.set_ylabel('Frequency')
ax2.legend()

# Plot 3: Monthly charges comparison
ax3 = fig.add_subplot(gs[1, 0])
sns.boxplot(data=df_churn, x='churned', y='monthly_charges', ax=ax3)
ax3.set_title('Monthly Charges: Churned vs Not Churned', fontweight='bold')
ax3.set_xticklabels(['Not Churned', 'Churned'])
ax3.set_ylabel('Monthly Charges ($)')

# Plot 4: Churn by contract type
ax4 = fig.add_subplot(gs[1, 1])
churn_contract_df = df_churn.groupby(['contract_type', 'churned']).size().unstack()
churn_contract_df.plot(kind='bar', stacked=True, ax=ax4, color=['lightgreen', 'lightcoral'])
ax4.set_title('Contract Type Distribution by Churn', fontweight='bold')
ax4.set_ylabel('Number of Customers')
ax4.set_xlabel('Contract Type')
ax4.legend(['Not Churned', 'Churned'])
ax4.tick_params(axis='x', rotation=45)

# Plot 5: Support tickets analysis
ax5 = fig.add_subplot(gs[2, 0])
sns.violinplot(data=df_churn, x='churned', y='num_support_tickets', ax=ax5)
ax5.set_title('Support Tickets: Churned vs Not Churned', fontweight='bold')
ax5.set_xticklabels(['Not Churned', 'Churned'])
ax5.set_ylabel('Number of Support Tickets')

# Plot 6: Correlation heatmap for numerical features
ax6 = fig.add_subplot(gs[2, 1])
numerical_features = ['tenure_months', 'monthly_charges', 'total_charges',
                      'has_tech_support', 'num_support_tickets', 'churned']
corr = df_churn[numerical_features].corr()
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax6)
ax6.set_title('Feature Correlations', fontweight='bold')

fig.suptitle('Customer Churn Analysis Dashboard', fontsize=18, fontweight='bold', y=0.995)
plt.savefig('churn_advanced_eda.png', dpi=300, bbox_inches='tight')
plt.show()

# Key insights
print("\n" + "=" * 70)
print("KEY INSIGHTS")
print("=" * 70)

avg_charges_churned = df_churn[df_churn['churned']==1]['monthly_charges'].mean()
avg_charges_not_churned = df_churn[df_churn['churned']==0]['monthly_charges'].mean()

print(f"1. Churned customers pay ${avg_charges_churned:.2f}/month on average")
print(f"   vs ${avg_charges_not_churned:.2f} for retained customers")

avg_tenure_churned = df_churn[df_churn['churned']==1]['tenure_months'].mean()
avg_tenure_not_churned = df_churn[df_churn['churned']==0]['tenure_months'].mean()

print(f"\n2. Churned customers have {avg_tenure_churned:.1f} months average tenure")
print(f"   vs {avg_tenure_not_churned:.1f} months for retained customers")

print(f"\n3. Month-to-month contracts have {churn_by_contract['Month-to-month']:.1f}% churn rate")
print(f"   vs {churn_by_contract['Two year']:.1f}% for two-year contracts")

print("\n4. RECOMMENDATIONS:")
print("   → Focus retention efforts on new customers (< 12 months)")
print("   → Incentivize long-term contracts")
print("   → Monitor high monthly charge customers closely")
print("   → Improve tech support to reduce tickets")
```

---

## 💡 Pro Tips

### 1. Feature Engineering Workflow

```python
"""
1. Domain knowledge → What features would be meaningful?
2. Create features → Build new variables
3. Visualize → Do they show patterns?
4. Validate → Are they useful for predictions?
5. Iterate → Refine based on findings
"""
```

### 2. Handling Time Series

- Always set datetime as index
- Use resample() for aggregation
- Calculate rolling statistics
- Check for seasonality and trends

### 3. Categorical Variables

- Use value_counts() for frequency
- Create cross-tabulations for relationships
- Visualize with count plots and bar charts
- Consider one-hot encoding for modeling

---

## 🎯 Practice Exercises

### Exercise 1: Feature Engineering (Warmup)

```python
import pandas as pd
import numpy as np

# Transaction data
np.random.seed(42)
transactions = pd.DataFrame({
    'date': pd.date_range('2023-01-01', periods=200, freq='D'),
    'amount': np.random.gamma(50, 2, 200),
    'customer_id': np.random.randint(1, 50, 200)
})

# Tasks:
# 1. Extract day_of_week, month, is_weekend
# 2. Calculate customer's total spending
# 3. Calculate customer's average transaction
# 4. Find customers with >5 transactions
# 5. Visualize spending by day of week
```

### Exercise 2: Categorical Analysis (Application)

```python
# Your code here to analyze product categories across regions
# and find which combinations perform best
```

### Exercise 3: Complete Advanced EDA (Real-World)

Perform advanced EDA on employee attrition data including feature engineering, multivariate analysis, and insights.

---

## 🎓 What You Learned Today

✅ Feature engineering techniques
✅ Handling and analyzing categorical variables
✅ Time series exploration methods
✅ Multivariate analysis approaches
✅ Automated EDA tools

---

**Practice file**: See `assets/projects/week4/day11-practice.py` for complete solutions!

**Next**: [Day 3 - Complete EDA Project](Day3.md)
