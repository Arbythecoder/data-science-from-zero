# Week 3: Complete Daily Lessons (Days 15-21)

**Work through each day separately - combined here for your convenience!**

---

# 📅 Day 15: Introduction to Pivot Tables

**Goal**: Create your first pivot table and understand its power

---

## 🧠 What is a Pivot Table?

**Pivot Table** = Interactive summary table that automatically groups and calculates data

**Without Pivot Table** ❌:
```
Manually calculate total sales per region:
=SUMIF(Region, "Lagos", Sales) → Lagos total
=SUMIF(Region, "Abuja", Sales) → Abuja total
... repeat for each region
```

**With Pivot Table** ✅:
```
Drag "Region" to Rows
Drag "Sales" to Values
Done! All regions automatically calculated!
```

---

## 💡 When to Use Pivot Tables

Use when you need to:
- Summarize large datasets quickly
- Group data by categories
- Calculate totals, averages, counts
- See data from different perspectives
- Answer "how much" or "how many" questions

**Example Questions Pivot Tables Answer**:
- "What's total sales by region?"
- "How many orders per month?"
- "Which product category sells best?"
- "Average purchase value by customer type?"

---

## 🛠️ Creating Your First Pivot Table

### Sample Data

**Create this sales data**:
```
   A          B          C          D         E
1  Date       Region     Category   Product   Sales
2  2024-01-01 Lagos      Electronics Laptop   50000
3  2024-01-02 Abuja      Food        Rice     800
4  2024-01-03 Lagos      Clothing    Shirt    2500
5  2024-01-04 Ibadan     Electronics Phone    35000
[Add 20 more rows with mix of regions, categories, products]
```

### Steps to Create Pivot Table

**Google Sheets**:
1. Select your data (A1:E25)
2. **Insert → Pivot table**
3. Choose "New sheet"
4. Click "Create"

**Excel**:
1. Select your data
2. **Insert → PivotTable**
3. Choose "New Worksheet"
4. Click "OK"

### Building the Pivot Table

**You'll see 4 areas**:
- **Filters**: Filter entire pivot table
- **Rows**: What to group by (vertical)
- **Columns**: Secondary grouping (horizontal)
- **Values**: What to calculate (numbers)

---

## 📊 Example 1: Sales by Region

**Question**: What's total sales per region?

**Setup**:
- **Rows**: Region
- **Values**: SUM of Sales

**Result**:
```
Region      Total Sales
Lagos       ₦150,000
Abuja       ₦85,000
Ibadan      ₦120,000
```

**One drag = instant summary!**

---

## 📊 Example 2: Sales by Category and Region

**Question**: Break down sales by both region and category

**Setup**:
- **Rows**: Region
- **Columns**: Category
- **Values**: SUM of Sales

**Result**:
```
               Electronics  Food     Clothing   Total
Lagos          ₦80,000     ₦20,000  ₦50,000    ₦150,000
Abuja          ₦50,000     ₦15,000  ₦20,000    ₦85,000
Ibadan         ₦70,000     ₦25,000  ₦25,000    ₦120,000
```

**Two-dimensional view instantly!**

---

## 🎯 Practice: Create 3 Pivot Tables

Using your sales data:

**Pivot 1**: Total sales by Category
- Rows: Category
- Values: SUM of Sales

**Pivot 2**: Number of transactions by Region
- Rows: Region
- Values: COUNT of Sales

**Pivot 3**: Average sale value by Product
- Rows: Product
- Values: AVERAGE of Sales

---

# 📅 Day 16: Advanced Pivot Table Techniques

**Goal**: Master grouping, calculated fields, and multiple values

---

## 📅 Grouping Dates

**Your data has daily dates**:
```
2024-01-01, 2024-01-02, 2024-01-03...
```

**You want monthly summary**:
```
January: ₦500,000
February: ₦450,000
March: ₦600,000
```

**How To**:
1. Right-click on date field in pivot table
2. **Create pivot date group**
3. Choose: Month, Quarter, or Year
4. Dates automatically group!

**Example**:
```
Month        Total Sales
Jan 2024     ₦500,000
Feb 2024     ₦450,000
Mar 2024     ₦600,000
```

---

## 🧮 Calculated Fields

**Add custom calculations to pivot tables**

**Example**: Calculate Profit if you have Revenue and Cost

