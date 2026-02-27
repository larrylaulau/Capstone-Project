from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

def train_rf_model(df, features):
    # 1. Chronological Split (80/20)
    split_index = int(len(df) * 0.8)
    X = df[features]
    y = df['Target']
    
    X_train, X_test = X.iloc[:split_index], X.iloc[split_index:]
    y_train, y_test = y.iloc[:split_index], y.iloc[split_index:]
    
    # 2. Train Model
    model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # 3. Predict & Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    print(f"🚀 Model Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred))
    
    return model, X_test, y_test, y_pred
