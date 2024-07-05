import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - `sales_person` indicates the salesperson information
    - `company` indicates the company information
    - `orders` indicates the orders between salesperson and company
    - so we can do the following steps:
       (1) left `merge` orders with company
       (2) and use `==` to filter orders related to "RED" company 
       (3) use `list(set())` to filter those salesperson not related to "RED" company on orders
       (4) create an output dataframe to show the result
    """
    orders = orders.loc[:, ["com_id", "sales_id"]].merge(
        company,
        on="com_id",
        how="left"
    )
    orders = list(set(orders[orders["name"]=="RED"]["sales_id"]))
    person_name = sales_person[~sales_person.isin(orders)].reset_index(drop=True)
    output = pd.DataFrame({
        "name": [person_name.loc[row, "name"] for row in range(person_name.shape[0]) if pd.isnull(person_name.loc[row, "sales_id"])==False]
    })
    return output