**Steps**:
1. Click in pivot table
2. **Data → Calculated field** (Google Sheets)
   - Or **PivotTable Analyze → Fields, Items & Sets → Calculated Field** (Excel)
3. Name: "Profit"
4. Formula: `=Revenue-Cost`
5. Click Add

**Now you can add "Profit" to Values!**

---

## 📊 Multiple Value Fields

**Show multiple calculations at once**

**Example**: For each product, show:
- Total sales (SUM)
- Number of transactions (COUNT)
- Average sale value (AVERAGE)

**Setup**:
- Rows: Product
- Values:
  - SUM of Sales
  - COUNT of Sales
  - AVERAGE of Sales

**Result**:
```
Product   Total Sales  Transactions  Avg Sale
Laptop    ₦500,000     10            ₦50,000
Phone     ₦350,000     15            ₦23,333
Tablet    ₦250,000     12            ₦20,833
```

---

## 🎯 Practice: Time-Based Analysis

**Create monthly sales trend**:
1. Rows: Date (grouped by Month)
2. Values: SUM of Sales
3. Create line chart from this pivot

**Analyze**:
- Which month had highest sales?
- Is there a trend?
- Any seasonal patterns?

---

# 📅 Day 17: Chart Types & When to Use Them

**Goal**: Choose the right chart for your data

---

## 📊 Chart Selection Guide

### Line Chart - Trends Over Time

**When**: Show how something changes over time

**Best for**:
- Monthly sales trends
- Temperature over days
- Stock prices
- Website traffic

**Example**: Monthly revenue for 12 months

**How to Create**:
1. Select data (dates and values)
2. Insert → Chart
3. Choose Line chart
4. Customize title and labels

---

### Bar/Column Chart - Compare Categories

**When**: Compare values across different categories

**Best for**:
- Sales by product
- Scores by student
- Population by city
- Revenue by region

**Horizontal Bar** vs **Vertical Column**:
- Horizontal: Better for long category names
- Vertical: Better for time periods or many categories

---

### Pie Chart - Parts of a Whole

**When**: Show percentage breakdown

**Best for**:
- Market share
- Budget allocation
- Category distribution

**Rules**:
- ⚠️ Use max 5-7 slices (more = confusing)
- ⚠️ Don't use for comparing over time
- ✅ Great for "what percent of total"

---

### Scatter Plot - Relationship Between Two Variables

**When**: Show correlation or relationship

**Best for**:
- Price vs. sales volume
- Height vs. weight
- Study hours vs. test scores
- Age vs. income

**Reveals**: Are two things related?

---

### Combo Chart - Multiple Metrics

**When**: Show two different types of data together

**Example**: Sales (bars) and Profit Margin % (line) on same chart

**Best for**:
- Different scales (revenue in millions, margin in %)
- Related but different metrics

---

## 🎯 Practice: Create 5 Charts

Using your sales data:

1. **Line**: Monthly sales trend
2. **Bar**: Total sales by category
3. **Pie**: Sales distribution by region
4. **Scatter**: Quantity vs. Revenue
5. **Combo**: Sales (bars) + Number of transactions (line)

---

# 📅 Day 18: Creating Professional Charts

**Goal**: Format charts to look professional and communicate clearly

---

## 🎨 Chart Formatting Best Practices

### 1. Clear Title

❌ Bad: "Chart 1"
✅ Good: "Monthly Sales Trend - Q1 2024"

**How**: Double-click chart → Edit title

### 2. Label Axes

**X-axis**: What's being measured (months, products, etc.)
**Y-axis**: The values (sales, count, percentage)

### 3. Remove Clutter

**Remove**:
- Unnecessary gridlines
- Borders
- Background colors (unless purposeful)
- 3D effects

**Keep it clean!**

### 4. Use Color Purposefully

**Good Uses**:
- Highlight most important data point
- Differentiate categories
- Show positive (green) vs negative (red)

**Avoid**:
- Too many colors
- Random colors
- Colors that don't mean anything

### 5. Add Data Labels (When Helpful)

**When to use**:
- Few data points (< 10)
- Exact values matter
- Making presentation slides

**When to skip**:
- Many data points (clutters chart)
- Trend is more important than exact values

---

## 📊 Chart Makeover Example

**Before** ❌:
- Title: "Chart 1"
- No axis labels
- Rainbow colors
- 3D effects
- Gridlines everywhere

