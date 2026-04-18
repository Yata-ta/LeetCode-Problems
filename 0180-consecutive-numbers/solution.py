import pandas as pd
import numpy as np

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    
    df = logs.copy()

    prev_2_num = 0
    prev_num = 0
    consecutive_nums = []
    for i, num in enumerate(df["num"]):

        if i == 0:
            prev_2_num = num
            continue
        if i == 1:
            prev_num = num
            continue
       
        if num == prev_num and num == prev_2_num:
            consecutive_nums.append(num)

        prev_2_num = prev_num
        prev_num = num

    return pd.DataFrame(np.unique(np.array(consecutive_nums)), columns = ["ConsecutiveNums"])


