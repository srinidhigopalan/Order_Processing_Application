# import unittest
# import pandas as pd

# class TestRevenueCalculations(unittest.TestCase):

#     def setUp(self):
#         # Sample data for testing
#         data = {
#             'order_id': [1, 2, 3],
#             'customer_id': [101, 102, 101],
#             'order_date': ['2024-01-01', '2024-01-15', '2024-02-01'],
#             'product_id': [1001, 1002, 1001],
#             'product_name': ['Product A', 'Product B', 'Product A'],
#             'product_price': [10.0, 20.0, 10.0],
#             'quantity': [1, 2, 3]
#         }
#         self.df = pd.DataFrame(data)
#         self.df['order_date'] = pd.to_datetime(self.df['order_date'])
#         self.df['revenue'] = self.df['product_price'] * self.df['quantity']

#     def test_revenue_by_month(self):
#         self.df['order_month'] = self.df['order_date'].dt.to_period('M')
#         revenue_by_month = self.df.groupby('order_month')['revenue'].sum()
#         expected_revenue_by_month = pd.Series([10.0, 60.0], index=['2024-01', '2024-02'])
#         pd.testing.assert_series_equal(revenue_by_month, expected_revenue_by_month)

#     def test_revenue_by_product(self):
#         revenue_by_product = self.df.groupby('product_id')['revenue'].sum()
#         expected_revenue_by_product = pd.Series([40.0, 40.0], index=[1001, 1002])
#         pd.testing.assert_series_equal(revenue_by_product, expected_revenue_by_product)

#     def test_revenue_by_customer(self):
#         revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
#         expected_revenue_by_customer = pd.Series([40.0, 40.0], index=[101, 102])
#         pd.testing.assert_series_equal(revenue_by_customer, expected_revenue_by_customer)

#     def test_top_10_customers(self):
#         revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
#         top_10_customers = revenue_by_customer.nlargest(10)
#         expected_top_10_customers = pd.Series([40.0, 40.0], index=[101, 102])
#         pd.testing.assert_series_equal(top_10_customers, expected_top_10_customers)

# if __name__ == '__main__':
#     unittest.main()
# import pandas as pd
# from io import StringIO

# class TestRevenueCalculations:
#     def setUp(self):
#         # Single record CSV data for testing
#         csv_data = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
# 1,101,2024-01-01,1001,Product A,10.0,1
# """
#         # Read data from CSV string
#         self.df = pd.read_csv(StringIO(csv_data))
#         # Convert order_date to datetime format
#         self.df['order_date'] = pd.to_datetime(self.df['order_date'])
#         # Compute revenue for each order
#         self.df['revenue'] = self.df['product_price'] * self.df['quantity']

#     def test_revenue_by_month(self):
#         self.df['order_month'] = self.df['order_date'].dt.to_period('M')
#         revenue_by_month = self.df.groupby('order_month')['revenue'].sum()
#         expected_revenue_by_month = pd.Series([10.0], index=pd.PeriodIndex(['2024-01'], freq='M'))

#         print("Revenue by Month:")
#         print(revenue_by_month)
#         print("Expected Revenue by Month:")
#         print(expected_revenue_by_month)
#         print("Test Revenue by Month: ", revenue_by_month.equals(expected_revenue_by_month))

#     def test_revenue_by_product(self):
#         revenue_by_product = self.df.groupby('product_id')['revenue'].sum()
#         expected_revenue_by_product = pd.Series([10.0], index=[1001])

#         print("\nRevenue by Product:")
#         print(revenue_by_product)
#         print("Expected Revenue by Product:")
#         print(expected_revenue_by_product)
#         print("Test Revenue by Product: ", revenue_by_product.equals(expected_revenue_by_product))

#     def test_revenue_by_customer(self):
#         revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
#         expected_revenue_by_customer = pd.Series([10.0], index=[101])

#         print("\nRevenue by Customer:")
#         print(revenue_by_customer)
#         print("Expected Revenue by Customer:")
#         print(expected_revenue_by_customer)
#         print("Test Revenue by Customer: ", revenue_by_customer.equals(expected_revenue_by_customer))

