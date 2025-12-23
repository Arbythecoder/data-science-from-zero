# 📅 Day 9: Text Functions - Manipulating Text Data

**Goal**: Master text manipulation functions for data transformation

**Time**: 60 minutes

---

## 🧠 What You'll Learn

1. Combining text (CONCATENATE, &, TEXTJOIN)
2. Extracting text (LEFT, RIGHT, MID)
3. Finding text (FIND, SEARCH, LEN)
4. Splitting text (SPLIT)
5. Real-world text manipulation scenarios

---

## 📖 Part 1: Combining Text

### CONCATENATE - Join Text Together

**Syntax**: `=CONCATENATE(text1, text2, text3, ...)`

**Example**:
```
   A          B          C (Formula)              D (Result)
1  First      Last       =CONCATENATE(A1," ",B1)  First Last
2  John       Doe        =CONCATENATE(A2," ",B2)  John Doe
```

**Why use it**:
- Combine first name + last name
- Build full addresses
- Create custom IDs
- Merge data from multiple cells

### The & Operator (Simpler!)

**Same as CONCATENATE but easier**:
```
=A2 & " " & B2    (joins A2, space, B2)
```

**Example - Create Email**:
```
   A        B           C (Formula)                    D (Result)
1  First    Last        =LOWER(A2&"."&B2&"@co.com")   john.doe@co.com
2  John     Doe
```

### TEXTJOIN (Google Sheets) - Join with Delimiter

**Syntax**: `=TEXTJOIN(delimiter, ignore_empty, text1, text2, ...)`

**Example**:
```
   A      B       C      Formula: =TEXTJOIN(", ", TRUE, A2:C2)
1  City   State   ZIP    Result: Lagos, Nigeria, 100001
2  Lagos  Nigeria 100001
```

**Parameters**:
- **delimiter**: What goes between (comma, space, dash, etc.)
- **ignore_empty**: TRUE = skip blank cells
- **text range**: Cells to join

---

## 📊 Part 2: Extracting Text

### LEFT - Extract from Beginning

**Syntax**: `=LEFT(text, num_chars)`

**Example**:
```
   A              Formula         Result
1  PROD-12345     =LEFT(A1,4)     PROD
2  08012345678    =LEFT(A2,4)     0801
```

**Use Cases**:
- Extract area code from phone
- Get category code from product ID
- First few characters of text

### RIGHT - Extract from End

**Syntax**: `=RIGHT(text, num_chars)`

**Example**:
```
   A              Formula          Result
1  file_2024.pdf  =RIGHT(A1,3)     pdf
2  PROD-12345     =RIGHT(A2,5)     12345
```

**Use Cases**:
- Extract file extension
- Get last digits of ID
- Extract suffix

### MID - Extract from Middle

**Syntax**: `=MID(text, start_position, num_chars)`

**Example**:
```
   A              Formula             Result
1  PROD-2024-5678 =MID(A1,6,4)        2024
2  AB-CD-EF-GH    =MID(A2,4,2)        CD
```

**Parameters**:
- **start_position**: Where to start (1 = first character)
- **num_chars**: How many characters to extract

**Use Cases**:
- Extract year from date string
- Get specific part of formatted ID
- Parse structured text

---

## 🔍 Part 3: Finding & Measuring Text

### LEN - Count Characters

**Syntax**: `=LEN(text)`

**Example**:
```
   A           Formula     Result
1  Hello       =LEN(A1)    5
2  Data        =LEN(A2)    4
```

**Use Cases**:
- Validate input length (passwords, phone numbers)
- Find cells with extra characters
- Data quality checks

**Example - Find Long Text**:
```
=IF(LEN(A2)>100, "Too long", "OK")
```

### FIND - Locate Text Position

**Syntax**: `=FIND(search_text, within_text, [start_position])`

**Example**:
```
   A                    Formula              Result
1  john.doe@email.com   =FIND("@",A1)        9
2  PROD-12345           =FIND("-",A2)        5
```

**Returns**: Position number where text is found
**Case-sensitive**: YES

**Use Cases**:
- Find position of separator
- Extract text before/after specific character
- Validate format

### SEARCH - Like FIND but Case-Insensitive

**Syntax**: `=SEARCH(search_text, within_text)`

**Difference from FIND**: Not case-sensitive

```
=FIND("data", "MyData")    → Error (case-sensitive)
=SEARCH("data", "MyData")  → 3 (not case-sensitive)
```

---

## 🛠️ Part 4: Splitting Text

### SPLIT - Separate Text into Columns

**Syntax (Google Sheets)**: `=SPLIT(text, delimiter)`

**Example**:
```
   A                   Formula              Results spread across B, C, D
1  John,Doe,25         =SPLIT(A1,",")       John | Doe | 25
2  Lagos-Nigeria       =SPLIT(A2,"-")       Lagos | Nigeria
```

**Common Delimiters**:
- Comma: `,`
- Space: ` `
- Dash: `-`
- Pipe: `|`

**Excel Alternative**: Data → Text to Columns

---

## 💡 Part 5: Real-World Examples

### Example 1: Extract First Name from Email

**Problem**: john.doe@company.com → Get "john"

**Solution**:
```
Email: john.doe@company.com

Step 1: Find @ position
=FIND("@", A2)  → 9

Step 2: Extract everything before @
=LEFT(A2, FIND("@",A2)-1)  → john.doe

Step 3: Extract first name (before .)
=LEFT(A2, FIND(".",A2)-1)  → john
```

**One Formula**:
```
=LEFT(A2, FIND(".", A2)-1)
```

### Example 2: Create Username from Name

**Problem**: John Doe → john.doe

