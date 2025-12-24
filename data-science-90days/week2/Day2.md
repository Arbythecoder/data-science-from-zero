# Week 2, Day 2: Selecting & Filtering Data

## 📖 Today's Story: The Coffee Shop Manager

You've just been hired as a data analyst for "Code & Coffee," a small chain of coffee shops. The owner hands you a messy spreadsheet with thousands of sales records and says:

*"I need to know which drinks are popular, who our best customers are, and when we're busiest. Can you help?"*

Today, you'll learn to filter and select exactly the data you need to answer these questions.

---

## 🎯 What You'll Learn

- Selecting specific columns from a DataFrame
- Filtering rows based on conditions
- Combining multiple filters
- Sorting data to find insights

---

## 💼 The Business Problem

**Code & Coffee** has 3 locations and sells various drinks. The owner wants answers to:

1. What are our top-selling drinks?
2. Who spends the most money?
3. Which location makes the most revenue?
4. What are our busiest hours?

Let's analyze the data to find out!

---

## 📊 Loading the Data

```python
import pandas as pd

# Coffee shop sales data
sales = {
    'Date': ['2024-01-15', '2024-01-15', '2024-01-15', '2024-01-16', '2024-01-16',
             '2024-01-16', '2024-01-17', '2024-01-17'],
    'Time': ['08:30', '09:15', '14:20', '07:45', '10:30', '15:10', '08:00', '13:45'],
    'Location': ['Downtown', 'Downtown', 'Mall', 'Airport', 'Downtown', 'Mall', 'Airport', 'Mall'],
    'Drink': ['Latte', 'Espresso', 'Cappuccino', 'Latte', 'Mocha', 'Latte', 'Espresso', 'Cappuccino'],
    'Size': ['Medium', 'Small', 'Large', 'Medium', 'Large', 'Small', 'Medium', 'Large'],
    'Price': [4.50, 3.00, 5.50, 4.50, 5.00, 4.00, 3.00, 5.50],
    'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Alice', 'Eve', 'Bob', 'Frank']
}

df = pd.DataFrame(sales)
print(df)
```

---

## 🔍 Core Techniques

### 1. Selecting Columns

**Story**: The owner only wants to see drink names and prices.

```python
# Select single column
drinks = df['Drink']
print(drinks)

# Select multiple columns
drinks_and_prices = df[['Drink', 'Price']]
print(drinks_and_prices)
```

### 2. Filtering Rows

**Story**: Show me only Latte sales.

```python
# Filter for lattes only
lattes = df[df['Drink'] == 'Latte']
print(lattes)

# Filter for prices above $4
expensive = df[df['Price'] > 4.00]
print(expensive)
```

### 3. Multiple Conditions

**Story**: Find all Large Lattes from the Downtown location.

```python
# AND condition (both must be true)
large_lattes = df[(df['Drink'] == 'Latte') & (df['Size'] == 'Large')]
print(large_lattes)

# OR condition (either can be true)
latte_or_mocha = df[(df['Drink'] == 'Latte') | (df['Drink'] == 'Mocha')]
print(latte_or_mocha)

# Complex filter
downtown_expensive = df[(df['Location'] == 'Downtown') & (df['Price'] >= 4.50)]
print(downtown_expensive)
```

### 4. Sorting Data

**Story**: Who are our top customers by total spending?

```python
# Sort by price (ascending)
df_sorted = df.sort_values('Price')
print(df_sorted)

# Sort by price (descending)
df_sorted_desc = df.sort_values('Price', ascending=False)
print(df_sorted_desc)

# Sort by multiple columns
df_multi_sort = df.sort_values(['Location', 'Price'], ascending=[True, False])
print(df_multi_sort)
```

---

## 💻 Practice Exercises

### Exercise 1: Customer Analysis

**Story**: Alice has been complaining about her recent bills. Check her purchase history.

```python
import pandas as pd

# Coffee shop data (expanded)
sales = {
    'Date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19',
             '2024-01-15', '2024-01-16', '2024-01-18', '2024-01-19', '2024-01-20'],
    'Customer': ['Alice', 'Alice', 'Bob', 'Alice', 'Charlie',
                 'Bob', 'Diana', 'Bob', 'Alice', 'Charlie'],
    'Drink': ['Latte', 'Mocha', 'Espresso', 'Cappuccino', 'Latte',
              'Latte', 'Mocha', 'Espresso', 'Latte', 'Cappuccino'],
    'Price': [4.50, 5.00, 3.00, 5.50, 4.50,
              4.50, 5.00, 3.00, 4.50, 5.50],
    'Size': ['Medium', 'Large', 'Small', 'Large', 'Medium',
             'Medium', 'Large', 'Small', 'Medium', 'Large']
}

df = pd.DataFrame(sales)

# YOUR TASKS:
# 1. Filter to show only Alice's purchases
# 2. Calculate Alice's total spending
# 3. Find Alice's most expensive purchase
# 4. Show all customers who bought Large drinks
# 5. Find the average price Alice pays per drink
```