**After** ✅:
- Title: "Q1 2024 Sales by Region"
- X-axis: "Region"
- Y-axis: "Sales (₦ thousands)"
- Consistent blue bars
- Clean, minimal gridlines
- Values labeled on bars

---

## 🎯 Today's Assignment

**Take one of your charts from Day 17 and make it professional**:

Checklist:
- [ ] Descriptive title
- [ ] Axis labels
- [ ] Appropriate colors
- [ ] Clean design (no clutter)
- [ ] Legend (if needed)
- [ ] Data labels (if helpful)

**Screenshot before and after!**

---

# 📅 Day 19: Conditional Formatting

**Goal**: Use color to highlight patterns and outliers

---

## 🎨 What is Conditional Formatting?

**Automatic coloring** based on cell values

**Example**:
- Sales > ₦100,000 → Green background
- Sales < ₦50,000 → Red background
- Sales between → Yellow background

**Why?** Spot patterns instantly without reading numbers!

---

## 🛠️ Types of Conditional Formatting

### 1. Color Scales

**What**: Gradient from low (red) to high (green)

**How**:
1. Select data range
2. Format → Conditional formatting
3. Color scale
4. Choose min/max colors

**Best for**: Heatmaps, comparing many values

---

### 2. Data Bars

**What**: Horizontal bars inside cells

**Example**:
```
Sales
₦50,000  ▓▓▓▓▓░░░░░  (50% bar)
₦100,000 ▓▓▓▓▓▓▓▓▓▓  (100% bar)
₦25,000  ▓▓░░░░░░░░  (25% bar)
```

**Best for**: Quick visual comparison

---

### 3. Icon Sets

**What**: Icons based on value ranges

**Example**:
```
Performance
95%  ↑ (green arrow)
75%  → (yellow arrow)
45%  ↓ (red arrow)
```

**Best for**: Status indicators, performance metrics

---

### 4. Custom Rules

**Create your own conditions**

**Example**: Highlight if sales > target

**Formula**: `=B2>C2`

**Steps**:
1. Select data
2. Conditional formatting → Custom formula
3. Enter: `=B2>C2`
4. Choose format (background color)
5. Apply

---

## 🎯 Practice: Create Performance Dashboard

**Data**:
```
   A           B          C          D
1  Rep Name    Sales      Target     Status
2  John        150000     100000
3  Jane        80000      100000
4  David       120000     100000
```

**Apply**:
1. **Color scale** on Sales (B column)
2. **Data bars** on Sales
3. **Custom rule**: If Sales > Target, green background
4. **Icon set**: On Status column using formula

**Result**: Visual dashboard showing who's hitting targets!

---

# 📅 Day 20: Dashboard Project - Sales Dashboard

**Goal**: Build complete executive dashboard

---

## 🏆 The Project

### Scenario

Create an executive sales dashboard for Q1 2024 showing:
- KPIs (key performance indicators)
- Trends over time
- Category breakdown
- Regional distribution
- Top performers

### Sample Data (Create 100+ rows)

```
Date       | Region | Category     | Product | Quantity | Revenue
2024-01-01 | Lagos  | Electronics  | Laptop  | 2        | 100000
2024-01-02 | Abuja  | Food         | Rice    | 10       | 8000
[... 100+ rows of varied data]
```

---

## 📊 Dashboard Layout

**Top Section - KPIs** (Row 1-5):
```
┌────────────┬────────────┬────────────┬────────────┐
│ Total      │ Total      │ Average    │ Number of  │
│ Revenue    │ Quantity   │ Sale       │ Orders     │
│ ₦5,200,000 │ 1,250      │ ₦41,600    │ 125        │
└────────────┴────────────┴────────────┴────────────┘
```

**Formulas**:
- Total Revenue: `=SUM(Data!F:F)`
- Total Quantity: `=SUM(Data!E:E)`
- Average Sale: `=AVERAGE(Data!F:F)`
- Number of Orders: `=COUNTA(Data!A:A)-1`

---

**Left Section - Pivot Tables**:

**Pivot 1**: Sales by Month
```
Month      Revenue
January    ₦1,800,000
February   ₦1,700,000
March      ₦1,700,000
```

**Pivot 2**: Sales by Category
```
Category       Revenue
Electronics    ₦3,000,000
Food           ₦1,200,000
Clothing       ₦1,000,000
```

