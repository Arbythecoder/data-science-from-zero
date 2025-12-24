# Week 2, Day 1: Introduction to Pandas & DataFrames

## 📚 What You'll Learn Today

- What is Pandas and why it's essential for data science
- Understanding Series and DataFrames
- Creating DataFrames from different data sources
- Basic DataFrame operations

---

## 🎯 Why Pandas?

Pandas is the most important library for data analysis in Python. It provides:
- **DataFrames**: Excel-like tables but with Python power
- **Fast operations**: Handle millions of rows efficiently
- **Data cleaning**: Built-in tools for messy data
- **Integration**: Works with NumPy, Matplotlib, Scikit-learn

**Real-world use**: Every data scientist uses Pandas daily for data manipulation.

---

## 📖 Core Concepts

### 1. Series (1D Data)

A Series is like a single column in a spreadsheet:

```python
import pandas as pd

# Create a Series
temperatures = pd.Series([72, 68, 75, 80, 77])
print(temperatures)

# Output:
# 0    72
# 1    68
# 2    75
# 3    80
# 4    77
# dtype: int64
```

### 2. DataFrame (2D Data)

A DataFrame is like a full spreadsheet with rows and columns:

```python
# Create DataFrame from dictionary
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [999, 25, 75, 299],
    'Stock': [15, 150, 80, 30]
}

df = pd.DataFrame(data)
print(df)

# Output:
#     Product  Price  Stock
# 0    Laptop    999     15
# 1     Mouse     25    150
# 2  Keyboard     75     80
# 3   Monitor    299     30
```

### 3. Loading Data from Files

```python
# From CSV (most common)
sales_df = pd.read_csv('sales_data.csv')

# From Excel
excel_df = pd.read_excel('report.xlsx')

# From JSON
json_df = pd.read_json('data.json')
```

### 4. Basic Exploration

```python
# View first 5 rows
df.head()

# View last 5 rows
df.tail()

# Get DataFrame info
df.info()

# Statistical summary
df.describe()

# Shape (rows, columns)
df.shape

# Column names
df.columns

# Data types
df.dtypes
```

---

## 💻 Practice Exercises

### Exercise 1: E-commerce Sales Data

**Scenario**: You're analyzing online store sales.

```python
import pandas as pd

# Create sales data
sales_data = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
    'Quantity': [1, 2, 1, 1, 2],
    'Price': [999, 25, 75, 299, 999]
}

df = pd.DataFrame(sales_data)

# YOUR TASKS:
# 1. Display the first 3 rows
# 2. Show the DataFrame shape (how many rows and columns?)
# 3. Calculate total revenue: Quantity * Price for each order
# 4. Add a new column 'Revenue' to the DataFrame
# 5. Find the total revenue across all orders
```

**Expected Output**:
```
First 3 rows should show Order 101-103
Shape: (5, 5)
Total Revenue: $3,396
```

---

### Exercise 2: Student Grades Analysis

**Scenario**: You're a teacher analyzing student performance.

```python
import pandas as pd

# Create student data
students = {
    'Name': ['John', 'Emma', 'Mike', 'Sarah', 'Tom', 'Lisa'],
    'Math': [85, 92, 78, 95, 88, 90],
    'Science': [88, 85, 92, 89, 91, 87],
    'English': [92, 88, 85, 93, 86, 94]
}

df = pd.DataFrame(students)

# YOUR TASKS:
# 1. Display all student data
# 2. Calculate each student's average grade (create 'Average' column)
# 3. Find the student with the highest average
# 4. Find the subject with the highest class average
# 5. Count how many students scored above 90 in Math
```

**Hint**:
```python
# Calculate average across columns
df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Find maximum
df['Average'].max()

# Find student with max average
df[df['Average'] == df['Average'].max()]
```

---

### Exercise 3: Real-World CSV Data

**Scenario**: Load and explore actual data from a CSV file.

```python
import pandas as pd

# First, create a sample CSV file
sample_data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Website_Visitors': [1250, 1380, 1120, 1450, 1590],
    'Sales': [45, 52, 38, 61, 68],
    'Revenue': [2250, 2600, 1900, 3050, 3400]
}

# Save to CSV
df = pd.DataFrame(sample_data)
df.to_csv('website_data.csv', index=False)

# NOW YOUR TASKS:
# 1. Read the CSV file into a new DataFrame
# 2. Display the first 3 rows
# 3. Show DataFrame info (data types, non-null counts)
# 4. Calculate conversion rate: (Sales / Website_Visitors) * 100
# 5. Add 'Conversion_Rate' column to DataFrame
# 6. Find the day with the highest conversion rate
# 7. Calculate average daily revenue
```

**Real-world learning**: This is exactly how you'd start analyzing any business data!

---

## 🎯 Challenge Exercise (Optional)

Create a DataFrame representing your own data:
- At least 4 columns
- At least 6 rows
- Mix of text and numbers
- Calculate at least 2 new columns based on existing data
- Save it to CSV and read it back

**Examples**:
- Personal expense tracker (Date, Category, Amount, Description)
- Workout log (Date, Exercise, Sets, Reps, Weight)
- Reading list (Title, Author, Pages, Rating, Finished_Date)
- Budget tracker (Month, Income, Expenses, Savings, Category)

---

## 📝 Key Takeaways

✅ Pandas DataFrames are like Excel spreadsheets in Python
✅ `pd.read_csv()` is your go-to for loading data
✅ `.head()`, `.info()`, `.describe()` help you explore data
✅ You can create new columns with calculations
✅ DataFrames make data analysis fast and efficient

---

## 🔗 Next Steps

Tomorrow (Day 2): Selecting and filtering data from DataFrames

**Homework**: Complete all 3 exercises above. These form the foundation for everything in data science!

---

## 💡 Common Errors & Solutions

**Error**: `KeyError: 'column_name'`
- **Solution**: Check spelling and case sensitivity of column names

**Error**: `FileNotFoundError` when reading CSV
- **Solution**: Check file path, make sure file exists in same folder

**Error**: `ValueError: Length mismatch`
- **Solution**: All lists in dictionary must have same length

---

*Practice makes perfect! Don't just read - type the code and experiment!*
