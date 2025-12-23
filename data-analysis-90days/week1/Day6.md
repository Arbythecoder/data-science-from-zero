# 📅 Day 6: Mini-Project - Personal Expense Tracker

**Goal**: Build a complete expense tracking and analysis system

**Time**: 90 minutes (this is project day!)

---

## 🎯 Project Overview

Today you'll create a **Personal Expense Tracker** that:
- Records all your expenses
- Calculates totals and averages
- Shows category breakdowns
- Identifies spending patterns
- Creates visual summaries

**This project uses EVERYTHING you learned Days 1-5!**

---

## 📋 Project Requirements

### Part 1: Data Collection Sheet

Create a sheet called "Expenses" with these columns:

| Column | Data Type | Purpose |
|--------|-----------|---------|
| Date | Date | When expense occurred |
| Category | Text | Food, Transport, Shopping, Bills, etc. |
| Description | Text | What you bought |
| Amount | Number | How much you spent |
| Payment Method | Text | Cash, Card, Mobile Money |
| Necessary | Yes/No | Was it essential? |

**Validation Rules**:
- Date must be valid date format
- Category dropdown: Food, Transport, Shopping, Bills, Entertainment, Healthcare, Other
- Amount must be number > 0
- Payment Method dropdown: Cash, Card, Mobile Money

---

## 🛠️ Step-by-Step Build Guide

### Step 1: Set Up Spreadsheet (10 min)

1. **Create new Google Sheet**
2. **Rename to**: "My Expense Tracker - Jan 2025"
3. **Create sheet tabs**:
   - Sheet 1: "Transactions"
   - Sheet 2: "Analysis"
   - Sheet 3: "Monthly Summary"

### Step 2: Build Transactions Sheet (15 min)

```
   A          B          C             D       E              F
1  Date       Category   Description   Amount  Payment        Necessary?
2  2025-01-14 Food       Breakfast     500     Cash           Yes
3  2025-01-14 Transport  Uber to work  800     Card           Yes
4  2025-01-15 Shopping   New shirt     2500    Card           No
5  [Add 30 more sample transactions]
```

**Formatting**:
- Bold headers with background color
- Format Date column as Date
- Format Amount as Currency (₦)
- Add borders
- Freeze header row

**Data Validation**:
- Category: Create dropdown list
- Payment: Create dropdown list
- Necessary: Create dropdown (Yes/No)

### Step 3: Add Automatic Calculations (15 min)

**At the bottom of Transactions sheet**:

```
35  ─────────────────────────────────────────
36  QUICK STATS
37  Total Spent          =SUM(D2:D34)
38  Average/Transaction  =AVERAGE(D2:D34)
39  Number of Transactions =COUNT(D2:D34)
40  Highest Expense      =MAX(D2:D34)
41  Lowest Expense       =MIN(D2:D34)
```

---

### Step 4: Build Analysis Sheet (20 min)

Switch to "Analysis" tab.

**Section 1: Category Breakdown**

```
   A                  B               C
1  CATEGORY ANALYSIS
2
3  Category           Total Spent     % of Total
4  Food               =SUMIF(Transactions!B:B,"Food",Transactions!D:D)
5  Transport          =SUMIF(Transactions!B:B,"Transport",Transactions!D:D)
6  Shopping           =SUMIF(Transactions!B:B,"Shopping",Transactions!D:D)
7  Bills              =SUMIF(Transactions!B:B,"Bills",Transactions!D:D)
8  Entertainment      =SUMIF(Transactions!B:B,"Entertainment",Transactions!D:D)
9  Healthcare         =SUMIF(Transactions!B:B,"Healthcare",Transactions!D:D)
10 Other              =SUMIF(Transactions!B:B,"Other",Transactions!D:D)
11
12 TOTAL              =SUM(B4:B10)
```

**For % of Total (Column C)**:
```
C4: =B4/$B$12*100
```
(Then drag down to C10)

**Section 2: Payment Method Analysis**

```
14 PAYMENT METHOD ANALYSIS
15
16 Payment Method     Total          Count
17 Cash               =SUMIF(...)    =COUNTIF(...)
18 Card               =SUMIF(...)    =COUNTIF(...)
19 Mobile Money       =SUMIF(...)    =COUNTIF(...)
```

**Section 3: Essential vs Non-Essential**

```
22 SPENDING TYPE
23
24 Type               Amount         % of Total
25 Necessary (Yes)    =SUMIF(Transactions!F:F,"Yes",Transactions!D:D)
26 Not Necessary (No) =SUMIF(Transactions!F:F,"No",Transactions!D:D)
```

---

### Step 5: Monthly Summary Sheet (15 min)

Create a dashboard view:

