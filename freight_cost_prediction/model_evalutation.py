from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn import svm
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

def train_linear_regression(x_train,y_train):
    model1=LinearRegression()
    model1.fit(x_train,y_train)
    return model1
def train_Decision_tree(x_train,y_train):
    model2=DecisionTreeRegressor(random_state=42)
    model2.fit(x_train,y_train)
    return model2
def train_Random_Forest(x_train,y_train):
    model3=RandomForestRegressor(random_state=42)
    model3.fit(x_train,y_train)
    return model3
def train_SVM(x_train,y_train):
    model4=svm.SVR()
    model4.fit(x_train,y_train)
    return model4

def evaluate_model(model,x_test,y_test,model_name)->dict:
    predict=model.predict(x_test)
    mse=mean_squared_error(y_test,predict)
    mae=mean_absolute_error(y_test,predict)
    r2=r2_score(y_test,predict)
    d={
        "model_name":model_name,
        "mean_square_error":mse,
        "mean_absolute_error":mae,
        "r2 score":r2
    }
    print(d)
    return d