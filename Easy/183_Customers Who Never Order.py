import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - `id` in `Customers` table = `customerId` in `Orders` table
    - merge two tables and filter whose orderId is null
    - get customers name
    """
    new_table = customers.merge(orders, 
                            left_on="id",
                            right_on="customerId",
                            how="left",
                            suffixes=("_customer", "_order"))
    new_table = new_table[new_table["id_order"].isnull()].loc[:, ["name"]]
    new_table = new_table.rename(columns={"name":"Customers"})
    return new_table
