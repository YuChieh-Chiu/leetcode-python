import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - note that the `managerId` column follows the RULE below
        (1) if managerId is null, then the employee does not have a manager
        (2) no employee will be the manager of themself
    - we can do the steps as below
        (1) use `value_counts()` to groupby `managerId` and get the number of each `managerId`
        (2) filter out managerIds that appear at least five times as a `list()`
        (3) get ids in `list()` and only .iloc[:, [1]]
    """
    cnt = employee["managerId"].value_counts()
    name_df = employee[employee["id"].isin(cnt[cnt >= 5].index.tolist())].iloc[:, [1]]
    return name_df
