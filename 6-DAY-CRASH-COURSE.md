# 🚀 6-DAY DATA SCIENCE CRASH COURSE FOR BUSINESS

**Get business-ready data skills in just 6 days**
**Focus: Immediate practical value for your business**

---

## ⚡ Reality Check

You **CANNOT** become a full data scientist in 6 days. But you **CAN**:

✅ Analyze your business data confidently
✅ Create insightful dashboards
✅ Make data-driven decisions
✅ Understand what's possible with data
✅ Know where to go deeper later

**This is NOT about completing the full curriculum - it's about getting USABLE skills NOW.**

---

## 🎯 What You'll Actually Learn

By Day 6, you'll be able to:
- ✅ Clean and organize messy business data (Excel/Sheets)
- ✅ Calculate key business metrics automatically
- ✅ Create professional charts and dashboards
- ✅ Spot trends and patterns in your data
- ✅ Present insights to stakeholders
- ✅ Know basic Python for simple automation

**Realistic outcome**: Junior analyst skills with Excel + basic Python exposure

---

## 📅 6-DAY INTENSIVE SCHEDULE

### Time Commitment Per Day:
- **Minimum**: 3 hours (bare bones)
- **Recommended**: 5 hours (solid learning)
- **Ambitious**: 8 hours (intensive immersion)

**Total**: 18-48 hours of focused learning over 6 days

---

## DAY 1: Data Fundamentals & Excel Basics (Foundation Day)

**Goal**: Understand what data is and master basic Excel operations

### Morning Session (2-3 hours)
📖 **Learn**:
- Read: [data-analysis-90days/week1/Day1.md](data-analysis-90days/week1/Day1.md) - What is Data?
- Read: [data-analysis-90days/week1/Day2.md](data-analysis-90days/week1/Day2.md) - Spreadsheet Basics

✍️ **Practice**:
- Set up Google Sheets account
- Complete: [data-analysis-90days/week1/practice/day1_exercises.md](data-analysis-90days/week1/practice/day1_exercises.md)
- Create your first organized dataset

### Afternoon Session (2-3 hours)
📖 **Learn**:
- Read: [data-analysis-90days/week1/Day3.md](data-analysis-90days/week1/Day3.md) - Basic Formulas

✍️ **Practice**:
- Master: SUM, AVERAGE, COUNT, MIN, MAX
- Practice: Apply formulas to sample business data
- Build: Simple sales calculator

### Evening Reflection (30 min)
📝 **Apply to YOUR Business**:
- What data do you already have? (sales, customers, expenses)
- What questions do you want to answer?
- What metrics matter most?

**Day 1 Deliverable**: ✅ Simple spreadsheet analyzing your business data with basic formulas

---

## DAY 2: Data Cleaning & Advanced Formulas (Power User Day)

**Goal**: Clean messy data and use advanced Excel functions

### Morning Session (2-3 hours)
📖 **Learn**:
- Read: [data-analysis-90days/week1/Day4.md](data-analysis-90days/week1/Day4.md) - Data Organization
- Read: [data-analysis-90days/week2/Day8.md](data-analysis-90days/week2/Day8.md) - Data Cleaning

✍️ **Practice**:
- Clean duplicate records
- Fix formatting issues
- Handle missing data
- Use TRIM, PROPER functions

### Afternoon Session (2-3 hours)
📖 **Learn**:
- Read: [data-analysis-90days/week2/Day10.md](data-analysis-90days/week2/Day10.md) - IF, AND, OR Functions
- Skim: [data-analysis-90days/week2/Day11-14-Combined.md](data-analysis-90days/week2/Day11-14-Combined.md) - VLOOKUP basics

✍️ **Practice**:
- Build IF statements for categorization
- Use VLOOKUP to match data between sheets
- Create conditional calculations

### Evening Application (1-2 hours)
🎯 **Build**: Clean your actual business data
- Import your messy data (sales, customers, etc.)
- Clean and organize it properly
- Add calculated columns (profit margins, customer segments, etc.)

**Day 2 Deliverable**: ✅ Clean, organized business dataset with advanced formulas

---

## DAY 3: Visualization & Dashboards (Insight Day)

**Goal**: Create charts and dashboards that reveal business insights

