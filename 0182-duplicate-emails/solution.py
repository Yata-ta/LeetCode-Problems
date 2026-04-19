import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    
    person_df = person.copy()

    mask = person_df["email"].duplicated()
    duplicates_df = person_df.loc[mask]
    return duplicates_df.rename(columns={"email":"Email"})[["Email"]].drop_duplicates()




