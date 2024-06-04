import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - same table merge
    - compare two columns
    - columns filter and rename
    """
    new_table = employee.merge(employee, 
                            left_on="managerId", 
                            right_on="id", 
                            how="left",
                            suffixes=("_employee", "_manager"))
    new_table = new_table[new_table["salary_employee"] > new_table["salary_manager"]].loc[:, ["name_employee"]]
    new_table = new_table.rename(columns={"name_employee": "Employee"})
    return new_table
