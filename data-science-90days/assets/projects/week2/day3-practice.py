# Week 2, Day 3: Data Cleaning Project - Practice Solutions
# The Messy Spreadsheet Nightmare Story

import pandas as pd
import numpy as np

print("="*70)
print("EXERCISE 1: Clean Customer Database for Marketing Campaign")
print("="*70)

# Messy customer data
messy_customers = {
    'Customer_ID': [1, 2, 3, 3, 4, 5, 6, 7, 8, 9],
    'Name': ['  alice JOHNSON', 'Bob Smith', 'charlie davis', 'charlie davis',
             'DIANA MARTINEZ', np.nan, 'eve brown  ', 'Frank Lee', 'Grace Taylor', '  henry wilson  '],
    'Email': ['alice@email.com', 'BOB@EMAIL.COM', 'charlie@email.com', 'charlie@email.com',
              'diana@email.com', 'missing@email.com', 'eve@email.com', np.nan, 'grace@email.com', 'henry@email.com'],
    'Phone': ['555-1234', '5551234', '555-5678', '555-5678', '555-9012',
              '555-3456', '555-7890', '555-2345', '555-6789', '555  0123'],
    'City': ['New York', 'new york', 'LOS ANGELES', 'LOS ANGELES', 'Chicago',
             'New York', 'chicago', 'Los Angeles', 'New York', 'CHICAGO']
}

df_cust = pd.DataFrame(messy_customers)

print("\nORIGINAL MESSY DATA:")
print(df_cust)

# TASK 1: Remove duplicates
df_cust_clean = df_cust.drop_duplicates()
print(f"\n1. After removing duplicates: {len(df_cust_clean)} rows (was {len(df_cust)})")

# TASK 2: Clean names
df_cust_clean['Name'] = df_cust_clean['Name'].fillna('Unknown')
df_cust_clean['Name'] = df_cust_clean['Name'].str.strip().str.title()
print("\n2. Cleaned names:")
print(df_cust_clean['Name'])

# TASK 3: Standardize emails
df_cust_clean['Email'] = df_cust_clean['Email'].fillna('no-email@unknown.com')
df_cust_clean['Email'] = df_cust_clean['Email'].str.lower()
print("\n3. Standardized emails:")
print(df_cust_clean['Email'])

# TASK 4-5: Already handled with fillna() above

# TASK 6: Clean phone numbers
df_cust_clean['Phone'] = df_cust_clean['Phone'].str.replace('-', '').str.replace(' ', '')
print("\n6. Cleaned phone numbers:")
print(df_cust_clean['Phone'])

# TASK 7: Standardize cities
df_cust_clean['City'] = df_cust_clean['City'].str.strip().str.title()
print("\n7. Standardized cities:")
print(df_cust_clean['City'].unique())

# TASK 8: Final clean dataset
print("\n8. FINAL CLEAN CUSTOMER DATABASE:")
print(df_cust_clean)
print(f"\n✅ Clean! {len(df_cust_clean)} unique customers ready for marketing campaign!")

print("\n" + "="*70)
print("EXERCISE 2: Fix Product Inventory Data")
print("="*70)

# Messy inventory
messy_inventory = {
    'SKU': ['LP-001', 'MS-002', 'KB-003', 'KB-003', 'MN-004', 'LP-005'],
    'Product_Name': ['  laptop', 'MOUSE', 'Keyboard  ', 'Keyboard', '  Monitor  ', 'Laptop'],
    'Category': ['Electronics', 'electronics', 'ELECTRONICS', 'ELECTRONICS', 'Electronics', 'electronics'],
    'Price': ['999.00', '25', 75.00, '75', np.nan, 999],
    'Stock': [15, 'OUT OF STOCK', 80, 80, 30, '5'],
    'Supplier': ['TechCorp', 'techcorp', 'GADGETS INC', 'GADGETS INC', 'TechCorp', 'techcorp']
}

df_inv = pd.DataFrame(messy_inventory)

print("\nORIGINAL MESSY INVENTORY:")
print(df_inv)

# TASK 1: Remove duplicates
df_inv_clean = df_inv.drop_duplicates()
print(f"\n1. After removing duplicates: {len(df_inv_clean)} products")

