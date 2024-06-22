import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - we need to `merge` two dataframe employee and department
    - we should do the following steps to get the top3 unique salary in each department:
        (1) `groupby` department name
        (2) `drop duplicate` salary
        (3) `sort` salary by `value` in descending order
        (4) get the `top3` unique salary in each department
    - `merge` back top3 dataframe with employee dataframe to get the employee name
    - `rename` columns to get correct column names
    """
    employee = employee.merge(department, 
        how="left",
        left_on="departmentId", 
        right_on="id", 
        suffixes=("_emp", "_dept"))
    top3 = employee[["name_dept", "salary"]].groupby(["name_dept"]).apply(lambda x: x.drop_duplicates().sort_values(["salary"], ascending=False)[:3])
    top3.reset_index(inplace=True, drop=True)
    top3 = top3.merge(employee,
        how="left",
        on=["name_dept", "salary"])
    top3.rename(
        columns={
            "name_dept": "Department",
            "name_emp": "Employee",
            "salary": "Salary"
        },
        inplace=True
    )
    top3 = top3.loc[:, ["Department", "Employee", "Salary"]]
    return top3
