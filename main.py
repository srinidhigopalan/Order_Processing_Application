import pandas as pd

# Read data from CSV
df = pd.read_csv('orders.csv')

# Convert order_date to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])

# Compute revenue for each order
df['revenue'] = df['product_price'] * df['quantity']

# Compute total revenue by month
df['order_month'] = df['order_date'].dt.to_period('M')
revenue_by_month = df.groupby('order_month')['revenue'].sum()

# Compute total revenue by product
revenue_by_product = df.groupby('product_id')['revenue'].sum()

# Compute total revenue by customer
revenue_by_customer = df.groupby('customer_id')['revenue'].sum()

# Identify top 10 customers by revenue
top_10_customers = revenue_by_customer.nlargest(10)

# Print results
print("Total revenue by month:\n", revenue_by_month)
print("\nTotal revenue by product:\n", revenue_by_product)
print("\nTotal revenue by customer:\n", revenue_by_customer)
print("\nTop 10 customers by revenue:\n", top_10_customers)

