import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - merge two tables to get the connection between `empId` and `bonus`
    - filter to get `bonus` less than 1000 and null
    """
    employee = employee.merge(bonus, on="empId", how="left")
    employee = employee[(employee.loc[:,"bonus"]<1000)|(employee.loc[:,"bonus"].isna())].loc[:, ["name", "bonus"]]
    return employee
