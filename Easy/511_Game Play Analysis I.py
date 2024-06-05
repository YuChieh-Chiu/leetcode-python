import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - we only need to know `first login date` of each player
    - the only columns we concerned are `player_id` and `event_date`
    - sort by `event_date` and drop_duplicates by `player_id`
    - filter the columns and rename it
    """
    activity.sort_values(
        by="event_date",
        ascending=True,
        inplace=True
    )
    activity.drop_duplicates(
        subset=["player_id"],
        keep="first",
        inplace=True
    )
    activity = activity.loc[:, ["player_id", "event_date"]].rename(columns={
        "event_date": "first_login"
    })
    return activity
