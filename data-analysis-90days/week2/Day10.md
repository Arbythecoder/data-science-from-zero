# 📅 Day 10: Logical Functions - IF, AND, OR

**Goal**: Create conditional logic to automate decision-making in spreadsheets

**Time**: 60 minutes

---

## 🧠 Core Concepts

### The IF Function - Make Decisions

**Syntax**: `=IF(condition, value_if_true, value_if_false)`

**How it works**:
1. Tests a condition
2. If TRUE → returns first value
3. If FALSE → returns second value

**Example**:
```
=IF(A2>100, "High", "Low")

If A2 is 150: Returns "High"
If A2 is 50: Returns "Low"
```

---

## 📊 Part 1: Basic IF Statements

### Example 1: Pass/Fail

```
   A       B (Formula)              C (Result)
1  Score   =IF(A2>=70,"Pass","Fail")
2  85      =IF(A2>=70,"Pass","Fail")  Pass
3  60      =IF(A3>=70,"Pass","Fail")  Fail
```

### Example 2: Sales Bonus

```
Sales > 100000 → ₦10,000 bonus
Otherwise → ₦5,000 bonus

Formula: =IF(A2>100000, 10000, 5000)
```

### Example 3: Inventory Status

```
Stock < 10 → "Order Now"
Stock >= 10 → "Sufficient"

Formula: =IF(A2<10, "Order Now", "Sufficient")
```

---

## 💡 Part 2: AND Function - Multiple Conditions (ALL must be TRUE)

**Syntax**: `=AND(condition1, condition2, condition3, ...)`

**Returns**: TRUE only if ALL conditions are true

**Example**:
```
=AND(A2>50, B2<100)

True if: A2 is greater than 50 AND B2 is less than 100
False if: Either condition fails
```

### Combined with IF

```
Age >= 18 AND Score >= 70 → "Eligible"
Otherwise → "Not Eligible"

=IF(AND(A2>=18, B2>=70), "Eligible", "Not Eligible")
```

### Real Example: Loan Approval

```
   A      B          C (Formula)
1  Age    Income     =IF(AND(A2>=21, B2>=30000), "Approved", "Denied")
2  25     50000      Approved  (both conditions met)
3  20     40000      Denied    (age too low)
4  30     25000      Denied    (income too low)
```

---

## 🔍 Part 3: OR Function - Multiple Conditions (ANY can be TRUE)

**Syntax**: `=OR(condition1, condition2, condition3, ...)`

**Returns**: TRUE if ANY condition is true

**Example**:
```
=OR(A2="VIP", B2>100000)

True if: Customer is VIP OR sales > 100000 (or both)
```

### Combined with IF

```
Discount if: VIP customer OR purchase > ₦50,000

=IF(OR(A2="VIP", B2>50000), "10% Discount", "No Discount")
```

### Real Example: Priority Shipping

```
   A          B         C (Formula)
1  Type       Amount    =IF(OR(A2="Express", B2>100000), "Priority", "Standard")
2  Standard   150000    Priority  (amount > 100000)
3  Express    5000      Priority  (express type)
4  Standard   3000      Standard  (neither condition)
```

---

## 🎯 Part 4: Nested IF - Multiple Levels

**Use when**: More than 2 outcomes

**Syntax**: `=IF(condition1, value1, IF(condition2, value2, value3))`

### Example: Grade Calculator

```
Score >= 90: A
Score >= 80: B
Score >= 70: C
Otherwise: F

Formula:
=IF(A2>=90, "A", IF(A2>=80, "B", IF(A2>=70, "C", "F")))
```

**How it works**:
```
IF score >= 90 → "A"
ELSE IF score >= 80 → "B"
ELSE IF score >= 70 → "C"
ELSE → "F"
```

### Example: Commission Tiers

```
Sales > 100000: 10%
Sales > 50000: 7%
Sales > 20000: 5%
Otherwise: 2%

=IF(A2>100000, A2*0.1, IF(A2>50000, A2*0.07, IF(A2>20000, A2*0.05, A2*0.02)))
```

---

## ✍️ Practice Exercises

### Exercise 1: Student Eligibility

**Rules**:
- Age >= 18 AND GPA >= 3.0 → "Admitted"
- Otherwise → "Not Admitted"

**Data**:
```
   A       B       C (Your Formula)
1  Age     GPA
2  20      3.5
3  17      3.8
4  19      2.5
```

<details>
<summary>Answer</summary>
C2: `=IF(AND(A2>=18, B2>=3.0), "Admitted", "Not Admitted")`
</details>

### Exercise 2: Shipping Cost

**Rules**:
- Weight > 10kg OR Distance > 100km → ₦2,000
- Otherwise → ₦1,000

**Data**:
```
   A          B           C (Your Formula)
1  Weight(kg) Distance(km)
2  15         50
3  5          150
4  8          80
```

<details>
<summary>Answer</summary>
C2: `=IF(OR(A2>10, B2>100), 2000, 1000)`
</details>

### Exercise 3: Performance Rating

**Rules**:
- >= 95: Excellent
- >= 85: Good
- >= 70: Satisfactory
- < 70: Needs Improvement

**Data**:
```
   A        B (Your Formula)
1  Score
2  98
3  87
4  72
5  65
```

<details>
<summary>Answer</summary>
B2: `=IF(A2>=95,"Excellent",IF(A2>=85,"Good",IF(A2>=70,"Satisfactory","Needs Improvement")))`
</details>

---

## 🏆 Today's Project

### Project: Sales Commission Calculator

**Scenario**: Calculate sales commission based on performance and tenure.

**Rules**:
1. Senior reps (Tenure >= 3 years):
   - Sales > ₦100,000: 10% commission
   - Sales > ₦50,000: 7% commission
   - Otherwise: 5% commission

2. Junior reps (Tenure < 3 years):
   - Sales > ₦100,000: 7% commission
   - Sales > ₦50,000: 5% commission
   - Otherwise: 3% commission

**Create this data**:
```
   A          B         C         D (Commission %)    E (Commission Amount)
1  Rep Name   Tenure    Sales
2  John       5         120000
3  Jane       2         80000
4  David      4         45000
5  Sarah      1         150000
```

**Your Tasks**:
1. Column D: Calculate commission % using nested IF and AND
2. Column E: Calculate commission amount (Sales * Commission %)
3. Add summary:
   - Total commissions paid
   - Average commission
   - Highest commission

<details>
<summary>Formula Hint</summary>

D2:
```
=IF(AND(B2>=3, C2>100000), 0.10,
  IF(AND(B2>=3, C2>50000), 0.07,
    IF(B2>=3, 0.05,
      IF(C2>100000, 0.07,
        IF(C2>50000, 0.05, 0.03)))))
```

E2: `=C2*D2`

</details>

---

## 🎯 Key Takeaways

✅ **IF(condition, true, false)** - Basic conditional logic
✅ **AND(cond1, cond2)** - ALL conditions must be TRUE
✅ **OR(cond1, cond2)** - ANY condition can be TRUE
✅ **Nested IF** - Multiple outcomes/levels
✅ **Combine functions** - IF + AND, IF + OR for complex logic

---

## 📚 Quick Reference

```
Basic IF:
=IF(A1>100, "High", "Low")

IF with AND (both required):
=IF(AND(A1>50, B1<100), "Valid", "Invalid")

IF with OR (either works):
=IF(OR(A1="VIP", B1>1000), "Special", "Regular")

Nested IF:
=IF(A1>90, "A", IF(A1>80, "B", IF(A1>70, "C", "F")))
```

---

**Tomorrow (Day 11)**: VLOOKUP - Match data across tables!
