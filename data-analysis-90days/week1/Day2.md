# 📅 Day 2: Spreadsheet Basics - Your Data Workspace

**Goal**: Learn how spreadsheets work and create your first organized dataset

**Time**: 60 minutes (20 min learn, 30 min practice, 10 min reflect)

**Tools Needed**: Google Sheets or Excel

---

## 🧠 What You'll Learn Today

1. What is a spreadsheet and why use it?
2. Understanding rows, columns, and cells
3. Navigating a spreadsheet
4. Formatting data properly
5. Creating your first data table

---

## 📖 Part 1: What is a Spreadsheet?

### Definition

A **spreadsheet** is a digital grid where you organize, calculate, and analyze data.

Think of it like:
- A **notebook** with infinite pages
- A **calculator** that remembers your work
- A **filing cabinet** that's searchable

### Why Use Spreadsheets for Data?

✅ **Organize** - Keep data structured in rows and columns
✅ **Calculate** - Automatic formulas (no manual calculator needed!)
✅ **Visualize** - Create charts and graphs
✅ **Share** - Collaborate with others
✅ **Sort/Filter** - Find information quickly

### Popular Spreadsheet Tools

| Tool | Best For | Cost |
|------|----------|------|
| **Google Sheets** | Beginners, collaboration, cloud access | Free |
| **Microsoft Excel** | Advanced features, offline work | Paid (free online version) |
| **LibreOffice Calc** | Offline, open-source | Free |

**We'll use Google Sheets** because it's free, accessible, and perfect for learning.

---

## 📊 Part 2: Spreadsheet Anatomy

### The Grid System

A spreadsheet is made of:
1. **Columns** (vertical) - labeled with LETTERS (A, B, C...)
2. **Rows** (horizontal) - labeled with NUMBERS (1, 2, 3...)
3. **Cells** (intersections) - named by column + row (A1, B3, C5...)

```
     A        B        C        D
1  [A1]     [B1]     [C1]     [D1]
2  [A2]     [B2]     [C2]     [D2]
3  [A3]     [B3]     [C3]     [D3]
```

### Cell Reference

**Cell Reference** = The address of a cell

Examples:
- **A1** = First column, first row (top-left corner)
- **B5** = Second column, fifth row
- **Z100** = 26th column, 100th row

**Why This Matters**: Formulas use cell references!
```
=A1 + A2  (adds the values in cell A1 and A2)
```

---

## 🎯 Part 3: Getting Started with Google Sheets

### Step 1: Access Google Sheets