#     def test_top_10_customers(self):
#         revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
#         top_10_customers = revenue_by_customer.nlargest(10)
#         expected_top_10_customers = pd.Series([10.0], index=[101])

#         print("\nTop 10 Customers:")
#         print(top_10_customers)
#         print("Expected Top 10 Customers:")
#         print(expected_top_10_customers)
#         print("Test Top 10 Customers: ", top_10_customers.equals(expected_top_10_customers))

# if __name__ == '__main__':
#     test = TestRevenueCalculations()
#     test.setUp()
#     test.test_revenue_by_month()
#     test.test_revenue_by_product()
#     test.test_revenue_by_customer()
#     test.test_top_10_customers()

# import pandas as pd
# from io import StringIO

# class TestRevenueCalculations:
#     def setUp(self):
#         # Single record CSV data for testing
#         csv_data = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
# 1,101,2024-01-01,1001,Product A,10.0,1
# """
#         # Read data from CSV string
#         self.df = pd.read_csv(StringIO(csv_data))
#         # Convert order_date to datetime format
#         self.df['order_date'] = pd.to_datetime(self.df['order_date'])
#         # Compute revenue for each order
#         self.df['revenue'] = self.df['product_price'] * self.df['quantity']

#     def test_revenue_by_month(self):
#         self.df['order_month'] = self.df['order_date'].dt.to_period('M')
#         revenue_by_month = self.df.groupby('order_month')['revenue'].sum()
#         expected_revenue_by_month = pd.Series([10.0], index=pd.PeriodIndex(['2024-01'], freq='M'))

#         print("\nRevenue by Month Test:")
#         print("Calculated Revenue by Month:")
#         print(revenue_by_month)
#         print("Expected Revenue by Month:")
#         print(expected_revenue_by_month)
#         if revenue_by_month.equals(expected_revenue_by_month):
#             print("Test Passed!\n")
#         else:
#             print("Test Failed!\n")

#     def test_revenue_by_product(self):
#         revenue_by_product = self.df.groupby('product_id')['revenue'].sum()
#         expected_revenue_by_product = pd.Series([10.0], index=[1001])

#         print("Revenue by Product Test:")
#         print("Calculated Revenue by Product:")
#         print(revenue_by_product)
#         print("Expected Revenue by Product:")
#         print(expected_revenue_by_product)
#         if revenue_by_product.equals(expected_revenue_by_product):
#             print("Test Passed!\n")
#         else:
#             print("Test Failed!\n")

#     def test_revenue_by_customer(self):
#         revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
#         expected_revenue_by_customer = pd.Series([10.0], index=[101])

#         print("Revenue by Customer Test:")
#         print("Calculated Revenue by Customer:")
#         print(revenue_by_customer)
#         print("Expected Revenue by Customer:")
#         print(expected_revenue_by_customer)
#         if revenue_by_customer.equals(expected_revenue_by_customer):
#             print("Test Passed!\n")
#         else:
#             print("Test Failed!\n")

#     def test_top_10_customers(self):
#         revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
#         top_10_customers = revenue_by_customer.nlargest(10)
#         expected_top_10_customers = pd.Series([10.0], index=[101])

#         print("Top 10 Customers Test:")
#         print("Calculated Top 10 Customers:")
#         print(top_10_customers)
#         print("Expected Top 10 Customers:")
#         print(expected_top_10_customers)
#         if top_10_customers.equals(expected_top_10_customers):
#             print("Test Passed!\n")
#         else:
#             print("Test Failed!\n")

# if __name__ == '__main__':
#     test = TestRevenueCalculations()
#     test.setUp()
#     test.test_revenue_by_month()
#     test.test_revenue_by_product()
#     test.test_revenue_by_customer()
#     test.test_top_10_customers()

# import pandas as pd
# from io import StringIO

