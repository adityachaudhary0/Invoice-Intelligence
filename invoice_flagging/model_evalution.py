from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,precision_score,recall_score,f1_score
def train_xg_boost(x_train,y_train):
    rf=XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    objective='binary:logistic',
    eval_metric='logloss',
    random_state=42)
    rf.fit(x_train,y_train)
    return rf
def evaluate_classifier(model, X_test, y_test, model_name):
    preds=model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test,preds):.2f}")
    report=classification_report(y_test, preds)
    print(f"\n{model_name} Performance")
    print(f"Accuracy: {accuracy_score(y_test,preds):.2f}")
    print(report)