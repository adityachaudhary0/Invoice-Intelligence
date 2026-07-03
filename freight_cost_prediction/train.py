import joblib
from pathlib import Path
from freight_cost_prediction.data_preprocessing import load_vender_invoice_data,prepare_features,split_data
from freight_cost_prediction.model_evalutation import train_linear_regression,train_Decision_tree,train_Random_Forest,train_SVM,evaluate_model

def main():
    db_path="/home/adi/Documents/project/data/inventory.db"
    model_dir=Path("models")
    model_dir.mkdir(exist_ok=True)

    #load data
    df=load_vender_invoice_data(db_path)

    #prepare data
    X,Y=prepare_features(df)
    x_train,x_test,y_train,y_test=split_data(X,Y)

    #Train models
    lr_model=train_linear_regression(x_train,y_train)
    dt_model=train_Decision_tree(x_train,y_train)
    rf_model=train_Random_Forest(x_train,y_train)
    svm_model=train_SVM(x_train,y_train)

    #Evalute model
    result=[]
    result.append(evaluate_model(lr_model,x_test,y_test,"Linear Regression"))
    result.append(evaluate_model(dt_model,x_test,y_test,"Decision Tree"))
    result.append(evaluate_model(rf_model,x_test,y_test,"Random Forest"))
    result.append(evaluate_model(svm_model,x_test,y_test,"SVM"))
    
    #best model
    best_model_info=min(result,key=lambda x:x["mean_absolute_error"])
    best_model_name=best_model_info["model_name"]
    best_model={
        "Linear Regression":lr_model,
        "Decision Tree":dt_model,
        "Random Forest":rf_model,
        "SVM":svm_model
    }[best_model_name]

    #save best model
    model_path=model_dir/"predict freight_model.pkl"
    joblib.dump(best_model,model_path)
    print(f"best model saved: {best_model_name}")
    print("best model save at : ",model_path)


if __name__=="__main__":
    main()

