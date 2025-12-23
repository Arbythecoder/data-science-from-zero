# 📅 Day 8: Data Cleaning Basics

**Goal**: Learn to identify and fix common data quality issues

**Time**: 60 minutes

**Welcome to Week 2!** This week is about making messy data usable.

---

## 🧠 What You'll Learn Today

1. Why data is messy (and that's normal!)
2. Common data quality issues
3. How to find and remove duplicates
4. Handling blank/missing cells
5. Fixing inconsistent formatting
6. Using Find & Replace effectively

---

## 📖 Part 1: Why Data is Messy

### The Reality of Real Data

**Textbook data** ✨:
- Perfectly formatted
- No errors
- Complete information
- Consistent structure

**Real-world data** 😅:
- Typos and errors
- Duplicate entries
- Missing values
- Inconsistent formats
- Mixed data types
- Extra spaces
- Different cases (JOHN, john, John)

**Important**: **60-80% of data work is cleaning!** This is normal and expected.

---

## 🔍 Part 2: Common Data Quality Issues

### Issue 1: Duplicate Records

**Problem**: Same entry appears multiple times

**Example**:
```
Name          Email
John Doe      john@email.com
Jane Smith    jane@email.com
John Doe      john@email.com    ← Duplicate!
```

**Why it happens**:
- Multiple people entering data
- System errors
- Data merged from different sources
- Copy-paste mistakes

**Impact**:
- Inflated counts
- Wrong statistics
- Skewed analysis
- Misleading insights

---

### Issue 2: Missing/Blank Values

**Problem**: Some cells are empty

**Example**:
```
Name      Age    City
John      25     Lagos
Jane            Abuja     ← Missing age
David     30              ← Missing city
```

**Why it happens**:
- Optional form fields
- Incomplete data collection
- Data loss during transfer
- User skipped fields

**Impact**:
- Can't calculate accurate averages
- Filtering excludes useful records
- Analysis incomplete

---

### Issue 3: Inconsistent Formatting

**Problem**: Same data entered differently

**Example**:
```
Phone Numbers:
08012345678
+234 801 234 5678
0801-234-5678
(0801) 234-5678
```

All the same number, but different formats!

**Example 2 - Names**:
```
JOHN DOE        ← All caps
john doe        ← All lowercase
John Doe        ← Proper case
john    doe     ← Extra spaces
```

**Impact**:
- Can't match records
- Looks unprofessional
- Sorting doesn't work properly
- Filters miss entries

---

### Issue 4: Leading/Trailing Spaces

**Problem**: Hidden spaces before or after text

**Example**:
```
What you see:   "John"
What's actually: " John " (spaces before and after)
```

**Why it's bad**:
- "John" ≠ " John " (computer sees them as different)
- VLOOKUP fails
- Filters don't work
- Sorting is wrong

---

### Issue 5: Wrong Data Types

**Problem**: Numbers stored as text, dates as numbers, etc.

**Example**:
```
Age Column:
25
30
"Unknown"    ← Text in number column!
28
```

**Impact**:
- Can't calculate (SUM, AVERAGE won't work)
- Can't sort properly
- Errors in formulas

---

## 🛠️ Part 3: Removing Duplicates

### Method 1: Built-in Remove Duplicates

**Steps**:
1. Select your data range (including headers)
2. **Data → Remove duplicates** (Google Sheets)
   - Or **Data → Data Tools → Remove duplicates** (Excel)
3. Check "Data has header row"
4. Select which columns to check
5. Click **Remove duplicates**

**Google Sheets will show**: "Found and removed X duplicate rows"

### Method 2: Advanced - Highlight Duplicates First

**Before removing, you might want to review them**:

1. Select data column (e.g., Email)
2. **Format → Conditional formatting**
3. **Format rules**: Custom formula
4. Formula: `=COUNTIF($A$2:$A$100,A2)>1`
5. Choose highlighting color (e.g., red)
6. Now duplicates are highlighted - review before deleting

### Practice: Remove Duplicates

**Create this data**:
```
   A              B
1  Name           Email
2  John Doe       john@email.com
3  Jane Smith     jane@email.com
4  John Doe       john@email.com
5  David Lee      david@email.com
6  Jane Smith     jane@email.com
7  Sarah Connor   sarah@email.com
```

**Task**: Remove duplicate rows

**Expected Result**: 4 rows remain (John, Jane, David, Sarah - one each)

---

