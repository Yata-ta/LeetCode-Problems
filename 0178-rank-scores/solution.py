import pandas as pd
import numpy as np

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    

    df = scores.copy()

    df = df.sort_values("score", axis = 0, ascending = False)
    is_diff_score = (df["score"] != df["score"].shift(1)).fillna(True)
    df["rank"] = is_diff_score.cumsum()  

    return df[["score", "rank"]]