### Morning Session (2-3 hours)
📖 **Learn**:
- Read: [data-analysis-90days/week1/Day5.md](data-analysis-90days/week1/Day5.md) - Sorting & Filtering
- Read: [data-analysis-90days/week3/Days15-21-Complete.md](data-analysis-90days/week3/Days15-21-Complete.md) - Focus on Days 15-17 (Charts)

✍️ **Practice**:
- Create bar charts, line charts, pie charts
- Understand when to use each chart type
- Format charts professionally

### Afternoon Session (3-4 hours)
📖 **Learn**:
- Read: [data-analysis-90days/week3/Days15-21-Complete.md](data-analysis-90days/week3/Days15-21-Complete.md) - Days 17-20 (Pivot Tables)

✍️ **Practice**:
- Build your first pivot table
- Analyze data from multiple angles
- Create pivot charts

### Evening Project (2 hours)
🎯 **Build**: Business Dashboard
- Create 3-5 key visualizations for YOUR business
- Use pivot tables for analysis
- Design a one-page dashboard
- Add conditional formatting for quick insights

**Day 3 Deliverable**: ✅ Interactive dashboard showing your business KPIs

---

## DAY 4: Python Basics & Data Setup (Automation Introduction)

**Goal**: Understand Python fundamentals and set up for data analysis

### Morning Session (2-3 hours)
📖 **Learn**:
- Review: [data-science-90days/week1/Day1.md](data-science-90days/week1/Day1.md) - Python Setup
- Review: [data-science-90days/assets/projects/week1/day1-practice.py](data-science-90days/assets/projects/week1/day1-practice.py)

✍️ **Practice**:
- Install Python (if not done)
- Set up Jupyter Notebook OR Google Colab
- Run first Python code
- Variables, data types, basic operations

### Afternoon Session (2-3 hours)
📖 **Learn**:
- Read: [data-science-90days/week1/Day2.md](data-science-90days/week1/Day2.md) - Lists, Loops

✍️ **Practice**:
- Create lists of business data
- Loop through data
- Basic calculations with Python
- Read CSV files

### Evening Practice (1-2 hours)
🎯 **Code**:
- Load your business data CSV into Python
- Calculate basic statistics (total sales, average, etc.)
- Print formatted results

**Day 4 Deliverable**: ✅ Python script that loads and analyzes your business data

---

## DAY 5: Pandas Basics (Real Data Analysis)

**Goal**: Use Pandas library for professional data analysis

### Morning Session (3 hours)
📖 **Learn**:
- Install Pandas: `pip install pandas`
- Learn DataFrame basics
- Read CSV files with Pandas
- Basic operations (head, describe, info)

✍️ **Practice**:
```python
import pandas as pd

# Load your data
df = pd.read_csv('your_business_data.csv')

# Explore it
print(df.head())
print(df.describe())
print(df.info())

# Basic analysis
total_sales = df['sales'].sum()
avg_sales = df['sales'].mean()
top_products = df.groupby('product')['sales'].sum().sort_values(ascending=False)

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Average Sale: ${avg_sales:,.2f}")
print("\nTop Products:")
print(top_products)
```

### Afternoon Session (3 hours)
📖 **Learn**:
- Filtering data with Pandas
- Grouping and aggregating
- Creating new calculated columns
- Basic data cleaning with Pandas

✍️ **Practice**:
```python
# Filter data
high_value = df[df['sales'] > 1000]

# Group by category
category_sales = df.groupby('category').agg({
    'sales': ['sum', 'mean', 'count']
})

# Add calculated column
df['profit'] = df['revenue'] - df['cost']
df['profit_margin'] = (df['profit'] / df['revenue']) * 100

# Export results
category_sales.to_csv('category_analysis.csv')
```

### Evening Project (2 hours)
🎯 **Build**: Automated Analysis Script
- Create Python script that loads YOUR data
- Calculates all key business metrics
- Exports summary report
- Can be run repeatedly as data updates

**Day 5 Deliverable**: ✅ Reusable Python script for automated business analysis

---

## DAY 6: Real Business Project & Integration (Application Day)

**Goal**: Apply everything to solve a real business problem

### Morning: Choose Your Project (30 min)

Pick ONE real business problem:

