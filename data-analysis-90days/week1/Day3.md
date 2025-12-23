# 📅 Day 3: Basic Formulas - Making Spreadsheets Calculate for You

**Goal**: Master basic formulas to automatically calculate totals, averages, and statistics

**Time**: 60 minutes (20 min learn, 30 min practice, 10 min reflect)

**Tools Needed**: Google Sheets or Excel

---

## 🧠 What You'll Learn Today

1. What formulas are and why they're powerful
2. How to write formulas (syntax)
3. Basic formulas: SUM, AVERAGE, COUNT, MIN, MAX
4. Cell references in formulas
5. Copying formulas across cells

---

## 📖 Part 1: Understanding Formulas

### What is a Formula?

A **formula** is an instruction that tells the spreadsheet to perform a calculation.

**Think of it like a recipe**:
- Recipe says: "Add 2 cups flour + 1 cup sugar"
- Formula says: "=A1 + B1" (add cell A1 and B1)

### Why Use Formulas?

**Without Formulas** ❌:
- You calculate manually (5 + 10 + 15 = 30)
- If data changes, recalculate manually
- Slow, error-prone

**With Formulas** ✅:
- Computer calculates instantly
- If data changes, formula updates automatically
- Fast, accurate, efficient

### Real-World Example

**Manual Calculation**:
```
Sales: 500, 750, 320, 890, 450
Total = 500+750+320+890+450 = 2,910 (you type this)
```
If 500 changes to 600, you must recalculate everything!

**Formula**:
```
=SUM(A1:A5)  (computer calculates automatically)
```
If any number changes, total updates instantly!

---

## 🎯 Part 2: Formula Syntax (How to Write Them)

### The Basic Rule

**Every formula starts with =**

```
=  [tells the spreadsheet: "this is a formula"]
```

### Formula Components

```
=FUNCTION_NAME(ARGUMENTS)
```

Example breakdown:
```
=SUM(A1:A5)
│ │   │
│ │   └─── Arguments (what to calculate)
│ └─────── Function name
└───────── Equals sign (required!)
```

### Common Mistakes

❌ **Missing equals sign**
```
SUM(A1:A5)  ← Won't work! Shows as text
```

✅ **Correct**
```
=SUM(A1:A5)  ← Works! Calculates sum
```

---

## 📊 Part 3: Essential Formulas

### 1️⃣ SUM - Add Numbers Together

**Purpose**: Calculate total of multiple numbers

**Syntax**:
```
=SUM(range)
=SUM(cell1, cell2, cell3, ...)
```

**Example 1: Sum a range**
```
   A
1  10
2  20
3  30
4  =SUM(A1:A3)  → Result: 60
```

**Example 2: Sum individual cells**
```
=SUM(A1, A3, A5)  → Adds only cells A1, A3, and A5
```

**Example 3: Sum multiple ranges**
```
=SUM(A1:A5, C1:C5)  → Adds all values from both ranges
```

**Real-World Use**:
- Total sales for the month
- Total expenses
- Sum of test scores

---

### 2️⃣ AVERAGE - Find the Mean

**Purpose**: Calculate the average (mean) of numbers

**Syntax**:
```
=AVERAGE(range)
```

**Example**:
```
   A          B
1  Score
2  85
3  90
4  78
5  92
6  =AVERAGE(A2:A5)  → Result: 86.25
```

**How It Works**:
1. Adds all numbers: 85+90+78+92 = 345
2. Divides by count: 345 ÷ 4 = 86.25

**Real-World Use**:
- Average daily sales
- Average test score
- Average temperature

---

### 3️⃣ COUNT - Count How Many Numbers

**Purpose**: Count cells that contain numbers

**Syntax**:
```
=COUNT(range)
```

**Important**: COUNT only counts cells with numbers, not text!

**Example**:
```
   A
1  10
2  20
3  (empty)
4  30
5  =COUNT(A1:A4)  → Result: 3 (ignores empty cell)
```

**Related Functions**:
- `=COUNTA(range)` - Counts non-empty cells (numbers + text)
- `=COUNTBLANK(range)` - Counts empty cells

**Real-World Use**:
- How many sales transactions?
- How many students took the test?
- How many days did I work out?

---

### 4️⃣ MIN - Find Smallest Number

**Purpose**: Find the minimum (lowest) value

**Syntax**:
```
=MIN(range)
```

