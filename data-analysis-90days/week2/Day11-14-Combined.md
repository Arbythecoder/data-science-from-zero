# Days 11-14: VLOOKUP, Practice & Project

**Note**: These are combined for efficiency. Work through each day separately!

---

# 📅 Day 11: VLOOKUP - Match Data Across Tables

**Goal**: Master VLOOKUP to match and combine data from different sources

---

## 🧠 What is VLOOKUP?

**VLOOKUP** = **V**ertical **LOOKUP**

**What it does**: Searches for a value in the first column of a table and returns a value from another column in the same row.

**Real-World Example**:
- You have Product IDs
- You want to find their Prices
- VLOOKUP matches ID and gets Price

---

## 📖 VLOOKUP Syntax

```
=VLOOKUP(lookup_value, table_range, column_index_number, [range_lookup])
```

**Parameters**:
1. **lookup_value**: What you're searching for (e.g., Product ID)
2. **table_range**: Where to search (e.g., Products table A:D)
3. **column_index_number**: Which column to return (1, 2, 3...)
4. **range_lookup**: FALSE (exact match) or TRUE (approximate)

**99% of the time, use FALSE for exact match!**

---

## 💡 Example: Product Price Lookup

**Table 1 - Orders** (What you have):
```
   A          B
1  Order ID   Product ID
2  ORD001     PROD-01
3  ORD002     PROD-03
```

**Table 2 - Products** (Reference data):
```
   D          E              F
1  Product ID Product Name   Price
2  PROD-01    Laptop         50000
3  PROD-02    Phone          35000
4  PROD-03    Tablet         25000
```

**Goal**: Add Price to Orders table

**Formula in C2**:
```
=VLOOKUP(B2, $D$2:$F$4, 3, FALSE)
```

**Explanation**:
- **B2**: Product ID to find (PROD-01)
- **$D$2:$F$4**: Product table (use $ to lock range)
- **3**: Return column 3 (Price)
- **FALSE**: Exact match only

**Result**: 50000

---

## 🎯 Common VLOOKUP Errors

### Error #1: #N/A

**Meaning**: Value not found

**Causes**:
- Lookup value doesn't exist in table
- Extra spaces (" PROD-01" ≠ "PROD-01")
- Different data types (number vs text)

**Fix**:
```
=IFERROR(VLOOKUP(B2,$D$2:$F$4,3,FALSE), "Not Found")
```

### Error #2: #REF!

**Meaning**: Column index too large

**Cause**: Asking for column 5 but table only has 3 columns

**Fix**: Count columns in table range correctly

### Error #3: Wrong Result

**Cause**: Using TRUE instead of FALSE (approximate match)

**Fix**: Always use FALSE unless you specifically need approximate match

---

## ✍️ Practice: Customer Email Lookup

**Setup**:

**Sheet 1 - Orders**:
```
   A            B
1  Customer ID  Customer Name
2  C001
3  C002
4  C003
```

**Sheet 2 - Customers**:
```
   A            B              C
1  Customer ID  Name           Email
2  C001         John Doe       john@email.com
3  C002         Jane Smith     jane@email.com
4  C003         David Lee      david@email.com
```

**Task**: Fill Name and Email in Orders sheet using VLOOKUP

**Formulas**:
```
B2: =VLOOKUP(A2, Customers!$A$2:$C$4, 2, FALSE)
C2: =VLOOKUP(A2, Customers!$A$2:$C$4, 3, FALSE)
```

---

# 📅 Day 12: Practice Day - Apply All Week 2 Skills

**Goal**: Combine all techniques learned this week

---

## 🎯 Comprehensive Practice Exercise

### Dataset: Messy Employee Records

**Create this data**:
```
   A           B            C              D         E
1  Emp ID      Name         Department     Salary    Email
2  E001        JOHN DOE     sales          45000
3  E002         jane smith  MARKETING      52000     jane@co.com
4  E001        JOHN DOE     sales          45000
5  E003        david   lee  IT             60000
6  E004        Sarah Connor HR             48000     sarah@co.com
7  E002        jane smith   MARKETING      52000     jane@co.com
```

**Issues**:
- Duplicates (rows 3, 7)
- Inconsistent capitalization
- Extra spaces in names
- Missing emails

**Your Tasks**:

1. **Remove Duplicates**
   - Use Data → Remove duplicates

2. **Clean Names** (Column F):
   - Formula: `=PROPER(TRIM(B2))`
   - Copy back to column B

3. **Clean Department** (Column G):
   - Formula: `=PROPER(C2)`
   - Copy back to column C

4. **Fill Missing Emails** (if you have email lookup table):
   - Use VLOOKUP from reference table

5. **Add Salary Grade** (Column F):
   - Salary < 50000: "Grade 1"
   - Salary 50000-60000: "Grade 2"
   - Salary > 60000: "Grade 3"
   - Formula: `=IF(D2<50000, "Grade 1", IF(D2<=60000, "Grade 2", "Grade 3"))`

6. **Create Summary**:
   - Total employees: `=COUNT(A:A)-1`
   - Average salary: `=AVERAGE(D2:D100)`
   - Employees per department: Use COUNTIF

---

# 📅 Day 13: Mini-Project - Customer Database Cleanup

**Goal**: Complete end-to-end data cleaning project

---

## 🏆 The Project

### Scenario

You're a data analyst at an e-commerce company. You received a messy customer database from merging 3 different systems. Your job: Clean it and make it usable.

### Raw Data (Create this)

