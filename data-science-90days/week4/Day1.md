# Week 4, Day 1: Introduction to Exploratory Data Analysis (EDA)

## 📚 What You'll Learn Today

- What is Exploratory Data Analysis and why it's crucial
- The EDA workflow and mindset
- Data profiling and understanding your dataset
- Finding patterns, anomalies, and insights
- Formulating hypotheses from data

---

## 🎯 The Story: The New Data Scientist's First Day

**You just started at a company as a data analyst.** Your boss hands you a spreadsheet with 10,000 rows of customer data and says: *"We need insights by Friday."*

You stare at the data. 50 columns. Numbers, dates, categories. Where do you even start?

**This is where EDA saves you.** It's your systematic approach to:
1. Understanding what you have
2. Finding what matters
3. Discovering the story hidden in the data

---

## 📖 What is EDA?

### Definition

**Exploratory Data Analysis (EDA)** is the process of:
- Examining data to understand its structure
- Identifying patterns and relationships
- Detecting anomalies and outliers
- Testing assumptions
- Generating hypotheses

### The EDA Mindset

Think of EDA like being a detective:

1. **🔍 Observe**: What does the data look like?
2. **❓ Question**: What patterns do I see?
3. **🧪 Investigate**: Why does this pattern exist?
4. **💡 Conclude**: What does this mean for the business?

**EDA is NOT about proving things** - it's about discovering things.

---

## 🎯 The 5-Step EDA Framework

### Step 1: Understand the Data

**Questions to ask:**
- What does each column represent?
- What's the data type (number, text, date)?
- How many rows/columns do I have?
- Where did this data come from?

```python
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('customer_data.csv')

# Basic info
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nFirst few rows:")
print(df.head())
```

---

### Step 2: Check Data Quality

**Questions to ask:**
- Are there missing values?
- Are there duplicates?
- Are there obvious errors?

```python
# Missing values
print("Missing values:")
print(df.isnull().sum())

# Duplicates
print(f"\nDuplicate rows: {df.duplicated().sum()}")

# Basic statistics
print("\nNumerical summary:")
print(df.describe())
```

**Real example:**

```python
import pandas as pd
import numpy as np

# Sample customer data
np.random.seed(42)
df = pd.DataFrame({
    'customer_id': range(1, 101),
    'age': np.random.randint(18, 70, 100),
    'purchase_amount': np.random.uniform(10, 500, 100),
    'days_since_purchase': np.random.randint(1, 365, 100),
    'email_domain': np.random.choice(['gmail.com', 'yahoo.com', 'outlook.com'], 100)
})

# Add some missing values
df.loc[5:10, 'age'] = np.nan
df.loc[15:18, 'purchase_amount'] = np.nan

print("MISSING VALUES ANALYSIS:")
print("=" * 40)
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Missing Count': missing,
    'Percentage': missing_pct
})
print(missing_df[missing_df['Missing Count'] > 0])
```

---

### Step 3: Analyze Distributions

**Questions to ask:**
- What's the typical value?
- How spread out is the data?
- Are there outliers?

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Distribution of purchase amounts
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df['purchase_amount'], bins=30, kde=True)
plt.title('Purchase Amount Distribution')
plt.xlabel('Amount ($)')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['purchase_amount'])
plt.title('Purchase Amount Box Plot')
plt.ylabel('Amount ($)')

plt.tight_layout()
plt.show()

# Statistical summary
print("Purchase Amount Statistics:")
print(f"Mean: ${df['purchase_amount'].mean():.2f}")
print(f"Median: ${df['purchase_amount'].median():.2f}")
print(f"Std Dev: ${df['purchase_amount'].std():.2f}")
print(f"Min: ${df['purchase_amount'].min():.2f}")
print(f"Max: ${df['purchase_amount'].max():.2f}")
```

---

### Step 4: Find Relationships

**Questions to ask:**
- Which variables are related?
- Are there interesting correlations?
- Can I group the data meaningfully?

```python
# Correlation analysis
numerical_cols = df.select_dtypes(include=[np.number]).columns
correlation = df[numerical_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Scatter plot for relationships
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='purchase_amount', alpha=0.6)
plt.title('Age vs Purchase Amount')
plt.xlabel('Customer Age')
plt.ylabel('Purchase Amount ($)')
plt.show()
```

---

### Step 5: Identify Anomalies

**Questions to ask:**
- What looks unusual?
- Are there data entry errors?
- Are there interesting outliers?

```python
# Find outliers using IQR method
def find_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = series[(series < lower_bound) | (series > upper_bound)]
    return outliers

