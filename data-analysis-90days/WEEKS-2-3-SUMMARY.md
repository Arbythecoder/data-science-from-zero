# 📚 Weeks 2-3 Complete Content Summary

**This document provides the complete roadmap for Weeks 2-3**
**Detailed day-by-day files are being created for you**

---

## WEEK 2: Data Cleaning & Advanced Functions

### ✅ Day 8: Data Cleaning Basics (COMPLETED)
- Remove duplicates
- Handle blank cells
- Fix inconsistent formatting (TRIM, PROPER, UPPER, LOWER)
- Find & Replace techniques
- Project: Clean messy product database

### Day 10: Logical Functions - IF, AND, OR

**Key Concepts**:
- IF statements for conditional logic
- Combining conditions with AND/OR
- Nested IF statements
- Common patterns and use cases

**Formulas to Learn**:
```
=IF(condition, value_if_true, value_if_false)
=IF(A2>100, "High", "Low")
=IF(AND(A2>50, B2<100), "Valid", "Invalid")
=IF(OR(A2="Yes", B2="Yes"), "Approved", "Denied")
=IF(A2>90, "A", IF(A2>80, "B", IF(A2>70, "C", "F")))
```

**Practice**:
- Grade calculator
- Sales commission tiers
- Inventory status flags
- Customer segmentation

---

### Day 11: VLOOKUP - Match Data Across Tables

**Key Concepts**:
- What VLOOKUP does (vertical lookup)
- Syntax and parameters
- Exact vs approximate match
- Common errors and fixes
- When to use VLOOKUP

**Formula**:
```
=VLOOKUP(lookup_value, table_range, column_index, [range_lookup])

Example:
=VLOOKUP(A2, Products!A:D, 3, FALSE)
```

**Parameters Explained**:
- **lookup_value**: What you're searching for
- **table_range**: Where to search
- **column_index**: Which column to return (1, 2, 3...)
- **range_lookup**: FALSE (exact match) or TRUE (approximate)

**Common Errors**:
- #N/A - Value not found
- #REF! - Column index too large
- Wrong results - Using TRUE instead of FALSE

**Practice**:
- Match product names to prices
- Look up customer information
- Combine data from multiple sheets
- Enrich data with reference tables

---

### Day 12: Practice Day

**Apply All Week 2 Skills**:

**Dataset**: Messy customer orders
- Duplicates
- Inconsistent names
- Missing emails
- Various phone formats
- Need price lookup from product table

**Tasks**:
1. Remove duplicate orders
2. Clean customer names (TRIM, PROPER)
3. Fill missing emails using VLOOKUP
4. Standardize phone numbers (text functions)
5. Add status flags using IF
6. Calculate totals
7. Create summary report

---

### Day 13: Mini-Project - Customer Database Cleanup

**Complete End-to-End Project**:

**Scenario**: E-commerce company with messy customer database from 3 different sources merged together.

**Issues**:
- 500 customer records
- Duplicate entries (same customer, different formatting)
- Names in various cases (UPPERCASE, lowercase, Proper)
- Emails missing for some customers
- Phone numbers in 5 different formats
- Purchase history needs matching via VLOOKUP
- Customer tier needs calculation via IF

**Deliverables**:
1. Clean customer list (no duplicates)
2. Standardized formatting
3. Complete contact information
4. Customer tier assignment (Gold/Silver/Bronze based on purchases)
5. Purchase totals via VLOOKUP
6. Data validation on all fields
7. Professional formatting

**Skills Used**:
- Remove duplicates
- TRIM, PROPER, LOWER
- CONCATENATE
- VLOOKUP
- IF, AND, OR
- Data validation

---

### Day 14: Week 2 Review & Quiz

**Self-Assessment Quiz**:
- Text function scenarios
- Write IF statements
- Fix VLOOKUP errors
- Data cleaning strategies

**Reflection**:
- What was hardest?
- Which functions will you use most?
- Real-world applications

**Prepare for Week 3**: Pivot Tables & Visualization!

---

## WEEK 3: Pivot Tables, Charts & Dashboards

