import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - note that `id` should be sort in ascending order and `id` may have a `hole`
    - add a new column `times` to record the consecutive times of num
    - in column `times`
        - if id in row == id in previous row + 1, then
            - if num in row == num in previous row, times in row == times in previous row + 1
            - if not, times == 1
        - if not, times == 1
    - filter the num with times == 3 (num with times > 3 is already be filtered when times == 3)
    """
    times = []
    logs.sort_values(
        by="id",
        ascending=True,
        inplace=True
    )
    logs.reset_index(inplace=True, drop=True)
    for row in range(logs.shape[0]):
        if row == 0:
            times.append(1)
        else:
            if logs.loc[row-1, "id"]+1 == logs.loc[row, "id"]:
                if logs.loc[row-1, "num"] == logs.loc[row, "num"]:
                    times.append(times[-1]+1)
                else:
                    times.append(1)
            else:
                times.append(1)
    logs["times"] = times
    logs_3 = logs[logs["times"]==3]
    consecutive_nums = pd.DataFrame({
        "ConsecutiveNums": list(set(logs_3["num"]))
    })
    return consecutive_nums