**Expected Output**:
```
Alice made 4 purchases
Total spent: $19.50
Most expensive: $5.50 (Cappuccino)
```

---

### Exercise 2: Location Performance

**Story**: The owner wants to know which location is performing best.

```python
# Multi-location sales data
sales_data = {
    'Location': ['Downtown', 'Mall', 'Airport', 'Downtown', 'Mall',
                 'Airport', 'Downtown', 'Mall', 'Airport', 'Downtown'],
    'Drink': ['Latte', 'Espresso', 'Cappuccino', 'Mocha', 'Latte',
              'Espresso', 'Latte', 'Cappuccino', 'Mocha', 'Espresso'],
    'Price': [4.50, 3.00, 5.50, 5.00, 4.50,
              3.00, 4.50, 5.50, 5.00, 3.00],
    'Quantity': [2, 1, 1, 1, 3, 2, 1, 2, 1, 4]
}

df_loc = pd.DataFrame(sales_data)

# YOUR TASKS:
# 1. Filter to show only Downtown sales
# 2. Calculate total revenue for Downtown (Price × Quantity)
# 3. Find which drink sells most at the Mall
# 4. Show all sales where Quantity > 1
# 5. Find the location with highest average price
# 6. Sort locations by total revenue (highest to lowest)
```

**Business Impact**: This tells us where to focus marketing efforts!

---

### Exercise 3: Time-Based Analysis

**Story**: The manager suspects mornings are busier than afternoons. Let's check!

```python
# Time-stamped sales data
time_sales = {
    'Time': ['07:30', '08:15', '09:00', '10:30', '12:00',
             '13:45', '15:20', '16:00', '17:30', '18:00'],
    'Hour': [7, 8, 9, 10, 12, 13, 15, 16, 17, 18],
    'Drink': ['Latte', 'Espresso', 'Latte', 'Cappuccino', 'Mocha',
              'Latte', 'Espresso', 'Cappuccino', 'Latte', 'Mocha'],
    'Price': [4.50, 3.00, 4.50, 5.50, 5.00,
              4.50, 3.00, 5.50, 4.50, 5.00],
    'Customer_Count': [15, 25, 30, 20, 22, 18, 12, 10, 8, 5]
}

df_time = pd.DataFrame(time_sales)

# YOUR TASKS:
# 1. Filter to show only morning sales (Hour < 12)
# 2. Filter to show afternoon sales (Hour >= 12)
# 3. Calculate total customers in morning vs afternoon
# 4. Find the busiest hour (highest Customer_Count)
# 5. Show all sales during lunch rush (Hour between 11 and 14)
# 6. Calculate average price during morning vs afternoon
```

**Insight**: Should we staff more employees in the morning?

---

## 🎯 Challenge Exercise (Optional)

**Story**: You're analyzing competitor data!

You've collected data from 3 competing coffee shops. Create a DataFrame with:
- Shop name
- Average price
- Customer rating (1-5)
- Distance from downtown (km)

Then answer:
1. Which shop has the highest rating?
2. Which shops are within 2km of downtown?
3. Which shop offers the best value (high rating, low price)?
4. Create a recommendation for customers based on priorities

---

## 📝 Key Takeaways

✅ Use `df['column']` to select one column
✅ Use `df[['col1', 'col2']]` for multiple columns
✅ Use `df[df['column'] > value]` to filter rows
✅ Combine filters with `&` (and) and `|` (or)
✅ Use `.sort_values()` to order your data
✅ Always think: "What question am I trying to answer?"

---

## 🔗 Next Steps

Tomorrow (Day 3): Clean messy sales data and handle missing values

**Homework**:
1. Complete all 3 exercises
2. Apply these techniques to your own data (expenses, workout log, etc.)
3. Think: What questions would YOU want to answer about your data?

---

## 💡 Pro Tips

1. **Use meaningful variable names**: `alice_purchases` not `df2`
2. **Comment your filters**: Explain what you're looking for
3. **Check your results**: Print shape and head() after filtering
4. **Save filtered data**: `filtered_df = df[condition]` for reuse

---

## 🐛 Common Errors

**Error**: `KeyError: 'column_name'`
- **Solution**: Check spelling, use `df.columns` to see available columns

**Error**: `ValueError: The truth value of a Series is ambiguous`
- **Solution**: Use `&` and `|`, not `and` and `or`

**Error**: Empty DataFrame after filtering
- **Solution**: Check your condition, print `df['column'].unique()` to see values

---

*Remember: Every line of code should answer a business question!* 📊