**Pivot 3**: Sales by Region
```
Region     Revenue
Lagos      ₦2,500,000
Abuja      ₦1,500,000
Ibadan     ₦1,200,000
```

---

**Right Section - Charts**:

**Chart 1**: Monthly Trend (Line chart from Pivot 1)
**Chart 2**: Category Breakdown (Bar chart from Pivot 2)
**Chart 3**: Regional Distribution (Pie chart from Pivot 3)

---

**Bottom Section - Top 10 Products**:

Table with conditional formatting:
```
Product   Revenue    Units    Avg Price  [Color Scale]
Laptop    ₦800,000   16       ₦50,000    [Dark Green]
Phone     ₦600,000   20       ₦30,000    [Green]
Tablet    ₦400,000   16       ₦25,000    [Light Green]
...
```

---

## ✅ Dashboard Checklist

**Data**:
- [ ] 100+ rows of sample sales data
- [ ] Dates, regions, categories, products
- [ ] Realistic values

**KPIs Section**:
- [ ] Total revenue
- [ ] Total quantity
- [ ] Average sale
- [ ] Order count
- [ ] Formatted with borders and colors

**Pivot Tables** (3):
- [ ] By month
- [ ] By category
- [ ] By region
- [ ] Properly formatted

**Charts** (3):
- [ ] Line chart (trend)
- [ ] Bar chart (categories)
- [ ] Pie chart (regions)
- [ ] Professional formatting
- [ ] Clear titles and labels

**Conditional Formatting**:
- [ ] Applied to top products table
- [ ] Color scale or data bars
- [ ] Easy to interpret

**Overall**:
- [ ] Clean layout
- [ ] Professional appearance
- [ ] All sections aligned
- [ ] Consistent fonts and colors
- [ ] Tells clear data story

---

# 📅 Day 21: Week 3 Review & Portfolio

**Goal**: Review, reflect, and document your work

---

## 📝 Self-Assessment Quiz

**Pivot Tables**:
1. What are the 4 areas of a pivot table?
   - Answer: Filters, Rows, Columns, Values

2. How do you group dates by month?
   - Answer: Right-click date → Create pivot date group → Month

3. When would you use COUNT vs SUM in values?
   - Answer: COUNT for number of items, SUM for totals

**Charts**:
4. Which chart shows trends over time?
   - Answer: Line chart

5. Which chart compares categories?
   - Answer: Bar/Column chart

6. When should you use a pie chart?
   - Answer: Show parts of whole, max 5-7 categories

**Conditional Formatting**:
7. Name 3 types of conditional formatting:
   - Answer: Color scales, Data bars, Icon sets

---

## 💭 Reflection

**What was your favorite part of Week 3?**

_______________________________________

**Which visualization technique will you use most?**

_______________________________________

**What dashboard impressed you most (yours or someone else's)?**

_______________________________________

**Rate confidence (1-10)**:
- Pivot tables: ___/10
- Charts: ___/10
- Dashboards: ___/10

---

## 📸 Portfolio Documentation

**Save these**:
1. Your sales dashboard (screenshot)
2. Best chart you created
3. Interesting pivot table insight
4. Before/after chart formatting example

**Write brief case study**:
```
Project: Q1 Sales Dashboard
Tools: Google Sheets, Pivot Tables, Charts
Skills: Data summarization, visualization, dashboard design
Insight: Discovered that Electronics category drives 60% of revenue
```

---

## ✅ Week 3 Completion

Can you:
- [ ] Create pivot table from raw data
- [ ] Group dates by month/quarter
- [ ] Add multiple value fields
- [ ] Choose appropriate chart type
- [ ] Format charts professionally
- [ ] Apply conditional formatting
- [ ] Build complete dashboard
- [ ] Present insights visually

**All checked?** Excellent! Ready for Week 4 (SQL)! 🎉

---

## 🚀 Weeks 1-3 Complete!

**You've mastered**:
- ✅ Excel/Sheets fundamentals
- ✅ Data cleaning and transformation
- ✅ Advanced formulas (IF, VLOOKUP)
- ✅ Pivot tables and summarization
- ✅ Data visualization
- ✅ Dashboard creation

**You're now an intermediate spreadsheet analyst!**

**Next**: Week 4 - SQL (query databases like a pro)

---

**Congratulations on completing the Excel/Sheets phase!** 🎉

**Take a day to celebrate, then dive into SQL!**
