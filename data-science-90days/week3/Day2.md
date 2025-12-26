# Week 3, Day 2: Seaborn & Statistical Visualizations

## 📚 What You'll Learn Today

- Introduction to Seaborn for beautiful statistical plots
- Histograms and distribution plots
- Box plots for detecting outliers
- Heatmaps for correlation analysis
- Comparing multiple variables

---

## 🎯 The Story: The E-commerce Analytics Challenge

**You're analyzing an online store's customer data.** The marketing team asks:

1. *"What's the typical order value?"* → **Histogram**
2. *"Are there any unusual orders we should investigate?"* → **Box plot**
3. *"Which products are often bought together?"* → **Heatmap**

Today you'll learn to answer all these questions with powerful visualizations.

---

## 📖 Why Seaborn?

### Matplotlib vs Seaborn

**Matplotlib** (Yesterday):
- Low-level control
- Requires more code for complex plots
- Great for basic charts

**Seaborn** (Today):
- Built on top of Matplotlib
- Beautiful default styling
- Statistical plots with less code
- Perfect for data analysis

**Example comparison:**

```python
# Matplotlib - More code
import matplotlib.pyplot as plt
plt.hist(data, bins=20, edgecolor='black')
plt.title('Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Seaborn - Simpler, prettier
import seaborn as sns
sns.histplot(data, bins=20)
plt.title('Distribution')
plt.show()
```

---

## 💻 Getting Started with Seaborn

### Installation

```python
# In your terminal
pip install seaborn
```

### Basic Setup

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set style (makes plots beautiful automatically)
sns.set_style('whitegrid')  # Try: 'darkgrid', 'white', 'dark', 'ticks'
sns.set_palette('husl')  # Beautiful color palette
```

---

## 📊 Essential Statistical Plots

### 1. Histogram - Understanding Distributions

**Use when**: You want to see the shape of your data distribution

**Story**: What's the typical customer age?

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Customer age data
ages = np.random.normal(35, 10, 1000)  # Mean=35, spread=10, 1000 customers

# Create histogram
plt.figure(figsize=(10, 6))
sns.histplot(ages, bins=30, kde=True, color='skyblue')
plt.title('Customer Age Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Age', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.axvline(ages.mean(), color='red', linestyle='--',
            label=f'Average: {ages.mean():.1f}')
plt.legend()
plt.show()
```

**What you learn**:
- Most customers are 30-40 years old
- Few customers under 20 or over 60
- The red line shows average age

**Key parameter**:
- `kde=True` - Adds smooth curve showing the distribution shape

---

### 2. Box Plot - Finding Outliers

**Use when**: You want to spot unusual values and understand data spread

**Story**: Are there any suspiciously large orders?

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Order values
np.random.seed(42)
orders = np.random.gamma(50, 2, 200)  # Typical orders
orders = np.append(orders, [500, 520, 480])  # Add some suspicious large orders

plt.figure(figsize=(10, 6))
sns.boxplot(y=orders, color='lightcoral')
plt.title('Order Value Distribution - Outlier Detection',
          fontsize=16, fontweight='bold')
plt.ylabel('Order Value ($)', fontsize=12)
plt.show()
```

**Reading a box plot**:
```
     ●  ← Outlier (investigate this!)
     |
  ---|---  ← Maximum (within normal range)
  |     |
  | BOX |  ← Middle 50% of data (IQR)
  |     |
  ---|---  ← Minimum
     |
     ●  ← Outlier
```

- **Box**: Middle 50% of your data
- **Line in box**: Median (50th percentile)
- **Dots above/below**: Outliers (unusual values)

**Business insight**: Those $500+ orders might be fraud or bulk purchases!

---

### 3. Distribution Plot - Comparing Groups

**Use when**: Comparing distributions of different categories

**Story**: Do premium customers spend more than regular customers?

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)
data = pd.DataFrame({
    'Purchase': np.concatenate([
        np.random.normal(50, 15, 500),   # Regular customers
        np.random.normal(120, 25, 500)   # Premium customers
    ]),
    'Customer_Type': ['Regular']*500 + ['Premium']*500
})

plt.figure(figsize=(12, 6))
sns.histplot(data=data, x='Purchase', hue='Customer_Type',
             bins=40, kde=True, alpha=0.6)
plt.title('Purchase Amount by Customer Type',
          fontsize=16, fontweight='bold')
plt.xlabel('Purchase Amount ($)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()
```

**Insights**:
- Premium customers clearly spend more
- Regular customers: $30-$70 typical
- Premium customers: $70-$170 typical
- **Action**: Focus marketing on converting regular → premium!