# Find outliers in purchase amounts
outliers = find_outliers(df['purchase_amount'].dropna())
print(f"Found {len(outliers)} outliers in purchase amounts")
print(f"Outlier values: {outliers.values}")
```

---

## 💼 Real-World EDA Example: E-commerce Dataset

Let's do a complete EDA on an e-commerce dataset.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create realistic e-commerce data
np.random.seed(42)

n_customers = 500

df = pd.DataFrame({
    'customer_id': range(1, n_customers + 1),
    'age': np.random.randint(18, 75, n_customers),
    'income': np.random.normal(50000, 20000, n_customers),
    'purchase_amount': np.random.gamma(50, 3, n_customers),
    'num_purchases': np.random.poisson(5, n_customers),
    'days_since_signup': np.random.randint(1, 730, n_customers),
    'customer_type': np.random.choice(['New', 'Regular', 'VIP'], n_customers,
                                      p=[0.3, 0.5, 0.2])
})

# Make income positive
df['income'] = df['income'].abs()

print("=" * 60)
print("E-COMMERCE DATASET - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# STEP 1: Understand the data
print("\n1. DATASET OVERVIEW")
print("-" * 60)
print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\nColumns: {df.columns.tolist()}")
print(f"\nData types:\n{df.dtypes}")

# STEP 2: Check data quality
print("\n2. DATA QUALITY CHECK")
print("-" * 60)
print(f"Missing values:\n{df.isnull().sum()}")
print(f"\nDuplicates: {df.duplicated().sum()}")

# STEP 3: Statistical summary
print("\n3. STATISTICAL SUMMARY")
print("-" * 60)
print(df.describe().round(2))

# STEP 4: Distribution analysis by customer type
print("\n4. CUSTOMER TYPE ANALYSIS")
print("-" * 60)
customer_summary = df.groupby('customer_type').agg({
    'purchase_amount': ['mean', 'median', 'std'],
    'num_purchases': 'mean',
    'income': 'mean'
}).round(2)
print(customer_summary)

# Visualize
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Age distribution
sns.histplot(df['age'], bins=20, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Age Distribution')
axes[0, 0].set_xlabel('Age')

# Plot 2: Purchase amount by customer type
sns.boxplot(data=df, x='customer_type', y='purchase_amount', ax=axes[0, 1])
axes[0, 1].set_title('Purchase Amount by Customer Type')
axes[0, 1].set_ylabel('Purchase Amount ($)')

# Plot 3: Income vs Purchase correlation
sns.scatterplot(data=df, x='income', y='purchase_amount',
                hue='customer_type', alpha=0.6, ax=axes[1, 0])
axes[1, 0].set_title('Income vs Purchase Amount')
axes[1, 0].set_xlabel('Income ($)')
axes[1, 0].set_ylabel('Purchase Amount ($)')

# Plot 4: Number of purchases distribution
sns.countplot(data=df, x='num_purchases', ax=axes[1, 1])
axes[1, 1].set_title('Distribution of Purchase Frequency')
axes[1, 1].set_xlabel('Number of Purchases')
axes[1, 1].set_ylabel('Count')

plt.tight_layout()
plt.savefig('ecommerce_eda.png', dpi=300, bbox_inches='tight')
plt.show()

# STEP 5: Key insights
print("\n5. KEY INSIGHTS")
print("-" * 60)

# Correlation between income and purchases
corr = df['income'].corr(df['purchase_amount'])
print(f"✓ Income vs Purchase Amount correlation: {corr:.3f}")

# Customer type distribution
type_dist = df['customer_type'].value_counts()
print(f"\n✓ Customer distribution:")
for ctype, count in type_dist.items():
    pct = (count / len(df)) * 100
    print(f"  {ctype}: {count} ({pct:.1f}%)")

# High value customers
vip_avg = df[df['customer_type'] == 'VIP']['purchase_amount'].mean()
regular_avg = df[df['customer_type'] == 'Regular']['purchase_amount'].mean()
print(f"\n✓ VIP customers spend ${vip_avg:.2f} on average")
print(f"✓ Regular customers spend ${regular_avg:.2f} on average")
print(f"✓ VIP customers spend {(vip_avg/regular_avg - 1)*100:.1f}% more!")
```

---

## 💡 EDA Best Practices

### 1. Always Start with Questions

Don't just make random plots. Ask:
- What problem am I solving?
- What do I need to know?
- What would be useful to discover?