**Option 1: Sales Analysis Dashboard**
- Which products sell best?
- Which customers are most valuable?
- What are the trends over time?
- Where should we focus efforts?

**Option 2: Customer Segmentation**
- Who are our different customer types?
- What do high-value customers look like?
- Who's at risk of churning?
- Who should we target for marketing?

**Option 3: Expense Optimization**
- Where is money being spent?
- What are unnecessary expenses?
- What's the ROI on different activities?
- Where can we cut costs?

**Option 4: Performance Tracking**
- What are our key KPIs?
- How are we trending?
- Are we meeting goals?
- What needs attention?

### Full Day Project (6-7 hours)

🎯 **Execute Your Project**:

1. **Define the Question** (30 min)
   - What specific business question are you answering?
   - What data do you need?
   - What would success look like?

2. **Gather & Clean Data** (1-2 hours)
   - Collect all relevant data
   - Import into Excel/Python
   - Clean and organize
   - Handle missing/bad data

3. **Analyze** (2-3 hours)
   - Calculate metrics
   - Create aggregations
   - Find patterns and trends
   - Generate insights

4. **Visualize** (1-2 hours)
   - Create charts in Excel OR
   - Use Python matplotlib/seaborn OR
   - Both (dashboard in Excel, automation in Python)

5. **Document Findings** (1 hour)
   - What did you discover?
   - What are the key insights?
   - What actions should be taken?
   - Create 1-page summary

### Evening: Presentation Prep (1-2 hours)

📊 **Create Business Presentation**:
- One-page dashboard (visual)
- Key findings (3-5 bullet points)
- Recommendations (what to do)
- Next steps (what to investigate further)

**Day 6 Deliverable**: ✅ Complete analysis project solving real business problem

---

## 🎯 End of 6 Days: What You'll Have

### Skills Acquired:
✅ Excel/Google Sheets mastery (formulas, pivot tables, charts)
✅ Data cleaning and organization
✅ Business metrics calculation
✅ Dashboard creation
✅ Basic Python programming
✅ Pandas for data analysis
✅ Data-driven decision making

### Deliverables:
1. ✅ Clean business dataset
2. ✅ Interactive Excel dashboard
3. ✅ Python analysis script
4. ✅ Complete business project with insights
5. ✅ Presentation-ready findings

### Business Impact:
- 📊 Understand your data deeply
- 🎯 Make informed decisions
- 💰 Identify opportunities and issues
- 🚀 Automate repetitive analysis
- 📈 Track metrics systematically

---

## 📚 Resources for Each Day

### Tools You MUST Have:
1. **Google Sheets** (free) - sheets.google.com
2. **Python 3.x** - python.org/downloads
3. **Jupyter Notebook** OR **Google Colab** (colab.research.google.com)
4. **Your actual business data** (CSV format)

### Learning Materials:
- ✅ All lessons already in this repository
- ✅ Practice exercises included
- ✅ Example code in data-science-90days
- ✅ Detailed tutorials in data-analysis-90days

---

## ⚠️ Critical Success Factors

### DO:
✅ Focus on YOUR business data from Day 1
✅ Actually BUILD things, don't just read
✅ Prioritize understanding over completion
✅ Apply each skill immediately to real problems
✅ Take breaks - your brain needs processing time
✅ Skip advanced topics that don't apply to your business

### DON'T:
❌ Try to learn everything in the full curriculum
❌ Get stuck on perfection - done is better than perfect
❌ Skip the hands-on practice
❌ Use only toy/example data - use REAL data
❌ Multitask - give full focus when learning
❌ Stress about what you're missing - you can learn more later

---

## 📊 Daily Time Allocation (Recommended 5-hour plan)

```
Day 1: Excel Fundamentals
├─ 2h: Learn concepts (read lessons)
├─ 2h: Practice exercises
└─ 1h: Apply to your data

Day 2: Advanced Excel
├─ 2h: Data cleaning & formulas
├─ 2h: Practice advanced functions
└─ 1h: Clean your business data

Day 3: Visualization
├─ 2h: Charts and pivot tables
├─ 2h: Practice visualization
└─ 1h: Build your dashboard

Day 4: Python Basics
├─ 2h: Setup & fundamentals
├─ 2h: Lists, loops, file reading
└─ 1h: Load your data in Python

Day 5: Pandas Analysis
├─ 2h: Learn Pandas basics
├─ 2h: Practice data manipulation
└─ 1h: Create analysis script

Day 6: Real Project
├─ 1h: Define problem & gather data
├─ 2h: Analyze and find insights
├─ 1h: Create visualizations
└─ 1h: Document & present
```

