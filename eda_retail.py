import pandas as pd

# Load the dataset
df = pd.read_csv('retail_sales_dataset.csv')

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create new column: Month
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Total Revenue
total_revenue = df['Total Amount'].sum()
print(f"Total Revenue: ₹{total_revenue}")

# Average Order Value
average_order_value = df['Total Amount'].mean()
print(f"Average Order Value: ₹{average_order_value:.2f}")

# Total Units Sold
total_units = df['Quantity'].sum()
print(f"Total Units Sold: {total_units}")

# Descriptive Statistics
print("\nSummary Statistics:")
print(df[['Quantity', 'Price per Unit', 'Total Amount']].describe())
import matplotlib.pyplot as plt

# Group by Month and calculate total revenue
monthly_sales = df.groupby('Month')['Total Amount'].sum().reset_index()

# Sort by month (in case it's unordered)
monthly_sales['Month'] = pd.to_datetime(monthly_sales['Month'])
monthly_sales = monthly_sales.sort_values('Month')

# Plotting the monthly sales trend
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales['Month'], monthly_sales['Total Amount'], marker='o', color='orange')
plt.title('Monthly Sales Trend', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Total Revenue (₹)')
plt.grid(True)
plt.tight_layout()
plt.show()


# ---------------------------
# 📊 1. Gender-based Sales
# ---------------------------
gender_sales = df.groupby('Gender')['Total Amount'].sum()

print("Revenue by Gender:")
print(gender_sales)

# Plot gender revenue
gender_sales.plot(kind='bar', color=['skyblue', 'pink'], title='Total Revenue by Gender')
plt.ylabel("Revenue (₹)")
plt.xlabel("Gender")
plt.tight_layout()
plt.show()


# ---------------------------
# 📊 2. Age Distribution
# ---------------------------
plt.figure(figsize=(8, 4))
plt.hist(df['Age'], bins=10, color='green', edgecolor='black')
plt.title('Customer Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.show()


# ---------------------------
# 📊 3. Top 10 Customers by Revenue
# ---------------------------
top_customers = df.groupby('Customer ID')['Total Amount'].sum().sort_values(ascending=False).head(10)

print("\nTop 10 Customers by Revenue:")
print(top_customers)

# Plot top customers
top_customers.plot(kind='bar', title='Top 10 Customers by Revenue', color='purple')
plt.ylabel("Revenue (₹)")
plt.xlabel("Customer ID")
plt.tight_layout()
plt.show()
# ---------------------------
# 📦 1. Total Revenue by Product Category
# ---------------------------
category_revenue = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)

print("\nTotal Revenue by Product Category:")
print(category_revenue)

# Plot revenue per category
category_revenue.plot(kind='bar', color='coral', title='Revenue by Product Category')
plt.ylabel("Revenue (₹)")
plt.xlabel("Product Category")
plt.tight_layout()
plt.show()


# ---------------------------
# 📦 2. Total Quantity Sold by Product Category
# ---------------------------
category_quantity = df.groupby('Product Category')['Quantity'].sum().sort_values(ascending=False)

print("\nTotal Quantity Sold by Product Category:")
print(category_quantity)

# Plot quantity per category
category_quantity.plot(kind='bar', color='skyblue', title='Quantity Sold by Product Category')
plt.ylabel("Total Quantity")
plt.xlabel("Product Category")
plt.tight_layout()
plt.show()


# ---------------------------
# 📦 3. Top 5 Categories by Revenue
# ---------------------------
top_categories = category_revenue.head(5)

print("\nTop 5 Best-Selling Categories (by revenue):")
print(top_categories)
