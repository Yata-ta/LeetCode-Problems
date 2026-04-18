import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    
    df = employee.copy()
    
    df = pd.unique(df.sort_values("salary", axis=0, ascending=False)["salary"])
    
    if len(df) <= 1:
        return pd.DataFrame([np.nan], columns = ["SecondHighestSalary"])
       
    
    min_index = 1
    
    second = pd.DataFrame([df[min_index]], columns = ["SecondHighestSalary"])
    
    
    return second
