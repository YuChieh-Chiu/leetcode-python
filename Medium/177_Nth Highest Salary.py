import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """
    thought:
    - because N may less than 1, if N < 1, nth_highest_salary == None
    - get the unique value in `salary` by set()
    - if length of set() < N, nth_highest_salary == None
    - if length of set() >= N, sort `list(set())` descending and get the nth element (index N-1)
    """
    col_name = f"getNthHighestSalary({N})"
    nth_highest_salary = pd.DataFrame({col_name: []})
    salary_set = set(employee["salary"])
    if (len(salary_set) < N) | (N < 1):
        nth_highest_salary[col_name] = [None]
        return nth_highest_salary
    salary_set = sorted(list(salary_set), reverse=True)
    nth_highest_salary[col_name] = [salary_set[N-1]]
    return nth_highest_salary
