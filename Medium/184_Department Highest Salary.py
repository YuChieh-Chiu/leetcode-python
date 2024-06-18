import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - Note that `Department name` is guaranteed not null
    - (1) we should merge two tables
    - (2) we should groupby `departmentId`
    - (3) we should get the highest value in each group
    - (4) we should only ouput dataframe with `Department name`, `Employee`, and `Salary`
    """
    tables = employee.merge(
        department,
        how="left",
        left_on="departmentId",
        right_on="id"
    )
    highest_by_group = tables.groupby(
        by=["departmentId"],
        sort=False
    )["salary"].max().to_frame().reset_index()
    output = pd.DataFrame({"Department": [], "Employee": [], "Salary": []})
    for row in range(highest_by_group.shape[0]):
        filter_tables = tables[(tables["departmentId"]==highest_by_group.loc[row, "departmentId"]) & (tables["salary"]==highest_by_group.loc[row, "salary"])]
        filter_tables = filter_tables.loc[:, ["name_y", "name_x", "salary"]]
        filter_tables.rename(
            columns={"name_y": "Department", "name_x": "Employee", "salary": "Salary"},
            inplace=True
        )
        output = pd.concat([output, filter_tables], ignore_index=True)
    return output
