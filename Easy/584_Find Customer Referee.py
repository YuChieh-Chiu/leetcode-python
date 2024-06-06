import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - filter column `referee_id` not equals to `2` or is null
    - only return the dataframe with column `name`
    """
    condition = ((customer["referee_id"]!=2) | (customer["referee_id"].isna()))
    customer = customer[condition].loc[:, ["name"]]
    return customer
