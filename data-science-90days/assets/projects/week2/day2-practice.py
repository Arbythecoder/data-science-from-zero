# Week 2, Day 2: Selecting & Filtering Data - Practice Solutions
# The Coffee Shop Manager Story

import pandas as pd

print("="*60)
print("EXERCISE 1: Customer Analysis - Alice's Purchase History")
print("="*60)

# Coffee shop data
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

# Task 1: Filter for Alice only
alice_purchases = df[df['Customer'] == 'Alice']
print("\n1. Alice's Purchases:")
print(alice_purchases)

# Task 2: Calculate Alice's total spending
alice_total = alice_purchases['Price'].sum()
print(f"\n2. Alice's Total Spending: ${alice_total:.2f}")

# Task 3: Alice's most expensive purchase
alice_max = alice_purchases[alice_purchases['Price'] == alice_purchases['Price'].max()]
print(f"\n3. Alice's Most Expensive Purchase:")
print(alice_max[['Date', 'Drink', 'Price']])

# Task 4: All Large drinks
large_drinks = df[df['Size'] == 'Large']
print(f"\n4. All Large Drink Purchases ({len(large_drinks)} total):")
print(large_drinks[['Customer', 'Drink', 'Size', 'Price']])

# Task 5: Alice's average price
alice_avg = alice_purchases['Price'].mean()
print(f"\n5. Alice's Average Price Per Drink: ${alice_avg:.2f}")

print("\n" + "="*60)
print("EXERCISE 2: Location Performance Analysis")
print("="*60)

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

# Task 1: Downtown sales only
downtown = df_loc[df_loc['Location'] == 'Downtown']
print("\n1. Downtown Sales:")
print(downtown)

# Task 2: Calculate revenue
df_loc['Revenue'] = df_loc['Price'] * df_loc['Quantity']
downtown_revenue = df_loc[df_loc['Location'] == 'Downtown']['Revenue'].sum()
print(f"\n2. Downtown Total Revenue: ${downtown_revenue:.2f}")

# Task 3: Top drink at Mall
mall_sales = df_loc[df_loc['Location'] == 'Mall']
mall_by_drink = mall_sales.groupby('Drink')['Quantity'].sum().sort_values(ascending=False)
print(f"\n3. Top-Selling Drink at Mall:")
print(mall_by_drink)

# Task 4: Sales where quantity > 1
high_quantity = df_loc[df_loc['Quantity'] > 1]
print(f"\n4. Sales with Quantity > 1:")
print(high_quantity)

# Task 5: Location with highest average price
location_avg_price = df_loc.groupby('Location')['Price'].mean().sort_values(ascending=False)
print(f"\n5. Average Price by Location:")
print(location_avg_price)

# Task 6: Sort by total revenue
location_revenue = df_loc.groupby('Location')['Revenue'].sum().sort_values(ascending=False)
print(f"\n6. Total Revenue by Location:")
print(location_revenue)
print(f"\n📊 Winner: {location_revenue.index[0]} with ${location_revenue.iloc[0]:.2f}")

print("\n" + "="*60)
print("EXERCISE 3: Time-Based Analysis")
print("="*60)

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

# Task 1: Morning sales (Hour < 12)
morning = df_time[df_time['Hour'] < 12]
print("\n1. Morning Sales:")
print(morning)

# Task 2: Afternoon sales (Hour >= 12)
afternoon = df_time[df_time['Hour'] >= 12]
print("\n2. Afternoon Sales:")
print(afternoon)

# Task 3: Total customers morning vs afternoon
morning_customers = morning['Customer_Count'].sum()
afternoon_customers = afternoon['Customer_Count'].sum()
print(f"\n3. Customer Traffic:")
print(f"   Morning (before noon): {morning_customers} customers")
print(f"   Afternoon (noon onwards): {afternoon_customers} customers")
print(f"   📊 Busier time: {'Morning' if morning_customers > afternoon_customers else 'Afternoon'}")

# Task 4: Busiest hour
busiest = df_time[df_time['Customer_Count'] == df_time['Customer_Count'].max()]
print(f"\n4. Busiest Hour:")
print(busiest[['Time', 'Hour', 'Customer_Count']])

# Task 5: Lunch rush (11-14)
lunch_rush = df_time[(df_time['Hour'] >= 11) & (df_time['Hour'] <= 14)]
print(f"\n5. Lunch Rush Sales (11am-2pm):")
print(lunch_rush)

# Task 6: Average price morning vs afternoon
morning_avg_price = morning['Price'].mean()
afternoon_avg_price = afternoon['Price'].mean()
print(f"\n6. Average Price Comparison:")
print(f"   Morning: ${morning_avg_price:.2f}")
print(f"   Afternoon: ${afternoon_avg_price:.2f}")
print(f"   💰 Higher prices in: {'Morning' if morning_avg_price > afternoon_avg_price else 'Afternoon'}")

print("\n" + "="*60)
print("📊 BUSINESS INSIGHTS")
print("="*60)

print("""
Based on our analysis:

1. Customer Behavior:
   - Alice is a regular customer (4 purchases)
   - Average spending: $4.88 per visit
   - Prefers Medium and Large sizes

2. Location Performance:
   - Need to calculate revenue for all locations
   - Different locations may have different popular drinks

3. Time Analysis:
   - Morning is busier than afternoon
   - Peak hour is 9:00 AM (30 customers)
   - Should increase morning staff

4. Recommendations:
   - Focus marketing on morning rush
   - Consider loyalty program for regulars like Alice
   - Stock more popular drinks at peak hours
""")

print("\n🎉 ALL EXERCISES COMPLETE!")
print("You now know how to filter and analyze data like a pro!")