### Day 15: Introduction to Pivot Tables

**What You'll Learn**:
- What pivot tables are and why they're powerful
- Create your first pivot table
- Rows, columns, values, filters
- Summarizing large datasets instantly

**Key Concepts**:
- Pivot tables = Interactive summary tables
- Automatically group and calculate
- No formulas needed!
- Change view instantly

**How to Create**:
1. Select your data (with headers)
2. Insert → Pivot Table
3. Choose where to create it
4. Drag fields to Rows, Columns, Values, Filters

**Practice**:
- Sales data by region
- Product sales by category
- Monthly revenue summary
- Customer purchase patterns

---

### Day 16: Advanced Pivot Table Techniques

**What You'll Learn**:
- Multiple value fields
- Calculated fields
- Grouping dates (by month, quarter, year)
- Sorting and filtering pivot data
- Pivot table formatting

**Advanced Features**:
```
Grouping:
- Group dates by month/quarter/year
- Group numbers into ranges
- Create custom groups

Calculated Fields:
- Profit = Revenue - Cost
- Profit Margin = Profit / Revenue
- Average per transaction

Multiple Summaries:
- SUM of sales
- COUNT of transactions
- AVERAGE order value
- All in one pivot table!
```

**Practice**:
- Time-based analysis (monthly trends)
- Product profitability
- Regional comparison
- Customer lifetime value

---

### Day 17: Chart Types & When to Use Them

**What You'll Learn**:
- Choosing the right chart type
- Creating effective visualizations
- Chart formatting and best practices
- Telling stories with data

**Chart Types**:

**Line Chart**:
- **When**: Show trends over time
- **Example**: Monthly sales, temperature changes
- **Best for**: Time series data

**Bar/Column Chart**:
- **When**: Compare categories
- **Example**: Sales by product, scores by student
- **Best for**: Comparing values

**Pie Chart**:
- **When**: Show parts of a whole
- **Example**: Market share, budget breakdown
- **Best for**: Percentages (max 5-7 slices)

**Scatter Plot**:
- **When**: Show relationship between two variables
- **Example**: Price vs. sales, height vs. weight
- **Best for**: Correlation analysis

**Combo Chart**:
- **When**: Two different metrics
- **Example**: Sales (bars) and profit margin (line)
- **Best for**: Related but different scales

**Best Practices**:
- Clear title
- Label axes
- Remove clutter
- Use color purposefully
- Make it self-explanatory

---

### Day 18: Creating Professional Charts

**What You'll Learn**:
- Step-by-step chart creation
- Customizing charts
- Chart formatting
- Adding trendlines
- Multi-series charts

**Practice Projects**:
1. Monthly sales trend line
2. Product comparison bar chart
3. Market share pie chart
4. Sales vs. profit scatter plot
5. Regional dashboard with multiple charts

**Formatting Checklist**:
- [ ] Descriptive title
- [ ] Axis labels
- [ ] Legend (if needed)
- [ ] Data labels (if helpful)
- [ ] Consistent colors
- [ ] Clean, uncluttered design

---

### Day 19: Conditional Formatting

**What You'll Learn**:
- Highlighting cells based on values
- Color scales
- Data bars
- Icon sets
- Custom rules

**Use Cases**:

**Color Scales**:
```
Sales: Low (red) → High (green)
Automatically shades cells based on value
```

**Data Bars**:
```
Visual bars inside cells showing relative size
Great for quick comparisons
```

**Icon Sets**:
```
↑ Green arrow: Above target
→ Yellow: At target
↓ Red arrow: Below target
```

**Custom Rules**:
```
=IF(A2>1000, TRUE, FALSE)
Highlight if sales > 1000

=IF(B2<C2, TRUE, FALSE)
Highlight if actual < budget
```

**Practice**:
- Sales performance dashboard
- Inventory status (low/medium/high)
- Student grade ranges
- Budget vs. actual comparison

---

### Day 20: Mini-Project - Sales Dashboard

**Complete Dashboard Project**:

**Scenario**: Create an executive sales dashboard for Q1 2024.

