import pandas as pd
import numpy as np
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee_df = employee.copy()
    
    employee_df = employee_df.merge(employee_df[["id", "salary"]], left_on="managerId", right_on="id", suffixes = ["", "_manager"])


    print(employee_df["salary"] > employee_df["salary_manager"])

    return employee_df.loc[employee_df["salary"] > employee_df["salary_manager"]].rename(columns= {"name":"Employee"})[["Employee"]]