# TASK 2: Clean product names
df_inv_clean['Product_Name'] = df_inv_clean['Product_Name'].str.strip().str.title()
print("\n2. Cleaned product names:")
print(df_inv_clean['Product_Name'])

# TASK 3: Standardize category
df_inv_clean['Category'] = df_inv_clean['Category'].str.title()
print("\n3. Standardized categories:")
print(df_inv_clean['Category'].unique())

# TASK 4: Convert price to numeric
df_inv_clean['Price'] = pd.to_numeric(df_inv_clean['Price'], errors='coerce')
print("\n4. Prices as numbers:")
print(df_inv_clean['Price'])

# Fill missing price with median
if df_inv_clean['Price'].isnull().sum() > 0:
    median_price = df_inv_clean['Price'].median()
    df_inv_clean['Price'] = df_inv_clean['Price'].fillna(median_price)
    print(f"   Filled missing price with median: ${median_price:.2f}")

# TASK 5: Fix stock column
df_inv_clean['Stock'] = df_inv_clean['Stock'].replace('OUT OF STOCK', 0)
df_inv_clean['Stock'] = pd.to_numeric(df_inv_clean['Stock'])
print("\n5. Fixed stock values:")
print(df_inv_clean['Stock'])

# TASK 6: Standardize suppliers
df_inv_clean['Supplier'] = df_inv_clean['Supplier'].str.title()
print("\n6. Standardized suppliers:")
print(df_inv_clean['Supplier'].unique())

# TASK 7: Add In_Stock column
df_inv_clean['In_Stock'] = df_inv_clean['Stock'] > 0
print("\n7. Added In_Stock indicator:")
print(df_inv_clean[['Product_Name', 'Stock', 'In_Stock']])

# TASK 8: Calculate total inventory value
df_inv_clean['Inventory_Value'] = df_inv_clean['Price'] * df_inv_clean['Stock']
total_value = df_inv_clean['Inventory_Value'].sum()

print("\n8. FINAL CLEAN INVENTORY:")
print(df_inv_clean)
print(f"\n💰 Total Inventory Value: ${total_value:,.2f}")

print("\n" + "="*70)
print("EXERCISE 3: Real-World Transaction Log Cleanup")
print("="*70)

# Messy transactions
messy_transactions = {
    'Transaction_ID': ['TXN001', 'TXN002', 'TXN003', 'TXN003', 'TXN004', 'TXN005',
                       'TXN006', 'TXN007', 'TXN008', 'TXN009'],
    'Date': ['2024-01-15 10:30:00', '2024/01/16 14:20:00', '15-01-2024', '15-01-2024',
             'Invalid Date', '2024-01-17', '2024-01-18 09:15:00', '2024-01-19',
             np.nan, '2024-01-20 16:45:00'],
    'Amount': [99.99, '150.00', 75, 75, np.nan, '200', 50.00, 125, 300.00, '  89.99  '],
    'Status': ['completed', 'COMPLETED', 'pending', 'pending', 'failed',
               'Completed', 'completed', 'PENDING', 'completed', 'completed'],
    'Payment_Method': ['Credit Card', 'credit card', 'PAYPAL', 'PAYPAL', 'Credit Card',
                      'paypal', 'Credit Card', 'credit card', 'PayPal', 'CREDIT CARD']
}

df_txn = pd.DataFrame(messy_transactions)

print("\nORIGINAL MESSY TRANSACTIONS:")
print(df_txn)

# TASK 1: Remove duplicates
df_txn_clean = df_txn.drop_duplicates()
print(f"\n1. After removing duplicates: {len(df_txn_clean)} transactions")

# TASK 2: Convert dates
df_txn_clean['Date'] = pd.to_datetime(df_txn_clean['Date'], errors='coerce', format='mixed')
print("\n2. Converted dates:")
print(df_txn_clean['Date'])

# TASK 3: Convert amount to float
df_txn_clean['Amount'] = df_txn_clean['Amount'].astype(str).str.strip()
df_txn_clean['Amount'] = pd.to_numeric(df_txn_clean['Amount'], errors='coerce')
print("\n3. Amounts as numbers:")
print(df_txn_clean['Amount'])

# TASK 4: Standardize status
df_txn_clean['Status'] = df_txn_clean['Status'].str.lower()
print("\n4. Standardized status:")
print(df_txn_clean['Status'].unique())

