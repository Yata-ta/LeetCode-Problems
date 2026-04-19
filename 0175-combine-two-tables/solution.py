import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    person_df = person.copy()
    address_df = address.copy()

    mode = "merge"

    if mode != "merge":

        person_df["city"] = np.nan
        person_df["state"] = np.nan

        for i, row in person_df.iterrows():
            city_data = address_df[address_df["personId"] == row["personId"]]  

            if not city_data.empty:
                person_df.at[i, "city"] = city_data.iloc[0]["city"]
                person_df.at[i, "state"] = city_data.iloc[0]["state"]

        return person_df[["firstName", "lastName", "city", "state"]]



    person_df = person_df.merge(address_df[['personId', 'city', 'state']], on="personId", how = "left")


    return person_df[["firstName", "lastName", "city", "state"]]


