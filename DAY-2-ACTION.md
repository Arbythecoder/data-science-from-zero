# DAY 2: DATA CLEANING & ADVANCED FORMULAS

**Goal**: Clean messy data and use IF/VLOOKUP

---

## ✅ CHECKLIST

### Morning Session (2 hours)
- [ ] **Read** [week1/Day4.md](data-analysis-90days/week1/Day4.md) (20 min)
- [ ] **Read** [week2/Day8.md](data-analysis-90days/week2/Day8.md) (30 min)
- [ ] **Practice** cleaning messy data (70 min)

### Afternoon Session (2 hours)
- [ ] **Read** [week2/Day10.md](data-analysis-90days/week2/Day10.md) (30 min)
- [ ] **Skim** [week2/Day11-14-Combined.md](data-analysis-90days/week2/Day11-14-Combined.md) - VLOOKUP section only (30 min)
- [ ] **Practice** IF and VLOOKUP (60 min)

### Evening Application (1 hour)
- [ ] **Clean** your real messy business data
- [ ] **Add** calculated columns

---

## 🎯 WHAT TO BUILD

**Data Cleaning Tasks**:
1. Remove duplicate rows
2. Fix formatting (spaces, capitalization)
3. Fill missing values
4. Standardize categories

**Add These Formulas**:
```
=IF(A1>100, "High", "Low")                    // Categorize
=VLOOKUP(A1, Sheet2!A:B, 2, FALSE)           // Match data
=TRIM(A1)                                     // Remove spaces
=PROPER(A1)                                   // Capitalize properly
```

---

## 📝 KEY SKILLS TODAY

### Data Cleaning:
- Remove duplicates (Data → Remove duplicates)
- Find & replace extra spaces
- Use TRIM() to clean text
- Use PROPER() for capitalization

### IF Statements:
```
=IF(condition, value_if_true, value_if_false)

Example:
=IF(D2>1000, "Premium", "Standard")
```

### VLOOKUP:
```
=VLOOKUP(lookup_value, table_range, column_number, FALSE)

Example:
=VLOOKUP(A2, PriceList!A:B, 2, FALSE)
```

---

## ✅ DAY 2 COMPLETE WHEN:

You have:
- [ ] Cleaned your messy data (no duplicates, no extra spaces)
- [ ] Added IF statement to categorize data
- [ ] Used VLOOKUP to match data from another sheet
- [ ] All data properly formatted

---

**Time**: 5 hours | **Difficulty**: Medium | **Day**: 2/6

**Tomorrow**: Build your dashboard!
