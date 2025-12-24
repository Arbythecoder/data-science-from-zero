# Week 2, Day 1: Pandas & DataFrames Practice Solutions
# Complete the exercises, then check your answers below

import pandas as pd

print("="*50)
print("EXERCISE 1: E-commerce Sales Data")
print("="*50)

# Create sales data
sales_data = {
    'Order_ID': [101, 102, 103, 104, 105],
    'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop'],
    'Quantity': [1, 2, 1, 1, 2],
    'Price': [999, 25, 75, 299, 999]
}

df = pd.DataFrame(sales_data)

# Task 1: Display first 3 rows
print("\n1. First 3 rows:")
print(df.head(3))

# Task 2: Show shape
print(f"\n2. DataFrame shape: {df.shape}")
print(f"   (5 rows, 5 columns)")

# Task 3 & 4: Calculate and add Revenue column
df['Revenue'] = df['Quantity'] * df['Price']
print("\n3 & 4. DataFrame with Revenue column:")
print(df)

# Task 5: Total revenue
total_revenue = df['Revenue'].sum()
print(f"\n5. Total Revenue: ${total_revenue:,}")

print("\n" + "="*50)
print("EXERCISE 2: Student Grades Analysis")
print("="*50)

# Create student data
students = {
    'Name': ['John', 'Emma', 'Mike', 'Sarah', 'Tom', 'Lisa'],
    'Math': [85, 92, 78, 95, 88, 90],
    'Science': [88, 85, 92, 89, 91, 87],
    'English': [92, 88, 85, 93, 86, 94]
}

df_students = pd.DataFrame(students)

# Task 1: Display all data
print("\n1. All student data:")
print(df_students)

# Task 2: Calculate average grade
df_students['Average'] = df_students[['Math', 'Science', 'English']].mean(axis=1)
print("\n2. With Average column:")
print(df_students)

# Task 3: Student with highest average
top_student = df_students[df_students['Average'] == df_students['Average'].max()]
print(f"\n3. Top student:")
print(top_student)

# Task 4: Subject with highest class average
subject_averages = {
    'Math': df_students['Math'].mean(),
    'Science': df_students['Science'].mean(),
    'English': df_students['English'].mean()
}
print(f"\n4. Subject averages:")
for subject, avg in subject_averages.items():
    print(f"   {subject}: {avg:.2f}")

best_subject = max(subject_averages, key=subject_averages.get)
print(f"   Best subject: {best_subject}")

# Task 5: Students with Math > 90
high_math = df_students[df_students['Math'] > 90]
print(f"\n5. Students with Math score > 90: {len(high_math)}")
print(high_math[['Name', 'Math']])

print("\n" + "="*50)
print("EXERCISE 3: Real-World CSV Data")
print("="*50)

# Create and save sample CSV
sample_data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05'],
    'Website_Visitors': [1250, 1380, 1120, 1450, 1590],
    'Sales': [45, 52, 38, 61, 68],
    'Revenue': [2250, 2600, 1900, 3050, 3400]
}

df_web = pd.DataFrame(sample_data)
df_web.to_csv('website_data.csv', index=False)
print("✓ CSV file created: website_data.csv")

# Task 1: Read CSV
df_loaded = pd.read_csv('website_data.csv')
print("\n1. Loaded from CSV:")

# Task 2: First 3 rows
print("\n2. First 3 rows:")
print(df_loaded.head(3))

# Task 3: DataFrame info
print("\n3. DataFrame info:")
print(df_loaded.info())

# Task 4 & 5: Calculate conversion rate
df_loaded['Conversion_Rate'] = (df_loaded['Sales'] / df_loaded['Website_Visitors']) * 100
print("\n4 & 5. With Conversion Rate:")
print(df_loaded)

# Task 6: Day with highest conversion
best_day = df_loaded[df_loaded['Conversion_Rate'] == df_loaded['Conversion_Rate'].max()]
print(f"\n6. Best conversion day:")
print(best_day[['Date', 'Conversion_Rate']])

# Task 7: Average daily revenue
avg_revenue = df_loaded['Revenue'].mean()
print(f"\n7. Average daily revenue: ${avg_revenue:,.2f}")

print("\n" + "="*50)
print("🎉 ALL EXERCISES COMPLETE!")
print("="*50)

# CHALLENGE: Create your own DataFrame!
print("\n💡 CHALLENGE: Create a DataFrame about something YOU track:")
print("   - Personal expenses")
print("   - Workout log")
print("   - Reading list")
print("   - Time tracker")
print("\nPractice makes perfect! 🚀")