```
   A                          B
1  ═══════════════════════════════════════
2       MONTHLY EXPENSE REPORT
3  ═══════════════════════════════════════
4
5  Total Spent This Month:    =Transactions!D37
6  Daily Average:             =Transactions!D38
7  Number of Transactions:    =Transactions!D39
8
9  ───────────────────────────────────────
10 TOP SPENDING CATEGORY
11 [Manually identify or use advanced formulas]
12
13 ───────────────────────────────────────
14 BIGGEST EXPENSE
15 Amount:                    =Transactions!D40
16
17 ───────────────────────────────────────
18 SMALLEST EXPENSE
19 Amount:                    =Transactions!D41
20
21 ───────────────────────────────────────
22 SAVINGS INSIGHTS
23 Total Non-Essential:       =Analysis!B26
24 Potential Savings:         =Analysis!B26
```

---

## 📊 Part 7: Create a Simple Chart

**In Analysis sheet**:

1. Select Category column and Total Spent column
2. Insert → Chart
3. Choose **Pie Chart**
4. Title: "Spending by Category"
5. Customize colors if desired

**Create second chart**:
- Bar chart showing expenses by payment method

---

## ✍️ Part 8: Analysis Questions

Now use your tracker to answer:

**Questions**:
1. What's your total spending for the period?
2. Which category costs you the most?
3. What percentage of spending is non-essential?
4. Do you use cash or card more?
5. What's your most expensive single purchase?
6. What's your average daily spending?
7. How many transactions were under ₦500?
8. If you eliminated all non-essential spending, how much would you save?

**Write insights**:

Create a section in Monthly Summary:
```
26 INSIGHTS
27
28 1. I spend most on: _______________
29 2. I could save ₦_____ by cutting _______________
30 3. My average daily spending is ₦_____
31 4. Surprising finding: _______________
```

---

## 🎯 Bonus Challenges

### Challenge 1: Weekly Breakdown

Add analysis showing spending per week:
```
Week 1 (Jan 1-7):    ₦_____
Week 2 (Jan 8-14):   ₦_____
Week 3 (Jan 15-21):  ₦_____
Week 4 (Jan 22-31):  ₦_____
```

### Challenge 2: Daily Tracking

Create formula that shows today's expenses:
```
=SUMIF(Transactions!A:A,TODAY(),Transactions!D:D)
```

### Challenge 3: Budget Tracker

Add a budget column:
```
Category     Budget    Actual    Difference    Status
Food         15000     12000     +3000         Under
Transport    8000      9500      -1500         Over
```

### Challenge 4: Conditional Formatting

- Highlight expenses > ₦5,000 in red
- Highlight non-essential purchases in yellow
- Highlight categories over budget in red

---

## ✅ Project Checklist

**Setup**:
- [ ] Created spreadsheet with 3 sheets
- [ ] Added proper headers
- [ ] Applied data validation
- [ ] Formatted cells properly

**Data**:
- [ ] Added at least 30 transactions
- [ ] Included all 7 categories
- [ ] Mixed essential and non-essential
- [ ] Used all payment methods

**Formulas**:
- [ ] SUM for totals
- [ ] AVERAGE for means
- [ ] COUNT for transaction count
- [ ] MIN/MAX for extremes
- [ ] SUMIF for category totals

**Analysis**:
- [ ] Category breakdown complete
- [ ] Payment method analysis
- [ ] Essential vs non-essential
- [ ] Charts created
- [ ] Insights written

**Formatting**:
- [ ] Professional appearance
- [ ] Color-coded sections
- [ ] Borders and alignment
- [ ] Currency symbols

---

## 🏆 What You Accomplished

By completing this project, you:
- ✅ Built a real, usable tool
- ✅ Applied all Week 1 concepts
- ✅ Created multi-sheet workbook
- ✅ Used 8+ different formulas
- ✅ Made data-driven insights
- ✅ Created visual charts

**This is a real data analysis project!**

---

## 📸 Share Your Work

Take screenshots of:
1. Your Transactions sheet
2. Your Analysis sheet with charts
3. Your insights section

**Optional**: Share on social media with #90DaysOfData

---

## 💡 Real-World Application

This same structure works for:
- **Business**: Track business expenses
- **Freelance**: Track project income/expenses
- **Student**: Track study hours by subject
- **Fitness**: Track workouts and progress

**The skills are transferable!**

---

## 📝 Reflection Questions

1. **What was the hardest part of this project?**

   _______________________________________

2. **Which formula took you longest to understand?**

   _______________________________________

3. **What insight surprised you about your spending?**

   _______________________________________

4. **How will you use this tracker going forward?**

   _______________________________________

5. **What would you add to make it better?**

   _______________________________________

---

## 🚀 Next Steps

**Week 1 Complete!** 🎉

Tomorrow (Day 7): Review everything, take a quiz, and prepare for Week 2!

**Week 2 Preview**: Data cleaning, advanced formulas (IF, VLOOKUP), text manipulation

---

**Congratulations on building your first complete data analysis project!**

Save this file - you'll want to reference it as you build more complex projects!
