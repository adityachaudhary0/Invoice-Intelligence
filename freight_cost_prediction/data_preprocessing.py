import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
def load_vender_invoice_data(path):
    conn=sqlite3.connect(path)
    tables=pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'",conn)
    vendor_df=pd.read_sql_query("select * from vendor_invoice",conn)
    conn.close()
    return vendor_df
def prepare_features(vendor_df:pd.DataFrame):
    vendor_df = vendor_df.copy()
    vendor_df["Freight_per_unit"] = vendor_df["Freight"] / vendor_df["Quantity"]
    X = vendor_df[["Quantity", "Dollars"]]
    Y = vendor_df["Freight"]
    return X, Y
def split_data(x,y):
    x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.2, random_state=42)
    return x_train,x_test,y_train,y_test

