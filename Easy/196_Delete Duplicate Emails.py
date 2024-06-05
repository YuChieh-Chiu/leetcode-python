import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    """
    thought:
    - we need to sort the dataframe by `id` first
    - and then drop duplicates and keep first one
    - we can use df.drop_duplicates()
    - note: return None
    """
    person.sort_values(
        by=["id"],
        ascending=True,
        inplace=True
    )
    person.drop_duplicates(
        subset=["email"],
        keep="first",
        inplace=True
    )