# # Sample data for testing
# data = """
# order_id,customer_id,order_date,product_id,product_name,product_price,quantity
# 1,Cust001,2023-01-05,1001,Product A,50,2
# 2,Cust002,2023-01-10,1002,Product B,30,1
# 3,Cust001,2023-02-15,1001,Product A,50,3
# 4,Cust003,2023-02-20,1003,Product C,100,1
# 5,Cust002,2023-03-01,1002,Product B,30,2
# 6,Cust001,2023-03-10,1001,Product A,50,1
# 7,Cust004,2023-03-15,1001,Product A,50,2
# 8,Cust002,2023-04-02,1002,Product B,30,3
# 9,Cust001,2023-04-05,1003,Product C,100,2
# 10,Cust003,2023-04-10,1001,Product A,50,1
# """

# import pandas as pd
# from io import StringIO

# # Sample data for testing
# data = """
# order_id,customer_id,order_date,product_id,product_name,product_price,quantity
# 1,Cust001,2023-01-05,1001,Product A,50,2
# 2,Cust002,2023-01-10,1002,Product B,30,1
# 3,Cust001,2023-02-15,1001,Product A,50,3
# 4,Cust003,2023-02-20,1003,Product C,100,1
# 5,Cust002,2023-03-01,1002,Product B,30,2
# 6,Cust001,2023-03-10,1001,Product A,50,1
# 7,Cust004,2023-03-15,1001,Product A,50,2
# 8,Cust002,2023-04-02,1002,Product B,30,3
# 9,Cust001,2023-04-05,1003,Product C,100,2
# 10,Cust003,2023-04-10,1001,Product A,50,1
# """

# import pandas as pd
# from io import StringIO

# # Sample data for testing
# data = """
# order_id,customer_id,order_date,product_id,product_name,product_price,quantity
# 1,Cust001,2023-01-05,1001,Product A,50,2
# 2,Cust002,2023-01-10,1002,Product B,30,1
# 3,Cust001,2023-02-15,1001,Product A,50,3
# 4,Cust003,2023-02-20,1003,Product C,100,1
# 5,Cust002,2023-03-01,1002,Product B,30,2
# 6,Cust001,2023-03-10,1001,Product A,50,1
# 7,Cust004,2023-03-15,1001,Product A,50,2
# 8,Cust002,2023-04-02,1002,Product B,30,3
# 9,Cust001,2023-04-05,1003,Product C,100,2
# 10,Cust003,2023-04-10,1001,Product A,50,1
# """

# # Load the data into a DataFrame
# df = pd.read_csv(StringIO(data), parse_dates=['order_date'])

# # Calculate total price for each order
# df['total_price'] = df['product_price'] * df['quantity']

# # Test 1: Total Revenue by Month
# def test_revenue_by_month():
#     df['month'] = df['order_date'].dt.to_period('M')
#     revenue_by_month = df.groupby('month')['total_price'].sum()
#     expected_revenue_by_month = {
#         '2023-01': 80,  # (50*2) + (30*1)
#         '2023-02': 200, # (50*3) + (100*1)
#         '2023-03': 180, # (50*1) + (50*2) + (30*2)
#         '2023-04': 280  # (100*2) + (50*1)
#     }
    
#     print("Calculated Revenue by Month:")
#     print(revenue_by_month.to_dict())
    
#     print("\nExpected Revenue by Month:")
#     print(expected_revenue_by_month)

# # Test 2: Total Revenue by Product
# def test_revenue_by_product():
#     revenue_by_product = df.groupby('product_name')['total_price'].sum()
#     expected_revenue_by_product = {
#         'Product A': 350, # (50*2) + (50*3) + (50*1) + (50*2)
#         'Product B': 90,  # (30*1) + (30*2) + (30*3)
#         'Product C': 200   # (100*1) + (100*2)
#     }
    
#     print("\nCalculated Revenue by Product:")
#     print(revenue_by_product.to_dict())
    
#     print("\nExpected Revenue by Product:")
#     print(expected_revenue_by_product)

# # Test 3: Total Revenue by Customer
# def test_revenue_by_customer():
#     revenue_by_customer = df.groupby('customer_id')['total_price'].sum()
#     expected_revenue_by_customer = {
#         'Cust001': 350, # (50*2) + (50*3) + (50*1) + (50*2) + (100*2)
#         'Cust002': 90,  # (30*1) + (30*2) + (30*3)
#         'Cust003': 200, # (100*1) + (100*2)
#         'Cust004': 100   # (50*2)
#     }
    
