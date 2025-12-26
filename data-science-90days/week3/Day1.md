# Week 3, Day 1: Introduction to Matplotlib - Telling Stories with Data

## 📚 What You'll Learn Today

- Why data visualization matters
- Creating your first plots with Matplotlib
- Line plots, scatter plots, and bar charts
- Customizing plots to communicate insights

---

## 🎯 The Story: The Coffee Shop's Revenue Mystery

**You're analyzing a coffee shop's sales data.** The owner asks: *"Are we making more money over time?"*

You could say: "Revenue went from $2,400 to $3,200 over 6 months."

Or you could **show them this**:

```
      Revenue ($)
3500  |                    ●
3000  |              ●   ●
2500  |        ●   ●
2000  |  ●   ●
      |___________________
       Jan Feb Mar Apr May Jun
```

**One glance tells the story.** That's the power of visualization.

---

## 📖 Core Concept: Why Visualize?

### The Problem with Numbers Alone

Which is easier to understand?

**Option 1: Raw Numbers**
```
January: 2400, February: 2550, March: 2700,
April: 2850, May: 3000, June: 3200
```

**Option 2: Visual**
A line going up consistently = growth trend

### When to Use Visualization

1. **Exploring data** - Find patterns you can't see in numbers
2. **Communicating insights** - Convince others with clear evidence
3. **Detecting outliers** - Spot weird data points instantly
4. **Comparing groups** - See differences at a glance

---

## 💻 Getting Started with Matplotlib

### Installation

```python
# In your terminal or command prompt
pip install matplotlib
```

### Your First Plot

```python
import matplotlib.pyplot as plt

# The data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [2400, 2550, 2700, 2850, 3000, 3200]

# Create the plot
plt.plot(months, revenue)
plt.title('Coffee Shop Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue ($)')
plt.show()
```

**That's it!** You've created a professional visualization.

---

## 📊 The Three Essential Plot Types

### 1. Line Plot - For Trends Over Time

**Use when**: Showing how something changes over time

```python
import matplotlib.pyplot as plt

# Daily temperature data
days = [1, 2, 3, 4, 5, 6, 7]
temperature = [72, 75, 73, 78, 80, 77, 76]

plt.plot(days, temperature, marker='o', color='red', linewidth=2)
plt.title('Weekly Temperature Trend')
plt.xlabel('Day')
plt.ylabel('Temperature (°F)')
plt.grid(True)  # Add grid lines
plt.show()
```

**Key customizations**:
- `marker='o'` - Show data points as circles
- `color='red'` - Change line color
- `linewidth=2` - Make line thicker
- `plt.grid(True)` - Add helpful grid lines

---

### 2. Scatter Plot - For Relationships

**Use when**: Checking if two things are related

**Story**: Does study time affect test scores?

```python
import matplotlib.pyplot as plt

# Student data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
test_scores = [60, 65, 70, 75, 80, 85, 88, 90]

plt.scatter(study_hours, test_scores, color='blue', s=100, alpha=0.6)
plt.title('Study Time vs Test Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.show()
```

**What this reveals**: More study time = higher scores (positive correlation)

**Key customizations**:
- `s=100` - Size of dots
- `alpha=0.6` - Transparency (0=invisible, 1=solid)

---

### 3. Bar Chart - For Comparisons

**Use when**: Comparing different categories

**Story**: Which product sells best?

```python
import matplotlib.pyplot as plt

# Product sales data
products = ['Latte', 'Cappuccino', 'Espresso', 'Americano']
sales = [150, 120, 80, 95]

plt.bar(products, sales, color=['brown', 'tan', 'black', 'gray'])
plt.title('Product Sales Comparison')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)  # Rotate labels for readability
plt.tight_layout()  # Prevent label cutoff
plt.show()
```

**What this reveals**: Latte is the top seller, Espresso needs promotion

**Key customizations**:
- `color=[...]` - Different color for each bar
- `rotation=45` - Angle labels so they fit
- `plt.tight_layout()` - Prevent labels from being cut off

---

## 🎨 Making Beautiful Plots

### The Anatomy of a Great Plot

Every good plot needs:

1. **Clear Title** - What am I looking at?
2. **Labeled Axes** - What do these numbers mean?
3. **Legend** (if multiple lines) - Which line is which?
4. **Appropriate Colors** - Easy to read, not garish
5. **Proper Scaling** - Don't exaggerate or minimize trends

### Example: Complete Professional Plot

```python
import matplotlib.pyplot as plt

# Website traffic data
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
organic = [1200, 1350, 1500, 1650]
paid = [800, 850, 900, 950]

# Create figure with specific size
plt.figure(figsize=(10, 6))

# Plot both lines
plt.plot(weeks, organic, marker='o', label='Organic Traffic',
         linewidth=2, color='green')
plt.plot(weeks, paid, marker='s', label='Paid Traffic',
         linewidth=2, color='blue')

# Customize
plt.title('Website Traffic Growth', fontsize=16, fontweight='bold')
plt.xlabel('Week', fontsize=12)
plt.ylabel('Visitors', fontsize=12)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
```

**Professional touches**:
- `figsize=(10, 6)` - Wider, easier to read
- `fontsize=16` - Larger title
- `label='...'` - Enables legend
- `loc='upper left'` - Legend position
- `alpha=0.3` - Subtle grid