1. Go to [sheets.google.com](https://sheets.google.com)
2. Sign in with Google account
3. Click **+ Blank** to create new spreadsheet

### Step 2: Explore the Interface

```
┌─────────────────────────────────────────────┐
│ File  Edit  View  Insert  Format  Data      │ ← Menu Bar
├─────────────────────────────────────────────┤
│ 📄 Untitled spreadsheet                      │ ← Title (click to rename)
├─────────────────────────────────────────────┤
│ [fx]  =  [Formula Bar]                       │ ← Formula Bar
├─────────────────────────────────────────────┤
│     A    │    B    │    C    │    D    │    │ ← Column Headers
├─────────┼─────────┼─────────┼─────────┼────┤
│  1  │         │         │         │         │ ← Row Numbers
├─────┼─────────┼─────────┼─────────┼─────────┤
│  2  │         │         │         │         │
├─────┼─────────┼─────────┼─────────┼─────────┤
│  3  │         │         │         │         │
└─────────────────────────────────────────────┘
```

### Step 3: Basic Navigation

**Mouse Navigation**:
- Click any cell to select it
- Click column letter to select entire column
- Click row number to select entire row
- Click corner box (top-left) to select all

**Keyboard Navigation** (Faster!):
- **Arrow keys** - Move between cells
- **Tab** - Move right one cell
- **Enter** - Move down one cell
- **Ctrl + Home** - Go to cell A1
- **Ctrl + End** - Go to last used cell

---

## 📝 Part 4: Entering Data

### Rules for Good Data Entry

1. **One type of data per column**
   - ✅ Column A: All names
   - ❌ Column A: Mix of names and ages

2. **First row = Headers** (column labels)
   - Example: Name, Age, City, Salary

3. **No empty rows** between data
   - ✅ Rows 1-10 filled consecutively
   - ❌ Rows 1-5, then empty row, then rows 7-10

4. **Consistent formatting**
   - ✅ All dates in same format (YYYY-MM-DD)
   - ❌ Some DD/MM/YYYY, some MM-DD-YY

### Example: Student Records

**BAD Structure** ❌:
```
A              B           C
Grace 25 Lagos
John 30 Abuja
```

**GOOD Structure** ✅:
```
A        B      C
Name     Age    City
Grace    25     Lagos
John     30     Abuja
Sarah    28     Ibadan
```

**Why?** Column headers make data clear and enable sorting/filtering!

---

## 🎨 Part 5: Formatting Your Data

### Making Data Readable

#### 1. Format Headers (Make Them Stand Out)

**Steps**:
1. Select header row (click "1")
2. Click **Bold** (Ctrl+B)
3. Add **background color** (Fill color icon)
4. Maybe add **borders**

#### 2. Adjust Column Width

**Method 1**: Double-click column divider (auto-fits)
**Method 2**: Drag column divider to desired width

#### 3. Number Formatting

For different data types:

**Currency**:
- Select cells → Format → Number → Currency
- Shows: ₦1,000.00

**Percentage**:
- Select cells → Format → Number → Percent
- Shows: 85%

**Date**:
- Select cells → Format → Number → Date
- Shows: 14/01/2025

#### 4. Text Alignment

- **Left** - For text (names, descriptions)
- **Right** - For numbers
- **Center** - For headers

---

## 🛠️ Part 6: Hands-On Practice

### Practice 1: Create a Simple Dataset

**Task**: Create a table tracking your daily water intake for one week.

**Step-by-Step**:

1. **Open new Google Sheet**
2. **Rename it** "Water Intake Tracker"
3. **Create headers** (Row 1):
   - A1: "Day"
   - B1: "Date"
   - C1: "Glasses of Water"
   - D1: "Goal Met?" (Yes/No)

4. **Add data** (Rows 2-8):
   ```
   Day       Date        Glasses  Goal Met?
   Monday    2025-01-13  6        No
   Tuesday   2025-01-14  8        Yes
   Wednesday 2025-01-15  7        Yes
   Thursday  2025-01-16  5        No
   Friday    2025-01-17  9        Yes
   Saturday  2025-01-18  10       Yes
   Sunday    2025-01-19  8        Yes
   ```

5. **Format it**:
   - Make headers bold
   - Add background color to header row (light blue)
   - Center-align "Glasses of Water" column
   - Add borders around the table

**Screenshot Your Work!** You'll want to track your progress.

---

### Practice 2: Product Inventory

**Task**: Create an inventory for a small shop.

**Required Columns**:
- Product Name
- Category (Electronics, Clothing, Food)
- Quantity in Stock
- Price per Unit
- Supplier

**Add 10 products** (make them up or use real examples)

**Example**:
```
Product Name    Category      Quantity  Price    Supplier
Phone Charger   Electronics   50        ₦1,500   Tech Hub
Rice (1kg)      Food          200       ₦800     Farm Direct
T-Shirt         Clothing      75        ₦2,500   Fashion Co
```

**Extra Challenge**:
- Format prices as currency
- Color-code categories (use conditional formatting later)
- Adjust column widths for readability

---

### Practice 3: Personal Budget Template

**Task**: Set up a monthly expense tracker.

**Structure**:
```
Date  | Category    | Description      | Amount | Payment Method
------+-------------+------------------+--------+---------------
01/14 | Food        | Lunch            | ₦1,200 | Cash
01/14 | Transport   | Uber to work     | ₦800   | Card
01/15 | Shopping    | Groceries        | ₦5,500 | Cash
...
```

**Headers You Need**:
- Date
- Category
- Description
- Amount
- Payment Method

**Add 15 sample transactions**

**Formatting Tips**:
- Format "Amount" as currency
- Make headers bold with colored background
- Freeze the header row (View → Freeze → 1 row)

---

## 💡 Part 7: Best Practices

### Data Entry Tips

1. **Be Consistent**
   - Use same format throughout
   - Don't mix data types in one column

2. **Use Validation** (prevents errors)
   - Data → Data validation
   - Restrict input (e.g., only numbers, only dates)

3. **Document Your Work**
   - Add notes to cells (right-click → Insert note)
   - Create a separate "README" sheet explaining your data

4. **Save Versions**
   - File → Version history
   - Google Sheets auto-saves, but you can name versions

5. **Use Descriptive Names**
   - ❌ "Sheet1", "Data123"
   - ✅ "2025_Sales_Data", "Customer_List"

---

## 🔍 Part 8: Common Mistakes to Avoid

### ❌ Mistake 1: Merging Cells Unnecessarily
**Problem**: Makes sorting/filtering impossible
**Solution**: Use center alignment instead

### ❌ Mistake 2: Multiple Tables on One Sheet
**Problem**: Confusing, hard to analyze
**Solution**: One table per sheet

### ❌ Mistake 3: Using Spaces Instead of Columns
**Problem**: "John    25    Lagos" in one cell
**Solution**: One piece of data per cell

### ❌ Mistake 4: No Headers
**Problem**: Can't remember what each column means
**Solution**: Always use descriptive headers

### ❌ Mistake 5: Inconsistent Data Entry
**Problem**: "Yes", "YES", "yes", "Y" all mean same thing
**Solution**: Pick one format and stick to it

---

## ✍️ Part 9: Today's Assignment

### Assignment: Personal Data Collection

**Choose ONE of these to track for the next 5 days**:

**Option 1: Screen Time Tracker**
- Columns: Date, App Name, Time Spent (minutes), Category
- Track every app you use for 5 days

**Option 2: Meal Logger**
- Columns: Date, Meal Type (Breakfast/Lunch/Dinner), Food Items, Estimated Cost
- Log everything you eat for 5 days

**Option 3: Productivity Tracker**
- Columns: Date, Time Block, Task Completed, Focus Level (1-5), Distractions (count)
- Track your work/study sessions for 5 days

**Option 4: Expense Tracker**
- Columns: Date, Category, Item, Amount, Necessary? (Yes/No)
- Track every purchase for 5 days

**Requirements**:
✅ Properly formatted headers
✅ At least 20 data entries
✅ Consistent formatting
✅ Saved with descriptive name
✅ Ready to analyze on Day 3!

---

## 🎯 Key Takeaways

✅ **Spreadsheets** organize data in rows and columns
✅ **Cells** are identified by column letter + row number (e.g., A1)
✅ **Headers** go in first row - always!
✅ **One data type per column** - keep it consistent
✅ **Formatting** makes data readable and professional
✅ **Good structure** now = easy analysis later

---

## 📚 Additional Resources

**Videos**:
- [Google Sheets Tutorial for Beginners (20 min)](https://www.youtube.com/watch?v=FIkZ1sPmKNw)
- [Excel Basics for Beginners (15 min)](https://www.youtube.com/watch?v=rwbho0CgEAE)

**Interactive Practice**:
- [Google Sheets Training](https://support.google.com/a/users/answer/9300022)

**Cheat Sheet**:
- [Google Sheets Shortcuts](https://support.google.com/docs/answer/181110)

---

## ✅ Self-Check: Ready for Day 3?

Can you:
- [ ] Create a new spreadsheet
- [ ] Name and rename sheets
- [ ] Navigate using keyboard shortcuts
- [ ] Enter data in cells
- [ ] Format headers (bold, color, alignment)
- [ ] Adjust column widths
- [ ] Create a simple data table with at least 5 columns
- [ ] Understand cell references (A1, B2, etc.)

**All checked? Great! Tomorrow you'll learn FORMULAS!** 🎉

---

## 📝 Reflection Questions

1. **What's the difference between a row and a column?**

   _______________________________________

2. **Why should headers always be in the first row?**

   _______________________________________

3. **What does "cell reference" mean?**

   _______________________________________

4. **Name 3 good data entry practices:**

   1. _______________________________________
   2. _______________________________________
   3. _______________________________________

---

## 💭 Daily Journal

**Date**: ___________

**What I created today**:


**What was easier than expected**:


**What I struggled with**:


**Questions for tomorrow**:


---

**🎉 Congratulations! You've created your first organized datasets!**

**Day 1**: You learned what data is
**Day 2**: You learned how to organize it

**Tomorrow (Day 3)**: You'll learn how to CALCULATE with formulas! (SUM, AVERAGE, COUNT, MAX, MIN)

---

**Pro Tip**: The best way to learn spreadsheets is to use them for REAL tasks in your life. Pick something you actually want to track and build it!