**customers_messy.csv**:
```
   A        B               C                D             E
1  ID       Name            Email            Phone         City
2  C001     JOHN DOE                         +234 801 2345 lagos
3  C002      jane smith     jane@email.com   0801-234-5678 ABUJA
4  C001     JOHN DOE        john@email.com   08012345      lagos
5  C003     david lee       david@email.com  (0801) 234 5  ibadan
6  C004     Sarah  Connor   sarah@email.com  08012345678   Port Harcourt
7  C002     jane smith      jane@email.com   0801-234-5678 ABUJA
```

### Deliverables

**1. Clean Customer List**:
- Remove duplicates
- Standardized name format (Proper Case)
- Clean phone numbers (format: 08012345678)
- Standardized city names
- Fill missing emails

**2. Customer Reference Table** (separate sheet):
```
ID    | Name         | Email              | Phone        | City
C001  | John Doe     | john@email.com     | 08012345678  | Lagos
C002  | Jane Smith   | jane@email.com     | 08012345678  | Abuja
C003  | David Lee    | david@email.com    | 08012345678  | Ibadan
C004  | Sarah Connor | sarah@email.com    | 08012345678  | Port Harcourt
```

**3. Purchase History** (Sheet 2):
```
Order ID | Customer ID | Amount | Date
ORD001   | C001        | 50000  | 2024-01-15
ORD002   | C002        | 35000  | 2024-01-16
ORD003   | C001        | 25000  | 2024-01-17
```

**4. Enhanced Orders** (use VLOOKUP):
```
Order ID | Customer ID | Customer Name | Amount | Customer Email
ORD001   | C001        | John Doe      | 50000  | john@email.com
```

### Step-by-Step

**Step 1: Clean Names**
```
Column F: =PROPER(TRIM(B2))
```

**Step 2: Clean Phone Numbers**
```
Column G:
=SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(D2,"+234","0"),"-","")," ",""),"(","")
(or do Find & Replace multiple times)
```

**Step 3: Clean Cities**
```
Column H: =PROPER(TRIM(E2))
```

**Step 4: Remove Duplicates**
- Select all data
- Data → Remove duplicates
- Check ID column

**Step 5: VLOOKUP Customer Names**
```
In Purchase History sheet:
=VLOOKUP(B2, Customers!$A$2:$C$100, 2, FALSE)
```

**Step 6: Add Customer Tier** (based on total purchases):
```
Total < 50000: Bronze
Total 50000-100000: Silver
Total > 100000: Gold

Use SUMIF to calculate total purchases per customer
Then IF statement for tier
```

---

# 📅 Day 14: Week 2 Review & Reflection

---

## 📝 Self-Assessment Quiz

### Part A: Formulas (write from memory)

1. Clean extra spaces from text in A2:
   - Answer: `=TRIM(A2)`

2. Make text in A2 Proper Case:
   - Answer: `=PROPER(A2)`

3. Join first name (A2) and last name (B2) with space:
   - Answer: `=A2 & " " & B2`

4. Check if sales (A2) > 100 AND region (B2) = "Lagos":
   - Answer: `=AND(A2>100, B2="Lagos")`

5. Assign grade: A if >= 90, B if >= 80, else C:
   - Answer: `=IF(A2>=90, "A", IF(A2>=80, "B", "C"))`

6. Look up price for product ID in A2 from table B:E, column 3:
   - Answer: `=VLOOKUP(A2, $B$2:$E$100, 3, FALSE)`

### Part B: Scenarios

**Scenario 1**: You have duplicate customer records. What do you do?
- Answer: Data → Remove duplicates

**Scenario 2**: Names are in various cases (JOHN, john, John). How to fix?
- Answer: Use `=PROPER(A2)` in helper column, copy values back

**Scenario 3**: VLOOKUP returns #N/A. What are possible causes?
- Answer:
  - Value doesn't exist in lookup table
  - Extra spaces
  - Wrong data type
  - Table range incorrect

**Scenario 4**: How do you create a formula that shows "VIP" if purchase > 100000 OR customer type = "Premium"?
- Answer: `=IF(OR(A2>100000, B2="Premium"), "VIP", "Regular")`

---

## 💭 Reflection Questions

1. **Which Week 2 skill will you use most often?**

   _______________________________________

2. **What was hardest to understand?**

   _______________________________________

3. **What real-world problem can you now solve?**

   _______________________________________

4. **Rate your confidence (1-10)**:
   - Data cleaning: ___/10
   - Text functions: ___/10
   - IF statements: ___/10
   - VLOOKUP: ___/10

---

## ✅ Week 2 Completion Checklist

Can you:
- [ ] Remove duplicate rows
- [ ] Clean text with TRIM and PROPER
- [ ] Extract portions of text (LEFT, RIGHT, MID)
- [ ] Write IF statements
- [ ] Combine conditions with AND/OR
- [ ] Create nested IF logic
- [ ] Use VLOOKUP to match data
- [ ] Handle VLOOKUP errors
- [ ] Build complete data cleaning workflow

**8+ checked**: Ready for Week 3! 🎉
**6-7 checked**: Review challenging topics
**< 6 checked**: Revisit this week before moving on

---

## 🚀 Week 3 Preview

**Next Week**: Pivot Tables, Charts & Dashboards

**You'll learn**:
- Create pivot tables to summarize data instantly
- Choose and create effective charts
- Use conditional formatting
- Build professional dashboards
- Tell data stories visually

**Why it's exciting**:
- Fastest way to analyze large datasets
- Impressive visualizations
- Professional reporting skills
- Portfolio-worthy dashboards

---

**Congratulations on completing Week 2!** 🎉

**You've learned the skills that separate beginners from intermediate analysts!**

**Rest today, start Week 3 tomorrow!**
