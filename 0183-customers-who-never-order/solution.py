import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    customers_df = customers.copy()
    orders_df = orders.copy()

    total = customers.merge(orders_df, left_on="id", right_on="customerId", suffixes = ["_order", ""])
    mask = customers["id"].isin(total["customerId"]) == False

    return customers_df.loc[mask].rename(columns={"name":"Customers"})[["Customers"]]