# TASK 5: Standardize payment method
df_txn_clean['Payment_Method'] = df_txn_clean['Payment_Method'].str.title()
print("\n5. Standardized payment methods:")
print(df_txn_clean['Payment_Method'].unique())

# TASK 6: Filter out failed transactions
df_txn_clean = df_txn_clean[df_txn_clean['Status'] != 'failed']
print(f"\n6. After removing failed: {len(df_txn_clean)} transactions")

# TASK 7: Calculate total revenue (completed only)
completed_txns = df_txn_clean[df_txn_clean['Status'] == 'completed']
total_revenue = completed_txns['Amount'].sum()
print(f"\n7. Total Revenue (completed transactions): ${total_revenue:,.2f}")

# TASK 8: Find busiest day
df_txn_clean['Day'] = df_txn_clean['Date'].dt.date
busiest_day = df_txn_clean.groupby('Day').size().sort_values(ascending=False)
print("\n8. Transactions per day:")
print(busiest_day)
if len(busiest_day) > 0:
    print(f"\n   📅 Busiest day: {busiest_day.index[0]} with {busiest_day.iloc[0]} transactions")

# TASK 9: Revenue by payment method
revenue_by_payment = completed_txns.groupby('Payment_Method')['Amount'].sum().sort_values(ascending=False)
print("\n9. Revenue by Payment Method:")
print(revenue_by_payment)

print("\n" + "="*70)
print("📊 BUSINESS INSIGHTS FROM CLEAN DATA")
print("="*70)

print(f"""
Customer Database Insights:
- {len(df_cust_clean)} unique customers
- Cities: {', '.join(df_cust_clean['City'].unique())}
- All names properly formatted
- All emails valid

Inventory Insights:
- {len(df_inv_clean)} unique products
- Total inventory value: ${df_inv_clean['Inventory_Value'].sum():,.2f}
- Products in stock: {df_inv_clean['In_Stock'].sum()}
- Out of stock: {(~df_inv_clean['In_Stock']).sum()}

Transaction Insights:
- {len(completed_txns)} completed transactions
- Total revenue: ${total_revenue:,.2f}
- Average transaction: ${completed_txns['Amount'].mean():,.2f}
- Most popular payment: {revenue_by_payment.index[0] if len(revenue_by_payment) > 0 else 'N/A'}
""")

print("="*70)
print("🎉 ALL CLEANING EXERCISES COMPLETE!")
print("="*70)
print("""
You now know how to:
✅ Handle missing data
✅ Remove duplicates
✅ Clean text (strip, title case, lowercase)
✅ Fix data types (to_numeric, to_datetime)
✅ Standardize formats
✅ Create calculated columns
✅ Extract business insights from clean data

🏆 You're ready for real-world messy data!
""")

# BONUS: Universal Cleaning Function Template
print("\n💡 BONUS: Universal Cleaning Function")
print("="*70)

def universal_cleaner(df, text_columns=None, numeric_columns=None, date_columns=None):
    """
    Universal data cleaning function.

    Args:
        df: DataFrame to clean
        text_columns: List of column names with text
        numeric_columns: List of column names with numbers
        date_columns: List of column names with dates

    Returns:
        Clean DataFrame
    """
    df_clean = df.copy()

    # Remove duplicates
    df_clean = df_clean.drop_duplicates()

    # Clean text columns
    if text_columns:
        for col in text_columns:
            if col in df_clean.columns:
                df_clean[col] = df_clean[col].astype(str).str.strip().str.title()

    # Convert numeric columns
    if numeric_columns:
        for col in numeric_columns:
            if col in df_clean.columns:
                df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')

    # Convert date columns
    if date_columns:
        for col in date_columns:
            if col in df_clean.columns:
                df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce')

    # Reset index
    df_clean = df_clean.reset_index(drop=True)

    return df_clean

# Test it!
print("\nTesting universal_cleaner on customer data...")
test_clean = universal_cleaner(
    pd.DataFrame(messy_customers),
    text_columns=['Name', 'City'],
    numeric_columns=['Customer_ID']
)
print("✅ Universal cleaner works!")
print(f"Cleaned {len(test_clean)} rows")

print("\n🚀 You're now a data cleaning expert! Ready for Week 3!")