---

### 4. Heatmap - Correlation Analysis

**Use when**: Finding relationships between multiple variables

**Story**: Which product sales are related?

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sales data for different products (daily)
np.random.seed(42)
products = pd.DataFrame({
    'Coffee': np.random.randint(50, 150, 30),
    'Pastries': np.random.randint(30, 100, 30),
    'Sandwiches': np.random.randint(40, 120, 30),
    'Smoothies': np.random.randint(20, 80, 30)
})

# Add correlation: Coffee buyers also buy pastries
products['Pastries'] = products['Coffee'] * 0.6 + np.random.randint(10, 30, 30)

# Calculate correlations
correlation_matrix = products.corr()

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm',
            center=0, square=True, linewidths=2)
plt.title('Product Sales Correlation', fontsize=16, fontweight='bold')
plt.show()
```

**Reading the heatmap**:
- **Red/Warm colors**: Positive correlation (when one goes up, other goes up)
- **Blue/Cool colors**: Negative correlation (when one goes up, other goes down)
- **Numbers**: Correlation strength (-1 to +1)

**Business insight**: Coffee and Pastries are highly correlated → bundle them together!

---

## 🎨 Advanced Seaborn Plots

### 5. Count Plot - Category Frequencies

**Story**: Which day of the week gets most orders?

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
orders_df = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] * 20
})

plt.figure(figsize=(10, 6))
sns.countplot(data=orders_df, x='Day',
              order=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
              palette='viridis')
plt.title('Orders by Day of Week', fontsize=16, fontweight='bold')
plt.xlabel('Day', fontsize=12)
plt.ylabel('Number of Orders', fontsize=12)
plt.show()
```

---

### 6. Violin Plot - Distribution + Density

**Story**: How do sales vary across different stores?

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sales data for 4 stores
np.random.seed(42)
sales_data = pd.DataFrame({
    'Sales': np.concatenate([
        np.random.normal(5000, 800, 100),   # Store A
        np.random.normal(7000, 1200, 100),  # Store B
        np.random.normal(4500, 600, 100),   # Store C
        np.random.normal(6500, 1000, 100)   # Store D
    ]),
    'Store': ['Store A']*100 + ['Store B']*100 +
             ['Store C']*100 + ['Store D']*100
})

plt.figure(figsize=(12, 6))
sns.violinplot(data=sales_data, x='Store', y='Sales', palette='muted')
plt.title('Sales Distribution by Store', fontsize=16, fontweight='bold')
plt.ylabel('Daily Sales ($)', fontsize=12)
plt.show()
```

**Violin plot** = Box plot + Distribution shape
- Wide parts = More data points at that value
- Narrow parts = Fewer data points

---

## 🎯 Real-World Example: Complete Analysis

**Scenario**: Analyzing employee satisfaction across departments

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample employee data
np.random.seed(42)
employees = pd.DataFrame({
    'Department': np.repeat(['Sales', 'Engineering', 'Marketing', 'HR'], 50),
    'Satisfaction': np.concatenate([
        np.random.normal(7, 1.5, 50),   # Sales
        np.random.normal(8, 1, 50),     # Engineering
        np.random.normal(6, 2, 50),     # Marketing
        np.random.normal(7.5, 1.2, 50)  # HR
    ]),
    'Salary': np.concatenate([
        np.random.normal(60000, 10000, 50),  # Sales
        np.random.normal(85000, 15000, 50),  # Engineering
        np.random.normal(55000, 8000, 50),   # Marketing
        np.random.normal(65000, 12000, 50)   # HR
    ])
})

# Create a multi-plot analysis
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Satisfaction by Department (Box plot)
sns.boxplot(data=employees, x='Department', y='Satisfaction',
            palette='Set2', ax=axes[0, 0])
axes[0, 0].set_title('Satisfaction by Department', fontweight='bold')
axes[0, 0].set_ylabel('Satisfaction Score (1-10)')

# 2. Salary Distribution (Histogram)
sns.histplot(data=employees, x='Salary', bins=30, kde=True,
             color='green', ax=axes[0, 1])
axes[0, 1].set_title('Salary Distribution', fontweight='bold')
axes[0, 1].set_xlabel('Salary ($)')

# 3. Salary vs Satisfaction (Scatter)
sns.scatterplot(data=employees, x='Salary', y='Satisfaction',
                hue='Department', s=100, alpha=0.6, ax=axes[1, 0])
axes[1, 0].set_title('Salary vs Satisfaction', fontweight='bold')

# 4. Department Counts
sns.countplot(data=employees, x='Department',
              palette='pastel', ax=axes[1, 1])
axes[1, 1].set_title('Employees per Department', fontweight='bold')
axes[1, 1].set_ylabel('Number of Employees')

plt.tight_layout()
plt.savefig('employee_analysis.png', dpi=300, bbox_inches='tight')
plt.show()
```