**Example**:
```
   A          B
1  Price
2  1500
3  2300
4  890
5  1200
6  =MIN(A2:A5)  → Result: 890
```

**Real-World Use**:
- Lowest price
- Minimum temperature
- Best time (in racing)

---

### 5️⃣ MAX - Find Largest Number

**Purpose**: Find the maximum (highest) value

**Syntax**:
```
=MAX(range)
```

**Example**:
```
   A
1  Sales
2  5000
3  7500
4  3200
5  8900
6  =MAX(A2:A5)  → Result: 8900
```

**Real-World Use**:
- Highest sale
- Maximum temperature
- Top score

---

## 🛠️ Part 4: Understanding Cell Ranges

### What is a Range?

A **range** is a group of cells.

**Notation**: `StartCell:EndCell`

**Examples**:
```
A1:A5    → Cells A1, A2, A3, A4, A5 (5 cells)
B2:B10   → Cells B2 through B10 (9 cells)
A1:C1    → Cells A1, B1, C1 (3 cells)
A1:C3    → Rectangle from A1 to C3 (9 cells)
```

**Visual**:
```
     A    B    C
1  [A1] [B1] [C1]
2  [A2] [B2] [C2]    A1:C3 includes all 9 shaded cells
3  [A3] [B3] [C3]
```

### Selecting Ranges

**Mouse Method**:
1. Click first cell (A1)
2. Hold Shift
3. Click last cell (A5)
4. Result: A1:A5 selected

**Keyboard Method**:
1. Click A1
2. Hold Shift + Arrow Down (4 times)
3. Result: A1:A5 selected

---

## 💡 Part 5: Hands-On Practice

### Practice 1: Sales Analysis

**Setup**: Create this data in Google Sheets

```
   A              B
1  Day            Sales
2  Monday         5000
3  Tuesday        7500
4  Wednesday      3200
5  Thursday       8900
6  Friday         6400
7
8  Total Sales    =SUM(B2:B6)
9  Average Sales  =AVERAGE(B2:B6)
10 Best Day       =MAX(B2:B6)
11 Worst Day      =MIN(B2:B6)
12 Days Tracked   =COUNT(B2:B6)
```

**Expected Results**:
- Total Sales: 31,000
- Average Sales: 6,200
- Best Day: 8,900
- Worst Day: 3,200
- Days Tracked: 5

**Challenge**: Add Saturday and Sunday sales. Notice formulas update automatically!

---

### Practice 2: Student Grades

**Setup**: Create a grade tracker

```
   A          B      C      D      E      F
1  Student    Test1  Test2  Test3  Average  Status
2  Grace      85     90     78     =AVERAGE(B2:D2)
3  John       92     88     95     =AVERAGE(B3:D3)
4  Sarah      78     82     80     =AVERAGE(B4:D4)
5  David      90     85     92     =AVERAGE(B5:D5)
6
7  Highest    =MAX(B2:D5)
8  Lowest     =MIN(B2:D5)
9  Class Avg  =AVERAGE(B2:D5)
```

**Tasks**:
1. Fill in the average formulas (column E)
2. Calculate highest, lowest, and class average
3. Verify your results manually for one row

---

### Practice 3: Monthly Budget

**Setup**: Track your expenses

```
   A              B
1  Category       Amount
2  Rent           50000
3  Food           15000
4  Transport      8000
5  Utilities      12000
6  Entertainment  5000
7  Shopping       20000
8  Savings        25000
9
10 Total Expenses =SUM(B2:B9)
11 Average/Category =AVERAGE(B2:B9)
12 Highest Expense =MAX(B2:B9)
13 Lowest Expense  =MIN(B2:B9)
```

