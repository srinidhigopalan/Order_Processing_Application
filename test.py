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