**Insights from this dashboard**:
1. **Engineering** has highest satisfaction
2. **Engineering** also has highest salaries (correlation?)
3. **Marketing** has most variable satisfaction (investigate!)
4. All departments evenly staffed

---

## 💡 Pro Tips

### 1. Choosing Color Palettes

```python
# For categories
sns.set_palette('Set2')      # Soft colors
sns.set_palette('Dark2')     # Bold colors
sns.set_palette('Pastel1')   # Light colors

# For heatmaps
cmap='coolwarm'  # Blue to Red (good for correlations)
cmap='viridis'   # Yellow to Purple (good for continuous data)
cmap='RdYlGn'    # Red-Yellow-Green (good for good/bad values)
```

### 2. Style Themes

```python
sns.set_style('whitegrid')   # White with grid
sns.set_style('darkgrid')    # Gray with grid
sns.set_style('white')       # Clean white
sns.set_style('ticks')       # White with axis ticks
```

### 3. Figure Size Matters

```python
# Too small = hard to read
plt.figure(figsize=(6, 4))

# Good for presentations
plt.figure(figsize=(12, 6))

# Multi-plot dashboard
plt.figure(figsize=(14, 10))
```

---

## 🎯 Practice Exercises

### Exercise 1: Customer Age Distribution (Warmup)

Analyze customer ages and find the typical age range.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Customer ages
np.random.seed(123)
customer_ages = np.random.gamma(4, 8, 500)  # Realistic age distribution

# Create a histogram with KDE
# Your code here
```

**Requirements**:
- Histogram with 25 bins
- KDE overlay
- Title: "Customer Age Distribution"
- Add vertical line at median age
- What age range contains most customers?

---

### Exercise 2: Department Performance (Application)

Compare sales performance across 4 departments.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

# Create a box plot to compare departments
# Your code here
```

**Requirements**:
- Box plot showing all 4 departments
- Horizontal layout (switch x and y)
- Title: "Sales Performance by Department"
- Which department has the most consistent sales?
- Which has the most outliers?

---

### Exercise 3: Multi-Variable Analysis Dashboard (Real-World)

Create a comprehensive analysis dashboard for website metrics.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Website metrics
np.random.seed(42)
web_data = pd.DataFrame({
    'Page_Views': np.random.poisson(500, 100),
    'Time_on_Site': np.random.normal(180, 60, 100),  # seconds
    'Bounce_Rate': np.random.beta(2, 5, 100) * 100,   # percentage
    'Conversions': np.random.poisson(15, 100)
})

# Create a 2x2 dashboard with:
# 1. Page Views distribution (histogram)
# 2. Time on Site vs Bounce Rate (scatter)
# 3. Correlation heatmap (all variables)
# 4. Conversions distribution (box plot)
# Your code here
```

**Requirements**:
- 2x2 subplot layout
- Each plot properly titled and labeled
- Save as 'web_metrics_dashboard.png'
- Write 3 insights you discover from the visualizations

---

## 🎓 What You Learned Today

✅ Creating beautiful plots with Seaborn
✅ Histograms for understanding distributions
✅ Box plots for outlier detection
✅ Heatmaps for correlation analysis
✅ Comparing multiple groups with violins and distributions
✅ Building multi-panel dashboards
✅ Choosing appropriate colors and styles

---

## 📚 Additional Resources

- [Seaborn Official Documentation](https://seaborn.pydata.org/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Color Palettes Guide](https://seaborn.pydata.org/tutorial/color_palettes.html)

---

## 🚀 Tomorrow's Preview

**Day 3: Real-World Visualization Project**

We'll build:
- Complete data analysis dashboard
- COVID-19 data visualization project
- Interactive multi-panel reports
- Export-ready professional graphics

**You'll apply everything you've learned to a real dataset!** 📊

---

## ✅ Check Your Understanding

Before moving on, make sure you can:
- [ ] Create histograms with KDE curves
- [ ] Use box plots to identify outliers
- [ ] Create and interpret heatmaps
- [ ] Compare distributions across groups
- [ ] Build multi-panel dashboards
- [ ] Choose appropriate color schemes

**Practice file**: See `assets/projects/week3/day8-practice.py` for complete solutions!

---

**Next**: [Day 3 - Real-World Visualization Project](Day3.md)