**Additional Challenge**:
Add a third column calculating percentage of total for each category:
```
   C
1  % of Total
2  =B2/B$10*100
```
(We'll learn about $ symbols later - they "lock" cell references)

---

## 🔍 Part 6: Formula Tips & Tricks

### Tip 1: Copy Formulas

**Drag to Copy**:
1. Write formula in first cell
2. Click cell corner (small square)
3. Drag down
4. Formula adjusts automatically!

**Example**:
```
A1: =B1*2
[Drag down]
A2: =B2*2  (automatically adjusted!)
A3: =B3*2
```

### Tip 2: Edit Formulas

**Double-click cell** to edit formula
- Cells referenced will highlight in colors
- Easy to see what you're calculating

### Tip 3: See Formula Result

**Formula bar** shows formula
**Cell** shows result

### Tip 4: Formula Errors

Common errors:

**#DIV/0!** - Division by zero
```
=A1/B1  where B1 is 0 or empty
```

**#NAME?** - Function name misspelled
```
=SOM(A1:A5)  ← should be SUM
```

**#REF!** - Reference to deleted cell
```
=A1+A2  after deleting column A
```

**#VALUE!** - Wrong data type
```
=SUM(A1:A5)  where cells contain text instead of numbers
```

---

## ✍️ Part 7: Today's Project

### Project: Personal Finance Dashboard

**Goal**: Create a complete expense analysis for one week

**Step 1: Data Entry**
Create this structure:
```
   A         B          C          D
1  Date      Category   Description Amount
2  01/14     Food       Lunch       1200
3  01/14     Transport  Uber        800
4  01/15     Shopping   Groceries   5500
5  [Add 12 more rows of sample data]
```

**Step 2: Add Analysis Section**
Below your data, add:
```
18  ANALYSIS
19  Total Spent       =SUM(D2:D17)
20  Average/Day       =AVERAGE(D2:D17)
21  Largest Expense   =MAX(D2:D17)
22  Smallest Expense  =MIN(D2:D17)
23  Number of Transactions  =COUNT(D2:D17)
```

**Step 3: Category Totals**
Create a breakdown:
```
25  CATEGORY BREAKDOWN
26  Food Total        =SUMIF(B:B,"Food",D:D)
27  Transport Total   =SUMIF(B:B,"Transport",D:D)
28  Shopping Total    =SUMIF(B:B,"Shopping",D:D)
```
(SUMIF is advanced - try it as bonus!)

**Step 4: Format**
- Bold headers
- Format amounts as currency (₦)
- Add borders
- Color-code sections

---

## 🎯 Key Takeaways

✅ **All formulas start with =**
✅ **SUM** adds numbers together
✅ **AVERAGE** finds the mean
✅ **COUNT** counts how many numbers
✅ **MIN** finds smallest value
✅ **MAX** finds largest value
✅ **Ranges** are written as StartCell:EndCell (e.g., A1:A10)
✅ **Formulas update automatically** when data changes

---

## 📚 Additional Resources

**Videos**:
- [Google Sheets Formulas for Beginners (15 min)](https://www.youtube.com/watch?v=8I5kRNL3B5A)
- [Excel Basic Formulas (10 min)](https://www.youtube.com/watch?v=YCjsYaJSNvA)

**Cheat Sheet**:
```
=SUM(A1:A10)      Add all numbers in range
=AVERAGE(A1:A10)  Calculate mean
=COUNT(A1:A10)    Count numbers
=MIN(A1:A10)      Find smallest
=MAX(A1:A10)      Find largest
=MEDIAN(A1:A10)   Find middle value
```

---

## ✅ Self-Check

Before moving to Day 4, can you:
- [ ] Write a SUM formula from memory
- [ ] Calculate an average using AVERAGE
- [ ] Find the highest value using MAX
- [ ] Count numbers using COUNT
- [ ] Explain what a cell range is (e.g., A1:A10)
- [ ] Copy a formula down multiple cells
- [ ] Identify and fix basic formula errors

**All checked? You're ready for Day 4!** 🎉

---

## 📝 Practice Challenge

**Quick Quiz** (try without looking!):

1. What formula adds numbers from A1 to A10?
   - Answer: `=SUM(A1:A10)`

2. What formula finds the average of B1 to B5?
   - Answer: `=AVERAGE(B1:B5)`

3. What's wrong with this formula? `SUM(A1:A5)`
   - Answer: Missing = sign at the start

4. What does COUNT(A1:A10) do?
   - Answer: Counts how many cells contain numbers

5. How do you find the highest score from C1 to C20?
   - Answer: `=MAX(C1:C20)`

---

## 💭 Daily Journal

**Date**: ___________

**Formulas I mastered today**:


**Coolest thing I calculated**:


**Formula I'm still confused about**:


**How I'll use formulas in real life**:


---

**🎉 Excellent work! You can now make spreadsheets calculate for you!**

**Tomorrow (Day 4)**: You'll learn data organization best practices and how to structure data for analysis!

---

**Pro Tip**: Practice formulas by tracking REAL data from your life. The more you use them, the more natural they'll become!