---

## 🎯 Real-World Example: Sales Analysis

**Scenario**: You're analyzing monthly sales for different store locations.

```python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
store_a = [45000, 47000, 49000, 51000, 53000]
store_b = [38000, 39000, 41000, 40000, 42000]
store_c = [52000, 51000, 50000, 49000, 48000]

# Create the plot
plt.figure(figsize=(12, 6))

plt.plot(months, store_a, marker='o', label='Store A', linewidth=2)
plt.plot(months, store_b, marker='s', label='Store B', linewidth=2)
plt.plot(months, store_c, marker='^', label='Store C', linewidth=2)

plt.title('Store Performance Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.show()
```

**Insights from the visualization**:
- **Store A**: Consistent growth - doing well!
- **Store B**: Slight growth but with a dip in April
- **Store C**: Declining - needs immediate attention!

---

## 📝 Saving Your Plots

Don't just show plots on screen - save them for reports!

```python
import matplotlib.pyplot as plt

# Create your plot
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('My Chart')

# Save as PNG
plt.savefig('my_chart.png', dpi=300, bbox_inches='tight')

# Save as PDF (for presentations)
plt.savefig('my_chart.pdf', bbox_inches='tight')

# Then show it
plt.show()
```

**Parameters explained**:
- `dpi=300` - High resolution (good for printing)
- `bbox_inches='tight'` - No white space around plot

---

## 💡 Pro Tips

### 1. Choose the Right Plot Type
- **Time series?** → Line plot
- **Relationship?** → Scatter plot
- **Comparison?** → Bar chart
- **Distribution?** → Histogram (we'll learn tomorrow!)

### 2. Don't Overdo It
- Simple is better than fancy
- Too many colors = confusing
- 3-5 lines max on one plot

### 3. Think About Your Audience
- **For managers**: Big fonts, clear titles
- **For technical folks**: Can include more detail
- **For presentations**: High contrast colors

### 4. Common Mistakes to Avoid
- Missing axis labels (what do the numbers mean?)
- Titles that don't explain the insight
- Colors that are hard to distinguish
- Y-axis that doesn't start at 0 (can exaggerate trends)

---

## 🎯 Practice Exercises

### Exercise 1: Your First Line Plot (Warmup)

Create a line plot showing your daily productivity (on a scale of 1-10) over a week.

```python
import matplotlib.pyplot as plt

# Your data here
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
productivity = [7, 8, 6, 9, 8, 5, 4]  # Example data

# Create the plot
# Your code here
```

**Requirements**:
- Line plot with markers
- Title: "My Weekly Productivity"
- X-axis: "Day of Week"
- Y-axis: "Productivity Score"
- Add grid lines

---

### Exercise 2: Scatter Plot Analysis (Application)

You're analyzing if advertising spend affects sales.

```python
import matplotlib.pyplot as plt

ad_spend = [1000, 1500, 2000, 2500, 3000, 3500, 4000]
sales = [15000, 18000, 22000, 25000, 28000, 30000, 33000]

# Create a scatter plot
# Your code here
```

**Requirements**:
- Scatter plot
- Title: "Ad Spend vs Sales"
- X-axis: "Ad Spend ($)"
- Y-axis: "Sales ($)"
- Blue dots with 50% transparency
- What's the insight? (Is there a relationship?)

---

### Exercise 3: Multi-Line Comparison (Real-World)

Compare three different investment portfolios over 6 months.

```python
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
conservative = [10000, 10200, 10350, 10500, 10650, 10800]
moderate = [10000, 10300, 10500, 10800, 11000, 11300]
aggressive = [10000, 10500, 10200, 11000, 10800, 11500]

# Create a plot comparing all three
# Your code here
```

**Requirements**:
- Three lines on one plot
- Different colors for each portfolio
- Legend showing which is which
- Title: "Investment Portfolio Performance"
- Grid lines
- Save the plot as 'portfolios.png'

**Business Question**: Which portfolio had the best return? Which was most stable?

---

## 🎓 What You Learned Today

✅ Why visualization is crucial for data analysis
✅ Creating line plots for trends
✅ Creating scatter plots for relationships
✅ Creating bar charts for comparisons
✅ Customizing plots with titles, labels, colors
✅ Saving plots as image files
✅ Choosing the right visualization for your data

---

## 📚 Additional Resources

- [Matplotlib Official Documentation](https://matplotlib.org/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html) - Browse example plots
- [Color Names in Matplotlib](https://matplotlib.org/stable/gallery/color/named_colors.html)

---

## 🚀 Tomorrow's Preview

**Day 2: Seaborn & Advanced Visualizations**

We'll learn:
- Creating beautiful statistical plots with Seaborn
- Heatmaps and correlation matrices
- Distribution plots (histograms, box plots)
- Multi-panel dashboards

**Get ready to make your plots even more impressive!** 📊

---

## ✅ Check Your Understanding

Before moving on, make sure you can:
- [ ] Create a basic line plot
- [ ] Create a scatter plot
- [ ] Create a bar chart
- [ ] Add titles and axis labels
- [ ] Save a plot as an image
- [ ] Choose the appropriate plot type for different data

**Practice file**: See `assets/projects/week3/day7-practice.py` for complete solutions!

---

**Next**: [Day 2 - Seaborn & Statistical Visualizations](Day2.md)