**Solution**:
```
First: John (A2)
Last: Doe (B2)

Formula:
=LOWER(A2 & "." & B2)  → john.doe
```

### Example 3: Parse Product Code

**Product Code Format**: CAT-YEAR-ID
**Example**: ELEC-2024-001

**Extract Each Part**:
```
   A              B (Category)        C (Year)          D (ID)
1  ELEC-2024-001  =LEFT(A2,4)         =MID(A2,6,4)      =RIGHT(A2,3)
2  ELEC-2024-001  ELEC                2024              001
```

### Example 4: Clean Phone Numbers

**Problem**: Various formats → Standard format

**Input**:
```
+234 801 234 5678
0801-234-5678
(0801) 234 5678
```

**Clean to**: 08012345678

**Step 1**: Remove all non-numbers
```
=SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(A2,"+234","0"),"-","")," ","")
```

**Better Approach - Multiple Steps**:
```
Column B: =SUBSTITUTE(A2,"+234","0")
Column C: =SUBSTITUTE(B2,"-","")
Column D: =SUBSTITUTE(C2," ","")
Column E: =SUBSTITUTE(D2,"(","")
Column F: =SUBSTITUTE(E2,")","")
```

Then copy final result back.

---

## ✍️ Part 6: Practice Exercises

### Exercise 1: Name Formatting

**Data**:
```
   A
1  Full Name
2  john doe
3  JANE SMITH
4  david LEE
```

**Tasks**:
1. Column B: First name only (use LEFT + FIND)
2. Column C: Last name only (use RIGHT or MID)
3. Column D: Proper case full name (use PROPER)
4. Column E: Email format: firstname.lastname@company.com

<details>
<summary>Solutions</summary>

B2: `=LEFT(A2, FIND(" ", A2)-1)`
C2: `=RIGHT(A2, LEN(A2)-FIND(" ", A2))`
D2: `=PROPER(A2)`
E2: `=LOWER(LEFT(A2,FIND(" ",A2)-1) & "." & RIGHT(A2,LEN(A2)-FIND(" ",A2)) & "@company.com")`

</details>

### Exercise 2: Product Code Parser

**Data**:
```
CAT-BRAND-SIZE-YEAR
FOOD-RICE-1KG-2024
ELEC-PHONE-6IN-2024
CLTH-SHIRT-L-2024
```

**Task**: Split into separate columns:
- Category
- Brand
- Size
- Year

**Hint**: Use SPLIT function or combination of LEFT, MID, RIGHT

### Exercise 3: Data Validation

**Data**: Phone numbers
**Rule**: Must be exactly 11 digits starting with 0

**Task**: Create formula that returns "Valid" or "Invalid"

```
=IF(AND(LEN(A2)=11, LEFT(A2,1)="0"), "Valid", "Invalid")
```

---

## 🎯 Part 7: Today's Project

### Project: Customer Data Standardization

**Scenario**: You have messy customer data that needs standardization.

**Create this data**:
```
   A                      B                    C
1  Full Name              Email                Phone
2  john doe               JOHN@EMAIL.COM       +234 801 234 5678
3  JANE SMITH             jane@email.com       0801-234-5678
4  david  lee             David.Lee@Email.Com  (0801) 234 5678
5  sarah connor           sarah@email.com      08012345678
```

**Your Tasks**:

1. **Column D - First Name** (Proper Case):
   - Extract first name
   - Use PROPER for capitalization

2. **Column E - Last Name** (Proper Case):
   - Extract last name
   - Use PROPER

3. **Column F - Email (Lowercase)**:
   - Convert all to lowercase
   - Standardize format

4. **Column G - Phone (Clean)**:
   - Remove all formatting
   - Result: 08012345678 format

5. **Column H - Username**:
   - Create as: firstname.lastname
   - Lowercase

6. **Column I - Validation**:
   - Check if phone is 11 digits
   - Return "Valid" or "Check Phone"

**Bonus**: Format as a professional table with headers, borders, and proper alignment.

---

## 🎯 Key Takeaways

✅ **CONCATENATE / &** - Join text
✅ **LEFT(text, num)** - Extract from start
✅ **RIGHT(text, num)** - Extract from end
✅ **MID(text, start, num)** - Extract from middle
✅ **LEN(text)** - Count characters
✅ **FIND/SEARCH(text, within)** - Locate text position
✅ **SPLIT(text, delimiter)** - Separate into columns
✅ **Combine functions** for powerful text manipulation

---

## 📚 Quick Reference

```
Text Combination:
=A2 & " " & B2               Join with space
=CONCATENATE(A2, " ", B2)    Same thing
=TEXTJOIN(", ", TRUE, A2:C2) Join range with comma

Text Extraction:
=LEFT(A2, 5)                 First 5 characters
=RIGHT(A2, 3)                Last 3 characters
=MID(A2, 3, 4)               4 chars starting at position 3

Text Info:
=LEN(A2)                     Count characters
=FIND("@", A2)               Find position of @
=SEARCH("text", A2)          Find text (case-insensitive)

Text Splitting:
=SPLIT(A2, ",")              Split by comma
```

---

## ✅ Self-Check

Can you:
- [ ] Join text from multiple cells
- [ ] Extract first N characters
- [ ] Extract last N characters
- [ ] Extract middle portion of text
- [ ] Count text length
- [ ] Find position of specific character
- [ ] Split text by delimiter
- [ ] Create email addresses from names
- [ ] Clean and standardize phone numbers

---

**Tomorrow (Day 10)**: Logical Functions - IF, AND, OR, Nested IFs!

**Pro Tip**: Text functions are often combined. Master each individually, then combine them for powerful data transformations!