#     print("\nCalculated Revenue by Customer:")
#     print(revenue_by_customer.to_dict())
    
#     print("\nExpected Revenue by Customer:")
#     print(expected_revenue_by_customer)

# # Test 4: Top 10 Customers by Revenue
# def test_top_10_customers():
#     revenue_by_customer = df.groupby('customer_id')['total_price'].sum()
#     top_10_customers = revenue_by_customer.nlargest(10)
#     expected_top_10_customers = revenue_by_customer.sort_values(ascending=False).head(10)
    
#     print("\nCalculated Top 10 Customers by Revenue:")
#     print(top_10_customers)
    
#     print("\nExpected Top 10 Customers by Revenue:")
#     print(expected_top_10_customers)

# # Run the tests
# test_revenue_by_month()
# test_revenue_by_product()
# test_revenue_by_customer()
# test_top_10_customers()

# import pandas as pd
# from io import StringIO

# # Sample data for testing
# data = """
# order_id,customer_id,order_date,product_id,product_name,product_price,quantity
# 1,Cust001,2023-01-05,1001,Product A,50,2
# 2,Cust002,2023-01-10,1002,Product B,30,1
# 3,Cust001,2023-02-15,1001,Product A,50,3
# 4,Cust003,2023-02-20,1003,Product C,100,1
# 5,Cust002,2023-03-01,1002,Product B,30,2
# 6,Cust001,2023-03-10,1001,Product A,50,1
# 7,Cust004,2023-03-15,1001,Product A,50,2
# 8,Cust002,2023-04-02,1002,Product B,30,3
# 9,Cust001,2023-04-05,1003,Product C,100,2
# 10,Cust003,2023-04-10,1001,Product A,50,1
# """

# # Load the data into a DataFrame
# df = pd.read_csv(StringIO(data), parse_dates=['order_date'])

# # Calculate total price for each order
# df['total_price'] = df['product_price'] * df['quantity']

# # Test 1: Total Revenue by Month
# def test_revenue_by_month():
#     df['month'] = df['order_date'].dt.to_period('M')
#     revenue_by_month = df.groupby('month')['total_price'].sum()
#     expected_revenue_by_month = {
#         '2023-01': 80,  # (50*2) + (30*1)
#         '2023-02': 200, # (50*3) + (100*1)
#         '2023-03': 180, # (50*1) + (50*2) + (30*2)
#         '2023-04': 280  # (100*2) + (50*1)
#     }
    
#     print("Calculated Revenue by Month:")
#     print(revenue_by_month.to_dict())
    
#     print("\nExpected Revenue by Month:")
#     print(expected_revenue_by_month)
    
#     # Check for pass/fail
#     if revenue_by_month.to_dict() == expected_revenue_by_month:
#         print("\nTest 1: Total Revenue by Month - PASSED")
#     else:
#         print("\nTest 1: Total Revenue by Month - FAILED")

# # Test 2: Total Revenue by Product
# def test_revenue_by_product():
#     revenue_by_product = df.groupby('product_name')['total_price'].sum()
#     expected_revenue_by_product = {
#         'Product A': 350, # (50*2) + (50*3) + (50*1) + (50*2)
#         'Product B': 90,  # (30*1) + (30*2) + (30*3)
#         'Product C': 200   # (100*1) + (100*2)
#     }
    
#     print("\nCalculated Revenue by Product:")
#     print(revenue_by_product.to_dict())
    
#     print("\nExpected Revenue by Product:")
#     print(expected_revenue_by_product)
    
#     # Check for pass/fail
#     if revenue_by_product.to_dict() == expected_revenue_by_product:
#         print("\nTest 2: Total Revenue by Product - PASSED")
#     else:
#         print("\nTest 2: Total Revenue by Product - FAILED")

