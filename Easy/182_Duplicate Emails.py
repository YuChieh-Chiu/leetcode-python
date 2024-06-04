import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - value_counts() 算出每個 email 的個數
    - .loc[] 篩選出其中大於1的
    - 回傳 index 並組成 df 
    - return
    """
    emails = person["email"].value_counts().loc[lambda x: x>1].index
    output_df = pd.DataFrame({
        "Email": emails.to_list()
    })
    return output_df
