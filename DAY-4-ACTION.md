# DAY 4: PYTHON BASICS

**Goal**: Get Python running and analyze data with code

---

## ✅ CHECKLIST

### Morning Setup (2 hours)
- [ ] **Install** Python OR setup Google Colab (30 min)
- [ ] **Read** [week1/Day1.md](data-science-90days/week1/Day1.md) (30 min)
- [ ] **Run** [day1-practice.py](data-science-90days/assets/projects/week1/day1-practice.py) (60 min)

### Afternoon Learning (2 hours)
- [ ] **Read** [week1/Day2.md](data-science-90days/week1/Day2.md) (30 min)
- [ ] **Run** [day2-practice.py](data-science-90days/assets/projects/week1/day2-practice.py) (30 min)
- [ ] **Build** simple Python script (60 min)

### Evening Application (1 hour)
- [ ] **Load** your business data (CSV)
- [ ] **Calculate** basic stats with Python

---

## 🎯 SETUP OPTIONS

### Option 1: Google Colab (EASIEST)
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Sign in with Google
3. New Notebook
4. Start coding!

### Option 2: Local Python
1. Download Python from python.org
2. Install Jupyter: `pip install jupyter`
3. Run: `jupyter notebook`
4. Create new notebook

**Recommendation**: Use Google Colab if new to Python!

---

## 📝 WHAT TO CODE TODAY

### Basic Python:
```python
# Variables
sales = 5000
costs = 3000
profit = sales - costs
print(f"Profit: ${profit}")

# Lists
products = ["Laptop", "Mouse", "Keyboard"]
prices = [999, 25, 75]

# Loop
for i in range(len(products)):
    print(f"{products[i]}: ${prices[i]}")

# Function
def calculate_revenue(quantity, price):
    return quantity * price

revenue = calculate_revenue(10, 50)
print(f"Revenue: ${revenue}")
```

### Load Your CSV:
```python
import pandas as pd

# Load your data
df = pd.read_csv('your_data.csv')

# Quick stats
total = df['Revenue'].sum()
average = df['Revenue'].mean()
count = len(df)

print(f"Total Revenue: ${total:,.2f}")
print(f"Average Sale: ${average:,.2f}")
print(f"Number of Sales: {count}")
```

---

## 🎯 WHAT TO BUILD

**Simple Business Calculator**:
```python
# Your business metrics
def business_stats(sales_list):
    total = sum(sales_list)
    average = total / len(sales_list)
    maximum = max(sales_list)
    minimum = min(sales_list)

    print(f"Total Sales: ${total:,.2f}")
    print(f"Average: ${average:,.2f}")
    print(f"Highest: ${maximum:,.2f}")
    print(f"Lowest: ${minimum:,.2f}")

# Test it
my_sales = [100, 250, 175, 300, 125]
business_stats(my_sales)
```

---

## ✅ DAY 4 COMPLETE WHEN:

You can:
- [ ] Run Python code (Colab or local)
- [ ] Create variables and lists
- [ ] Write a simple function
- [ ] Load a CSV file
- [ ] Calculate basic statistics
- [ ] Print formatted results

---

**Time**: 5 hours | **Difficulty**: Medium | **Day**: 4/6

**Tomorrow**: Master Pandas for data analysis!
