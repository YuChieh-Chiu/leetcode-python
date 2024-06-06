import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - consider the corner case that dataframe is empty
    - filter the row with `area` >= 3000000 or `population` >= 25000000
    - return dataframe with columns `name`, `population`, `area`
    """
    if world.empty:
        return world[["name", "population", "area"]]
    else:
        condition = ((world["area"] >= 3000000) | (world["population"] >= 25000000))
        big_country = world[condition].loc[:, ["name", "population", "area"]]
        return big_country