# # Test 3: Total Revenue by Customer
# def test_revenue_by_customer():
#     revenue_by_customer = df.groupby('customer_id')['total_price'].sum()
#     expected_revenue_by_customer = {
#         'Cust001': 350, # (50*2) + (50*3) + (50*1) + (50*2) + (100*2)
#         'Cust002': 90,  # (30*1) + (30*2) + (30*3)
#         'Cust003': 200, # (100*1) + (100*2)
#         'Cust004': 100   # (50*2)
#     }
    
#     print("\nCalculated Revenue by Customer:")
#     print(revenue_by_customer.to_dict())
    
#     print("\nExpected Revenue by Customer:")
#     print(expected_revenue_by_customer)
    
#     # Check for pass/fail
#     if revenue_by_customer.to_dict() == expected_revenue_by_customer:
#         print("\nTest 3: Total Revenue by Customer - PASSED")
#     else:
#         print("\nTest 3: Total Revenue by Customer - FAILED")

# # Test 4: Top 10 Customers by Revenue
# def test_top_10_customers():
#     revenue_by_customer = df.groupby('customer_id')['total_price'].sum()
#     top_10_customers = revenue_by_customer.nlargest(10)
#     expected_top_10_customers = revenue_by_customer.sort_values(ascending=False).head(10)
    
#     print("\nCalculated Top 10 Customers by Revenue:")
#     print(top_10_customers)
    
#     print("\nExpected Top 10 Customers by Revenue:")
#     print(expected_top_10_customers)
    
#     # Check for pass/fail
#     if top_10_customers.equals(expected_top_10_customers):
#         print("\nTest 4: Top 10 Customers by Revenue - PASSED")
#     else:
#         print("\nTest 4: Top 10 Customers by Revenue - FAILED")

# # Run the tests
# test_revenue_by_month()
# test_revenue_by_product()
# test_revenue_by_customer()
# test_top_10_customers()

# import pandas as pd
# from io import StringIO

# # Sample data for testing
# data = """
# order_id,customer_id,order_date,product_id,product_name,product_price,quantity
# 1,Cust001,2023-01-05,1001,Product A,50,2
# 2,Cust002,2023-01-10,1002,Product B,30,1
# 3,Cust001,2023-02-15,1001,Product A,50,3
# 4,Cust003,2023-02-20,1003,Product C,100,1
# 5,Cust001,2023-03-01,1001,Product A,50,1
# 6,Cust004,2023-03-10,1001,Product A,50,2
# 7,Cust002,2023-03-15,1002,Product B,30,3
# 8,Cust001,2023-04-02,1003,Product C,100,2
# 9,Cust003,2023-04-10,1001,Product A,50,1
# 10,Cust002,2023-04-15,1002,Product B,30,2
# """

# import unittest
# import pandas as pd
# from io import StringIO

# class TestOrderProcessing(unittest.TestCase):
#     def setUp(self):
#         # Sample data to test
#         data = """order_date,product_id,product_price,quantity,customer_id
# 2024-01-15,1,10,2,1001
# 2024-01-20,2,20,1,1002
# 2024-02-15,1,10,1,1001
# 2024-02-20,2,20,3,1003
# 2024-03-15,3,30,1,1004
# """
#         self.df = pd.read_csv(StringIO(data))
#         self.df['order_date'] = pd.to_datetime(self.df['order_date'])
#         self.df['revenue'] = self.df['product_price'] * self.df['quantity']
#         self.df['order_month'] = self.df['order_date'].dt.to_period('M')
        
#         # Expected outputs
#         self.expected_revenue_by_month = self.df.groupby('order_month')['revenue'].sum()
#         self.expected_revenue_by_product = self.df.groupby('product_id')['revenue'].sum()
#         self.expected_revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
#         self.expected_top_10_customers = self.expected_revenue_by_customer.nlargest(10)

#     def test_revenue_by_month(self):
#         revenue_by_month = self.df.groupby('order_month')['revenue'].sum()
#         pd.testing.assert_series_equal(revenue_by_month, self.expected_revenue_by_month)

#     def test_revenue_by_product(self):
#         revenue_by_product = self.df.groupby('product_id')['revenue'].sum()
#         pd.testing.assert_series_equal(revenue_by_product, self.expected_revenue_by_product)