---

## 🎯 After Day 6: What's Next?

### Immediate Next Steps:
1. **Use your new skills** in daily business operations
2. **Automate** repetitive analysis tasks
3. **Share insights** with your team
4. **Track metrics** regularly

### Continue Learning (After Your 6-Day Push):
- **Weeks 1-3**: Complete data-analysis-90days fully (solidify Excel/Sheets)
- **Weeks 4-5**: Learn SQL for database querying
- **Weeks 6-9**: Deep dive into Python and Pandas
- **Weeks 10-13**: Advanced projects and portfolio building

### Or Focus on Business:
- Apply what you learned to grow your business
- Learn more only when you hit specific limitations
- Hire specialists for advanced needs
- You now UNDERSTAND data enough to make smart decisions

---

## 💡 Pro Tips for 6-Day Success

### Learning Strategies:
1. **Batch similar content** - Don't jump between topics
2. **Practice immediately** - Read → Do → Apply (within same session)
3. **Use real data** - Your business data makes learning stick
4. **Focus on 80/20** - Master the 20% that gives 80% value
5. **Document as you go** - Notes help retention

### Time Management:
1. **Block calendar** - Treat this like urgent business
2. **Eliminate distractions** - No social media during learning
3. **Take strategic breaks** - 50 min work, 10 min break
4. **Sleep well** - Your brain consolidates learning during sleep
5. **Front-load hard topics** - Do complex stuff when fresh

### Staying Motivated:
1. **Track progress** - Check off each completed section
2. **Celebrate wins** - Acknowledge each deliverable
3. **Visualize the end** - Imagine using these skills in business
4. **Connect to purpose** - Remember WHY this matters
5. **Share journey** - Post daily updates (#6DayDataChallenge)

---

## 🏆 Success Metrics

### End of Day 1:
- [ ] Created organized spreadsheet with formulas
- [ ] Analyzed sample business data
- [ ] Understand data types and organization

### End of Day 2:
- [ ] Cleaned messy real data
- [ ] Used IF statements and VLOOKUP
- [ ] Built calculations for business metrics

### End of Day 3:
- [ ] Created professional charts
- [ ] Built pivot table analysis
- [ ] Designed 1-page dashboard

### End of Day 4:
- [ ] Set up Python environment
- [ ] Wrote basic Python code
- [ ] Loaded CSV file and did calculations

### End of Day 5:
- [ ] Used Pandas for data analysis
- [ ] Created automated analysis script
- [ ] Exported results programmatically

### End of Day 6:
- [ ] Completed full business project
- [ ] Generated actionable insights
- [ ] Created presentation-ready deliverable
- [ ] **CAN USE DATA SCIENCE IN YOUR BUSINESS!**

---

## 📞 Quick Reference: Where to Find What

| Need | Location |
|------|----------|
| Excel basics | data-analysis-90days/week1/ |
| Data cleaning | data-analysis-90days/week2/ |
| Charts & pivot tables | data-analysis-90days/week3/ |
| Python setup | data-science-90days/week1/Day1.md |
| Python practice code | data-science-90days/assets/projects/week1/ |
| Full curriculum overview | README.md |

---

## 🚀 START NOW!

**You have 6 days. That's 144 hours. You're dedicating ~30 of them to learning data skills.**

**In 6 days, you'll go from zero to analyzing your business data confidently.**

**The clock is ticking. Every hour counts.**

---

# 👉 BEGIN DAY 1 NOW:

1. **Open**: [data-analysis-90days/week1/Day1.md](data-analysis-90days/week1/Day1.md)
2. **Read** for 20 minutes
3. **Practice** for 40 minutes
4. **Apply** to your data for 20 minutes
5. **Repeat** with Day 2 content

---

**Stop reading plans. Start executing.**

**Your 6-day transformation starts RIGHT NOW!** 🚀⏰

---

*Created for urgent business needs | Focus on results, not perfection | You've got this!* 💪
