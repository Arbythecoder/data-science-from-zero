# DAY 5: PANDAS DATA ANALYSIS

**Goal**: Master Pandas to analyze and clean data

---

## ✅ CHECKLIST

### Morning Session (3 hours)
- [ ] **Read** [week2/Day1.md](data-science-90days/week2/Day1.md) (30 min)
- [ ] **Run** [day1-practice.py](data-science-90days/assets/projects/week2/day1-practice.py) (60 min)
- [ ] **Read** [week2/Day2.md](data-science-90days/week2/Day2.md) (30 min)
- [ ] **Run** [day2-practice.py](data-science-90days/assets/projects/week2/day2-practice.py) (60 min)

### Afternoon Session (2 hours)
- [ ] **Read** [week2/Day3.md](data-science-90days/week2/Day3.md) (30 min)
- [ ] **Run** [day3-practice.py](data-science-90days/assets/projects/week2/day3-practice.py) (90 min)

### Evening Application (1 hour)
- [ ] **Build** analysis script for YOUR data
- [ ] **Test** it with different datasets

---

## 📝 ESSENTIAL PANDAS CODE

### Load and Explore:
```python
import pandas as pd

# Load data
df = pd.read_csv('your_data.csv')

# Quick look
print(df.head())          # First 5 rows
print(df.info())          # Data types, nulls
print(df.describe())      # Statistics
print(df.shape)           # (rows, columns)
```

### Filter and Select:
```python
# Select columns
sales = df['Sales']
subset = df[['Product', 'Revenue']]

# Filter rows
high_value = df[df['Revenue'] > 1000]
recent = df[df['Date'] > '2024-01-01']

# Multiple conditions
premium = df[(df['Revenue'] > 1000) & (df['Category'] == 'Electronics')]
```

### Clean Data:
```python
# Handle missing data
df_clean = df.dropna()                    # Remove nulls
df['Price'] = df['Price'].fillna(0)       # Fill with 0

# Remove duplicates
df_clean = df.drop_duplicates()

# Clean text
df['Name'] = df['Name'].str.strip()       # Remove spaces
df['Name'] = df['Name'].str.title()       # Capitalize

# Fix data types
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'])
```

### Analyze:
```python
# Group and aggregate
by_product = df.groupby('Product')['Revenue'].sum()
by_month = df.groupby('Month')['Sales'].mean()

# Sort
top_products = df.sort_values('Revenue', ascending=False)

# Calculate new columns
df['Profit'] = df['Revenue'] - df['Cost']
df['Margin'] = (df['Profit'] / df['Revenue']) * 100
```

---

## 🎯 BUILD THIS

**Complete Analysis Script**:
```python
import pandas as pd

def analyze_business_data(file_path):
    """Load, clean, and analyze business data."""

    # 1. Load data
    df = pd.read_csv(file_path)
    print(f"Loaded {len(df)} rows")

    # 2. Clean data
    df = df.drop_duplicates()
    df = df.dropna()
    print(f"After cleaning: {len(df)} rows")

    # 3. Calculate metrics
    total_revenue = df['Revenue'].sum()
    avg_revenue = df['Revenue'].mean()
    top_product = df.groupby('Product')['Revenue'].sum().idxmax()

    # 4. Print results
    print(f"\n=== BUSINESS INSIGHTS ===")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Average Sale: ${avg_revenue:,.2f}")
    print(f"Top Product: {top_product}")

    # 5. Save clean data
    df.to_csv('clean_data.csv', index=False)
    print("\nClean data saved to clean_data.csv")

    return df

# Use it!
df = analyze_business_data('your_data.csv')
```

---

## ✅ DAY 5 COMPLETE WHEN:

You can:
- [ ] Load any CSV into Pandas
- [ ] Explore data (head, info, describe)
- [ ] Filter rows and select columns
- [ ] Clean messy data (nulls, duplicates, text)
- [ ] Group and aggregate data
- [ ] Calculate new columns
- [ ] Save results back to CSV

**Bonus**: You have a reusable script for YOUR business data!

---

**Time**: 6 hours | **Difficulty**: Hard | **Day**: 5/6

**Tomorrow**: Build your final project!