#     def test_revenue_by_customer(self):
#         revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
#         pd.testing.assert_series_equal(revenue_by_customer, self.expected_revenue_by_customer)

#     def test_top_10_customers(self):
#         top_10_customers = self.expected_revenue_by_customer.nlargest(10)
#         pd.testing.assert_series_equal(top_10_customers, self.expected_top_10_customers)

# if __name__ == '__main__':
#     unittest.main()

import unittest
import pandas as pd
from io import StringIO

class TestOrderProcessing(unittest.TestCase):
    def setUp(self):
        # Sample data to test
        data = """order_id,customer_id,order_date,product_id,product_name,product_price,quantity
1,Cust001,2024-01-01,1001,Product A,10,2
2,Cust002,2024-01-01,1002,Product B,20,1
3,Cust003,2024-01-02,1003,Product C,30,3
4,Cust004,2024-01-03,1004,Product D,40,1
5,Cust005,2024-01-03,1005,Product E,50,4
6,Cust006,2024-01-04,1006,Product F,60,2
7,Cust007,2024-01-05,1007,Product G,70,1
8,Cust008,2024-01-06,1008,Product H,80,3
9,Cust009,2024-01-07,1009,Product I,90,5
10,Cust010,2024-01-08,1010,Product J,100,2
11,Cust011,2024-01-09,1011,Product K,110,1
12,Cust012,2024-01-10,1012,Product L,120,4
13,Cust013,2024-01-11,1013,Product M,130,3
14,Cust014,2024-01-12,1014,Product N,140,2
15,Cust015,2024-01-13,1015,Product O,150,1
16,Cust001,2024-01-14,1002,Product B,20,3
17,Cust002,2024-01-15,1003,Product C,30,2
18,Cust003,2024-01-16,1004,Product D,40,1
19,Cust004,2024-01-17,1005,Product E,50,2
20,Cust005,2024-01-18,1006,Product F,60,1"""

        self.df = pd.read_csv(StringIO(data))
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        self.df['revenue'] = self.df['product_price'] * self.df['quantity']
        self.df['order_month'] = self.df['order_date'].dt.to_period('M')
        
        # Expected outputs
        self.expected_revenue_by_month = self.df.groupby('order_month')['revenue'].sum()
        self.expected_revenue_by_product = self.df.groupby('product_id')['revenue'].sum()
        self.expected_revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
        self.expected_top_10_customers = self.expected_revenue_by_customer.nlargest(10)

    def test_revenue_by_month(self):
        revenue_by_month = self.df.groupby('order_month')['revenue'].sum()
        print("Expected revenue by month:\n", self.expected_revenue_by_month)
        print("Computed revenue by month:\n", revenue_by_month)
        pd.testing.assert_series_equal(revenue_by_month, self.expected_revenue_by_month)
        print("Revenue by month test passed.\n")

    def test_revenue_by_product(self):
        revenue_by_product = self.df.groupby('product_id')['revenue'].sum()
        print("Expected revenue by product:\n", self.expected_revenue_by_product)
        print("Computed revenue by product:\n", revenue_by_product)
        pd.testing.assert_series_equal(revenue_by_product, self.expected_revenue_by_product)
        print("Revenue by product test passed.\n")

    def test_revenue_by_customer(self):
        revenue_by_customer = self.df.groupby('customer_id')['revenue'].sum()
        print("Expected revenue by customer:\n", self.expected_revenue_by_customer)
        print("Computed revenue by customer:\n", revenue_by_customer)
        pd.testing.assert_series_equal(revenue_by_customer, self.expected_revenue_by_customer)
        print("Revenue by customer test passed.\n")

    def test_top_10_customers(self):
        top_10_customers = self.expected_revenue_by_customer.nlargest(10)
        print("Expected top 10 customers by revenue:\n", self.expected_top_10_customers)
        print("Computed top 10 customers by revenue:\n", top_10_customers)
        pd.testing.assert_series_equal(top_10_customers, self.expected_top_10_customers)
        print("Top 10 customers test passed.\n")

if __name__ == '__main__':
    unittest.main()