## 🧹 Part 4: Handling Blank Cells

### Strategy 1: Delete Rows with Blanks

**When to use**: If missing data makes the row useless

**Steps**:
1. Select data range
2. **Data → Create a filter**
3. Click filter icon on column with blanks
4. Uncheck **(Blanks)**
5. Select visible rows
6. Right-click → Delete rows
7. Remove filter

### Strategy 2: Fill with Default Value

**When to use**: Want to keep rows but need a placeholder

**Example**: Replace blank ages with 0 or "Unknown"

**Steps**:
1. Select column with blanks
2. **Edit → Find and replace** (Ctrl+H)
3. **Find**: Leave empty (or use regex: `^\s*$`)
4. **Replace with**: "Unknown" (or 0, or whatever makes sense)
5. **Search**: Specific range
6. Click **Replace all**

### Strategy 3: Fill Down from Above

**When to use**: Blank means "same as above"

**Example**:
```
Category    Product
Food        Rice
            Beans     ← Should be "Food"
            Bread     ← Should be "Food"
Transport   Uber
            Bus       ← Should be "Transport"
```

**Steps**:
1. Select the range with blanks
2. **Edit → Find and replace**
3. **Find**: `^$` (regex for empty cell)
4. Check **Search using regular expressions**
5. Manually fill OR use formula method

**Formula Method**:
```
=IF(A2="", A1, A2)
```
(If current cell blank, copy from above; otherwise keep current value)

---

## 📝 Part 5: Fixing Inconsistent Text

### Issue: Inconsistent Capitalization

**Problem**:
```
JOHN DOE
john doe
John Doe
jOhN dOe
```

**Solution**: Use `PROPER()` function

**Steps**:
1. Insert new column next to messy data
2. Formula: `=PROPER(A2)`
3. Drag down to apply to all
4. Copy results
5. **Paste Special → Values only** over original column
6. Delete helper column

**Functions**:
- `=UPPER(A2)` → MAKES ALL UPPERCASE
- `=LOWER(A2)` → makes all lowercase
- `=PROPER(A2)` → Makes Proper Case

---

### Issue: Extra Spaces

**Problem**:
```
" John Doe "     ← Spaces before and after
"John  Doe"      ← Double space in middle
```

**Solution**: Use `TRIM()` function

**What TRIM does**:
- Removes all leading spaces
- Removes all trailing spaces
- Reduces multiple spaces to single space

**Steps**:
1. New column: `=TRIM(A2)`
2. Drag down
3. Copy and paste values back
4. Delete helper column

**Example**:
```
Before: " John   Doe "
After:  "John Doe"
```

---

## 🔧 Part 6: Find & Replace Power Moves

### Basic Find & Replace

**Shortcut**: Ctrl+H (Cmd+H on Mac)

**Use Cases**:

**1. Fix Typos**:
- Find: "Laogs"
- Replace: "Lagos"

**2. Standardize Terms**:
- Find: "N/A"
- Replace: "Unknown"

**3. Remove Characters**:
- Find: "$"
- Replace: (leave empty)

### Advanced: Regular Expressions (Regex)

**Enable Regex** in Find & Replace:
- Check ✅ "Search using regular expressions"

**Common Patterns**:

**Remove all numbers**:
- Find: `[0-9]+`
- Replace: (empty)

**Find emails**:
- Find: `\S+@\S+\.\S+`

**Find empty cells**:
- Find: `^$`

---

## 🎯 Part 7: Hands-On Practice

### Exercise 1: Clean This Dataset

**Create this messy data**:
```
   A               B            C
1  Name            Email        City
2  JOHN DOE        john@co.com  lagos
3  jane smith      jane@co.com  ABUJA
4  JOHN DOE        john@co.com  lagos
5   David Lee      david@co.com ibadan
6  jane  smith     jane@co.com  ABUJA
7  Sarah Connor    sarah@co.com Lagos
```

**Your Tasks**:
1. Remove duplicate rows (rows 3 and 6)
2. Fix name capitalization (use PROPER)
3. Fix city capitalization (use PROPER)
4. Remove extra spaces in names (use TRIM)

**Expected Clean Result**:
```
   A               B            C
1  Name            Email        City
2  John Doe        john@co.com  Lagos
3  Jane Smith      jane@co.com  Abuja
4  David Lee       david@co.com Ibadan
5  Sarah Connor    sarah@co.com Lagos
```

---

### Exercise 2: Handle Missing Data

