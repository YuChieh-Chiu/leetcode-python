import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - check if the dataframe is empty or not
    - if empty, return empty dataframe; if not empty, do the following
    - sort the dataframe by `recordDate`
    - use `df.diff()` to calculate the delta date between row and last row
    - filter the rows fullfill the following conditions 
        - the value in `recordDate` column == 1 (delta date == 1)
        - the value in `temperature` column > 0 (temperature is higher)
    """
    if weather.empty:
        return weather[["id"]]
    else:
        weather.sort_values(
            by=["recordDate"],
            ascending=True,
            inplace=True
        )
        diff_df = weather.diff()
        condition = (diff_df.loc[:,"recordDate"] == "1 days") & (diff_df.loc[:,"temperature"] > 0)
        weather = weather.loc[diff_df[condition].index.tolist(), ["id"]]
        return weather
