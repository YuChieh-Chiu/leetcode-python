import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - get the unique value in `salary` by set()
    - if length of set() <= 1, second_highest_salary == None
    - if length of set() > 1, sort `list(set())` descending and get the second element
    """
    second_highest_salary = pd.DataFrame({"SecondHighestSalary": []})
    salary_set = set(employee["salary"])
    if len(salary_set) <= 1:
        second_highest_salary["SecondHighestSalary"] = [None]
        return second_highest_salary
    salary_set = sorted(list(salary_set), reverse=True)
    second_highest_salary["SecondHighestSalary"] = [salary_set[1]]
    return second_highest_salary
