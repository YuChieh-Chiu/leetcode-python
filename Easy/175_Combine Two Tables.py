import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - left merge
    - columns filter
    """
    new_table = person.merge(address, on="personId", how="left")
    columns = ["firstName", "lastName", "city", "state"]
    return new_table.loc[:, columns]
