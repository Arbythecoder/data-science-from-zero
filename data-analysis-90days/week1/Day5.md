# 📅 Day 5: Sorting and Filtering Data

**Goal**: Learn to find patterns and insights by sorting and filtering

**Time**: 60 minutes

---

## 🧠 What You'll Learn

1. Why sorting and filtering matter
2. How to sort data (ascending/descending)
3. Multi-level sorting
4. Filtering data by criteria
5. Finding patterns in data

---

## 📖 Part 1: Understanding Sorting

### What is Sorting?

**Sorting** arranges data in a specific order (A-Z, Z-A, smallest-largest, etc.)

**Why Sort?**
- Find highest/lowest values quickly
- Group similar items together
- Identify patterns
- Prepare data for analysis

### Types of Sorting

**Ascending** (↑):
- Numbers: 1, 2, 3, 4, 5 (smallest to largest)
- Text: A, B, C (alphabetical)
- Dates: Oldest to newest

**Descending** (↓):
- Numbers: 5, 4, 3, 2, 1 (largest to smallest)
- Text: Z, Y, X (reverse alphabetical)
- Dates: Newest to oldest

---

## 📊 Part 2: How to Sort in Google Sheets

### Method 1: Single Column Sort

**Steps**:
1. Select data range (including headers)
2. Data → Sort range
3. Check "Data has header row"
4. Choose column to sort by
5. Choose A→Z or Z→A
6. Click Sort

### Method 2: Quick Sort

**Steps**:
1. Click any cell in the column
2. Data → Sort sheet by column X (A→Z)

**⚠️ Warning**: This sorts entire sheet, not just selected range!

---

## 💡 Part 3: Multi-Level Sorting

### What is Multi-Level Sorting?

Sort by multiple columns in order of priority.

**Example**: Employee database
1. First sort by Department
2. Then sort by Salary (within each department)

**Steps**:
1. Select data range
2. Data → Sort range → Advanced range sorting options
3. Add multiple sort conditions
4. Set sort order for each

**Example**:
```
Before:
Name      Dept    Salary
John      IT      50000
Grace     IT      60000
Sarah     HR      55000
David     HR      52000

After (Sort by Dept, then Salary descending):
Name      Dept    Salary
Grace     IT      60000
John      IT      50000
Sarah     HR      55000
David     HR      52000
```

---

## 🔍 Part 4: Filtering Data

### What is Filtering?

**Filtering** shows only rows that meet specific criteria, hiding the rest.

**Why Filter?**
- Focus on specific categories
- Find transactions above/below threshold
- Identify matching records
- Analyze subsets of data

### How to Create Filters

**Steps**:
1. Select your data (including headers)
2. Data → Create a filter
3. Filter icons appear in header row
4. Click icon → Choose criteria

### Filter Types

**1. Text Filters**:
- Contains "word"
- Doesn't contain "word"
- Starts with "A"
- Equals exactly

**2. Number Filters**:
- Greater than 1000
- Less than 500
- Between 100 and 200
- Equals 50

**3. Date Filters**:
- Is after 2025-01-01
- Is before 2025-12-31
- Is in the past week

---

## 🛠️ Part 5: Hands-On Practice

### Practice 1: Sales Analysis

**Data** (create this):
```
Date        Product      Category      Amount    Region
2025-01-01  Laptop       Electronics   50000     Lagos
2025-01-02  Rice         Food          800       Abuja
2025-01-03  Shirt        Clothing      2500      Lagos
2025-01-04  Phone        Electronics   35000     Ibadan
2025-01-05  Bread        Food          500       Lagos
[Add 15 more rows]
```

**Tasks**:
1. Sort by Amount (highest to lowest) - What's the biggest sale?
2. Sort by Category, then Amount - Which category has highest sales?
3. Filter to show only Electronics
4. Filter to show amounts > ₦10,000
5. Filter to show Lagos sales only

### Practice 2: Student Records

**Data**:
```
Name     Class   Test1   Test2   Final   Status
Grace    10A     85      90      78      Pass
John     10B     92      88      95      Pass
Sarah    10A     78      65      72      Pass
David    10B     45      50      48      Fail
[Add 20 more students]
```

**Analysis Questions**:
1. Who scored highest in Final exam? (Sort)
2. How many students failed? (Filter Status = Fail, then count)
3. What's the average for Class 10A? (Filter by class, then AVERAGE)
4. List all students who scored above 80 in Test1 (Filter)

---

## 🎯 Part 6: Finding Patterns

### Pattern Recognition Techniques

**1. Sort by Date**
- See trends over time
- Identify seasonal patterns

**2. Sort by Amount**
- Find top performers
- Identify outliers

**3. Sort by Category**
- Compare group totals
- See distribution

**4. Combine Sort + Filter**
- "Show me Electronics sales over ₦20,000"
- "Who are top 10 customers in Lagos?"

---

## 🏆 Today's Project

### Project: E-commerce Sales Analysis

**Create a dataset**:
- 50 transactions
- Columns: Date, Product, Category, Price, Quantity, Customer, City
- At least 5 different cities
- At least 3 product categories

**Analysis Tasks**:
1. Find the highest single transaction
2. List all transactions above ₦5,000
3. Show only Lagos customers
4. Sort by date to see recent sales
5. Group by category and analyze

**Insights to Find**:
- Which city buys most?
- Which category sells best?
- What's the average transaction value?
- Are there any unusually high/low sales?

---

## ✅ Key Takeaways

✅ **Sorting** arranges data in order
✅ **Ascending** = smallest to largest (A→Z)
✅ **Descending** = largest to smallest (Z→A)
✅ **Multi-level sort** = sort by multiple columns
✅ **Filtering** shows only matching rows
✅ **Combine sort + filter** for powerful analysis

---

## 📚 Resources

**Videos**:
- [Google Sheets Filter & Sort Tutorial](https://www.youtube.com/watch?v=MtVG7lJ8oqU)

**Practice**:
- Use your own data (expenses, grades, etc.)
- Try filtering your email by sender/date
- Sort your photo library by date

---

## ✅ Self-Check

Can you:
- [ ] Sort data ascending and descending
- [ ] Sort by multiple columns
- [ ] Create and apply filters
- [ ] Filter by text, numbers, and dates
- [ ] Combine sorting and filtering
- [ ] Find patterns in sorted data

**All checked? Ready for Day 6!** 🎉

---

**Next**: Day 6 - Mini-Project: Personal Expense Tracker (applying everything you've learned!)
