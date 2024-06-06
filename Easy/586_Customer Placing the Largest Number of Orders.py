import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - we need to find the `customer_number` of customer whose number of `order_number` is the largest
    - consider the corner case that dataframe is empty
    - group by `customer_number` and sort by count in descending order -> use value_counts()
    - get the first row of column `customer_number`
    """
    if orders.empty:
        return orders[["customer_number"]]
    else:
        order = orders["customer_number"].value_counts(
            ascending=False
        )
        print(order)
        customer_with_most_orders = pd.DataFrame({
            "customer_number": [order.index[0]]
        })
        return customer_with_most_orders