**Data**: 500 sales transactions
- Date
- Product
- Category
- Region
- Sales Rep
- Amount
- Quantity

**Dashboard Components**:

1. **KPIs (Top of Dashboard)**:
   - Total Sales (SUM)
   - Average Transaction (AVERAGE)
   - Number of Transactions (COUNT)
   - Top Product (MAX)

2. **Pivot Tables**:
   - Sales by Month
   - Sales by Category
   - Sales by Region
   - Top 10 Products

3. **Charts**:
   - Line chart: Monthly trend
   - Bar chart: Sales by category
   - Pie chart: Regional distribution
   - Combo chart: Sales & quantity

4. **Conditional Formatting**:
   - Highlight top performers (green)
   - Highlight underperformers (red)
   - Data bars for visual comparison

5. **Interactivity**:
   - Filters for date range
   - Slicers for category/region
   - Drill-down capability

**Skills Applied**:
- Pivot tables
- Charts (4 types)
- Conditional formatting
- Formulas (SUM, AVERAGE, MAX)
- Professional formatting
- Layout and design

**Deliverable**: One-page dashboard that tells the complete Q1 sales story.

---

### Day 21: Week 3 Review & Portfolio

**Review Topics**:
- Pivot table creation
- Chart selection
- Dashboard design principles
- Data storytelling

**Portfolio Task**:
- Screenshot your best dashboards
- Write brief descriptions
- Explain insights found
- Document skills used

**Self-Assessment**:
- Can you create pivot tables confidently?
- Can you choose appropriate charts?
- Can you build a dashboard from scratch?
- Can you explain insights to stakeholders?

**Prepare for Week 4**: SQL begins!

---

## 🎯 Key Formulas - Weeks 2-3 Reference

### Text Functions
```
=CONCATENATE(A1, " ", B1)    Join text
=A1 & " " & B1               Join text (simpler)
=LEFT(A1, 5)                 First 5 characters
=RIGHT(A1, 3)                Last 3 characters
=MID(A1, 2, 4)               4 chars from position 2
=LEN(A1)                     Character count
=TRIM(A1)                    Remove extra spaces
=UPPER(A1)                   UPPERCASE
=LOWER(A1)                   lowercase
=PROPER(A1)                  Proper Case
=SPLIT(A1, ",")              Split by comma
```

### Logical Functions
```
=IF(A1>100, "High", "Low")
=IF(AND(A1>50, B1<100), "Valid", "Invalid")
=IF(OR(A1="Yes", B1="Yes"), "Approved", "Denied")
=IF(A1>90, "A", IF(A1>80, "B", "C"))  [Nested IF]
```

### Lookup Function
```
=VLOOKUP(A1, Table!A:D, 3, FALSE)
  - A1: value to find
  - Table!A:D: where to look
  - 3: column to return
  - FALSE: exact match
```

### Data Cleaning
```
Data → Remove duplicates
Data → Create filter
Format → Conditional formatting
Edit → Find and replace (Ctrl+H)
```

---

## 📊 Skills Progression

**After Week 2, you can**:
✅ Clean any messy dataset
✅ Use text functions to transform data
✅ Create conditional logic with IF
✅ Match data across tables with VLOOKUP
✅ Build professional clean datasets

**After Week 3, you can**:
✅ Create pivot tables from any dataset
✅ Choose and create appropriate charts
✅ Use conditional formatting effectively
✅ Build complete dashboards
✅ Tell data stories visually
✅ Present insights professionally

---

## 🎉 Weeks 2-3 Projects

**You'll build**:
1. Product database cleanup (Day 8)
2. Customer data standardization (Day 9)
3. Customer database with VLOOKUP (Day 13)
4. Sales analysis dashboard (Day 20)

**Portfolio-ready work!**

---

## 📅 Next Steps

**Week 4**: SQL Basics - Querying databases
**Week 5**: SQL Advanced - Joins and aggregations
**Week 6**: Python for Data - Environment setup
**Week 7**: Pandas - DataFrames

**You're building systematic data skills!**

---

**All detailed lesson files are being created for you.**
**Work at your own pace - content is ready when you are!**
