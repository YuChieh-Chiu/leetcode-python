import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    """
    thought:
    - sort the column `score` in descending order (rule 1)
    - the rank of the first row should be `1`, and the rank of next row should depend on its value (rule 2&3)
        - just note that rank is consecutive
    """
    ranks = []
    current_rank = 1
    scores.sort_values(
        by="score",
        ascending=False,
        inplace=True
    )
    scores.reset_index(inplace=True, drop=True)
    for row in range(scores.shape[0]):
        if row == 0:
            ranks.append(1)
            continue
        if scores.loc[row-1, "score"] != scores.loc[row, "score"]:
            current_rank += 1
        ranks.append(current_rank)
    scores["rank"] = ranks
    return scores.loc[:, ["score", "rank"]]
