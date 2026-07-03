from model_evalution import train_xg_boost,evaluate_classifier
import joblib
from data_preproccessing import load_vender_invoice_data,apply_labels,create_invoice_label,split_data,scale_features
FEATURES = ["Invoice_Quantity","Invoice_Dollars","Freight","Total_Item_Quantity","Total_Item_Dollars"]
TARGET = "flag_invoice"
def main():
    #load data
    db_path="/home/adi/Documents/project/data/inventory.db"
    df=load_vender_invoice_data(db_path)
    df=apply_labels(df)
    x_train,x_test,y_train,y_test=split_data(df,FEATURES,TARGET)
    x_train_scalled,x_test_scalled=scale_features(x_train,x_test,"invoice_flagging/models/scaler.pkl")

    model=train_xg_boost(x_train_scalled,y_train)
    evaluate_classifier(model,x_test_scalled,y_test,"Xg_boost")
    joblib.dump(model,"invoice_flagging/models/predict_flag_invoice.pkl")
if __name__=="__main__":
    main()