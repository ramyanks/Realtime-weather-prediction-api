import pandas as pd
import pathlib
from pathlib import Path
import os
import shutil
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
import warnings
warnings.filterwarnings(action='ignore')
import joblib
import json
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def read_and_process_data():
    data_path = pathlib.Path('data', 'DailyWeatherData.csv')
    # print("data path:", data_path)
    data = pd.read_csv(data_path)
        
    #drop date
    data = data.iloc[:,1:]
    # print("Data:", data.head())
    
    #split data into X, y
    X = data.drop(columns='meantemp')
    y = data['meantemp']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    print("Train and test data have been successfully loaded and formatted.")
    return X_train, X_test, y_train, y_test
    
def model_and_evaluate(X_train, X_test, y_train, y_test):
    #modelling
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    MAE = mean_absolute_error(y_test, predictions)
    MAPE = round(mean_absolute_percentage_error(y_test, predictions)*100,2)
    print(f"Error metrics: Mean absolute Error is {MAE} and Mean absolute error percentage is {MAPE}%")
        
    #write predictions
    predictions = pd.DataFrame(predictions, columns=['predicted_mean_temp'])
    # predictions.columns = ["predicted_temp"]
    os.makedirs("outputs", exist_ok=True)
    predictions.to_csv("outputs/predictions.csv", index=False)
    
    #save the model
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, filename="model/model.joblib")
    
    #write error metrics
    metrics = {"Mean absolute Error":MAE, 
               "Mean absolute percentage error":MAPE
               }
    
    os.makedirs("outputs", exist_ok=True)
    
    with open("outputs/metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)
    return MAE

if __name__=="__main__":
    X_train, X_test, y_train, y_test = read_and_process_data()
    MAE = model_and_evaluate(X_train, X_test, y_train, y_test)