### 2. Follow a Checklist

```python
"""
EDA CHECKLIST:
□ Load and view data
□ Check shape and columns
□ Check data types
□ Check for missing values
□ Check for duplicates
□ Get statistical summary
□ Visualize distributions
□ Check correlations
□ Identify outliers
□ Group by categories
□ Document insights
"""
```

### 3. Document Your Findings

Keep notes as you explore:

```python
# INSIGHTS LOG
insights = []

insights.append("60% of customers are under 40 years old")
insights.append("VIP customers have 3x more purchases on average")
insights.append("Purchase amount weakly correlated with income (r=0.12)")
insights.append("Found 15 outlier purchases >$500 - investigate")

print("\nKEY FINDINGS:")
for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")
```

### 4. Use Visualization Wisely

Different questions need different plots:

| Question | Best Visualization |
|----------|-------------------|
| How is data distributed? | Histogram, Box plot |
| Is there a relationship? | Scatter plot |
| How do groups compare? | Box plot, Bar chart |
| How did it change over time? | Line plot |
| What's the correlation? | Heatmap |

---

## 🎯 Practice Exercises

### Exercise 1: Quick EDA (Warmup)

Load and explore this sales dataset:

```python
import pandas as pd
import numpy as np

np.random.seed(42)
sales = pd.DataFrame({
    'product': np.random.choice(['A', 'B', 'C', 'D'], 200),
    'quantity': np.random.randint(1, 20, 200),
    'price': np.random.uniform(10, 100, 200),
    'region': np.random.choice(['North', 'South', 'East', 'West'], 200)
})

# Your task:
# 1. Print basic info (shape, columns, dtypes)
# 2. Check for missing values
# 3. Get statistical summary
# 4. Find which product sells most
# 5. Calculate total revenue by region
```

---

### Exercise 2: Distribution Analysis (Application)

Analyze employee salaries:

```python
import pandas as pd
import numpy as np

np.random.seed(123)
employees = pd.DataFrame({
    'salary': np.random.normal(60000, 20000, 300),
    'years_experience': np.random.randint(0, 30, 300),
    'department': np.random.choice(['Sales', 'Engineering', 'HR'], 300)
})

# Your task:
# 1. Create histogram of salaries
# 2. Create box plot by department
# 3. Find correlation between experience and salary
# 4. Identify salary outliers
# 5. Calculate average salary by department
```

---

### Exercise 3: Complete EDA (Real-World)

Perform full EDA on customer churn data:

```python
import pandas as pd
import numpy as np

np.random.seed(42)
customers = pd.DataFrame({
    'tenure_months': np.random.randint(1, 60, 400),
    'monthly_charges': np.random.uniform(20, 100, 400),
    'total_charges': np.random.uniform(100, 5000, 400),
    'contract_type': np.random.choice(['Month-to-month', 'One year', 'Two year'], 400),
    'churned': np.random.choice([0, 1], 400, p=[0.7, 0.3])
})

# Your task:
# 1. Complete data overview
# 2. Check data quality
# 3. Analyze distributions
# 4. Compare churned vs not-churned customers
# 5. Create 2x2 visualization dashboard
# 6. Write 5 key insights
```

---

## 🎓 What You Learned Today

✅ The purpose and importance of EDA
✅ The 5-step EDA framework
✅ Data quality checks
✅ Distribution analysis techniques
✅ Finding relationships and correlations
✅ Identifying outliers and anomalies
✅ Best practices for systematic exploration

---

## 📚 Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [EDA in Python Guide](https://realpython.com/pandas-python-explore-dataset/)
- [Kaggle EDA Notebooks](https://www.kaggle.com/code?searchQuery=exploratory+data+analysis)

---

## 🚀 Tomorrow's Preview

**Day 2: Advanced EDA Techniques**

We'll learn:
- Feature engineering and transformation
- Handling categorical variables
- Time series analysis in EDA
- Multivariate analysis
- Automated EDA tools

**Get ready to level up your EDA skills!** 📊

---

## ✅ Check Your Understanding

Before moving on, make sure you can:
- [ ] Load data and get basic information
- [ ] Check for missing values and duplicates
- [ ] Generate statistical summaries
- [ ] Create distribution visualizations
- [ ] Find correlations between variables
- [ ] Identify and handle outliers
- [ ] Document insights from data

**Practice file**: See `assets/projects/week4/day10-practice.py` for complete solutions!

---

**Next**: [Day 2 - Advanced EDA Techniques](Day2.md)