**Data**:
```
   A        B      C
1  Name     Age    City
2  John     25     Lagos
3  Jane            Abuja
4  David    30
5  Sarah    28     Ibadan
```

**Tasks**:
1. Fill blank ages with "Unknown"
2. Fill blank cities with "Not Provided"
3. Count how many complete records you have

---

### Exercise 3: Standardize Phone Numbers

**Data**:
```
08012345678
+234 801 234 5678
0801-234-5678
(0801) 234-5678
```

**Task**: Make all format the same: 08012345678

**Hint**: Use Find & Replace to:
1. Remove "+"
2. Remove "234 "
3. Remove all spaces
4. Remove all dashes "-"
5. Remove all parentheses "(" and ")"

---

## 📊 Part 8: Today's Project

### Project: Clean Product Database

**Scenario**: You received a product list from a supplier. It's messy!

**Create this data** (copy exactly with all the issues!):
```
Product Name       Category        Price     Stock
 Laptop            ELECTRONICS     50000     10
laptop             Electronics     50000     10
Phone              electronics     35000     5
  Rice (1kg)       food            800       200
RICE (1KG)         Food            800       200
T-Shirt            CLOTHING        2500      50
t-shirt            Clothing        2500      50
Charger            ELECTRONICS     1500      30
```

**Cleaning Tasks**:

1. **Remove Duplicates** (rows 2, 5, 7)
2. **Standardize Category**:
   - Use PROPER() to make: Electronics, Food, Clothing

3. **Clean Product Names**:
   - TRIM() to remove extra spaces
   - PROPER() for capitalization

4. **Verify Data Types**:
   - Ensure Price and Stock are numbers (not text)

5. **Add Validation**:
   - Category must be dropdown: Electronics, Food, Clothing

6. **Final Formatting**:
   - Bold headers
   - Price as currency
   - Borders around table

**Clean Result**:
```
Product Name       Category        Price     Stock
Laptop             Electronics     ₦50,000   10
Phone              Electronics     ₦35,000   5
Rice (1kg)         Food            ₦800      200
T-Shirt            Clothing        ₦2,500    50
Charger            Electronics     ₦1,500    30
```

---

## ✅ Data Cleaning Checklist

Before calling data "clean", check:

- [ ] No duplicate rows
- [ ] No blank cells (or handled appropriately)
- [ ] Consistent capitalization
- [ ] No extra spaces (use TRIM)
- [ ] Correct data types (numbers as numbers, dates as dates)
- [ ] Standardized formats (phone, email, etc.)
- [ ] No typos or obvious errors
- [ ] Column headers clear and consistent
- [ ] Data validated where possible

---

## 🎯 Key Takeaways

✅ **Data is messy** - that's normal, not your fault
✅ **Remove duplicates** - use built-in tools
✅ **TRIM()** removes extra spaces
✅ **PROPER()** fixes capitalization
✅ **Find & Replace** is powerful for batch edits
✅ **Handle blanks** thoughtfully (delete, fill, or flag)
✅ **Clean data** = accurate analysis

---

## 📚 Additional Resources

**Videos**:
- [Data Cleaning in Excel](https://www.youtube.com/watch?v=vGOqAj3bM_k)
- [Google Sheets TRIM and PROPER](https://www.youtube.com/watch?v=3_eP7YqJmJE)

**Cheat Sheet**:
```
Remove Duplicates:   Data → Remove duplicates
Find & Replace:      Ctrl+H
TRIM:                =TRIM(A2)
PROPER:              =PROPER(A2)
UPPER:               =UPPER(A2)
LOWER:               =LOWER(A2)
```

---

## ✅ Self-Check

Can you:
- [ ] Identify common data quality issues
- [ ] Remove duplicate rows
- [ ] Handle blank cells appropriately
- [ ] Use TRIM to remove spaces
- [ ] Use PROPER/UPPER/LOWER
- [ ] Use Find & Replace effectively
- [ ] Explain why data cleaning matters

**All checked? Great! Tomorrow you'll learn text functions!** 🎉

---

## 📝 Reflection

**What messy data have you encountered in real life?**

_______________________________________

**Which cleaning technique will you use most?**

_______________________________________

**What surprised you today?**

_______________________________________

---

**Tomorrow (Day 9)**: Text Functions - CONCATENATE, LEFT, RIGHT, MID, SPLIT!

**Pro Tip**: Save a copy of your messy data before cleaning, so you can always compare before/after!
