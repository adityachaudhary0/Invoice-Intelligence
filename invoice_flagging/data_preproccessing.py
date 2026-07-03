import sqlite3
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,MinMaxScaler
import joblib
def load_vender_invoice_data(path):
    conn=sqlite3.connect(path)
    query="""
WITH purchase_aggr AS (
    SELECT
        p.PONumber,
        COUNT(DISTINCT p.Brand) AS Total_Brands,
        SUM(p.Quantity) AS Total_Item_Quantity,
        SUM(p.Dollars) AS Total_Item_Dollars,
        AVG(julianday(p.ReceivingDate) - julianday(p.PODate)) AS Avg_Receiving_Delay
    FROM purchases p
    GROUP BY p.PONumber
)

SELECT
    vi.PONumber,
    vi.Quantity AS Invoice_Quantity,
    vi.Dollars AS Invoice_Dollars,
    vi.Freight,

    julianday(vi.InvoiceDate) - julianday(vi.PODate) AS Days_PO_To_Invoice,

    julianday(vi.PayDate) - julianday(vi.InvoiceDate) AS Days_To_Pay,

    pa.Total_Brands,
    pa.Total_Item_Quantity,
    pa.Total_Item_Dollars,
    pa.Avg_Receiving_Delay

FROM vendor_invoice vi

LEFT JOIN purchase_aggr pa
ON vi.PONumber = pa.PONumber
"""
    df=pd.read_sql_query(query,conn)
    conn.close()
    return df
def create_invoice_label(row):
  if abs(row["Invoice_Dollars"]-row["Total_Item_Dollars"])>5:
    return 1
  if row["Avg_Receiving_Delay"]>10:
    return 1
  return 0
def apply_labels(df):
   df["flag_invoice"]=df.apply(create_invoice_label,axis=1)
   return df
def split_data(df, features, target):
    X=df[features]
    y=df[target]
    return train_test_split(
X, y, test_size=0.2, random_state=42)
def scale_features (X_train, X_test, scaler_path):
    scaler=StandardScaler()
    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.transform(X_test)
    joblib.dump(scaler, scaler_path)
    return X_train_scaled,X_test_scaled
