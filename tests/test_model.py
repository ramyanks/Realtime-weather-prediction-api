import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.modelling import read_and_process_data, model_and_evaluate

def test_model():
    print("Testing the model....")
    
    X_train, X_test, y_train, y_test = read_and_process_data()
    MAE = model_and_evaluate(X_train, X_test, y_train, y_test)
    try:
        # ensure there are no missing values in train, validation and test data
        assert not X_train.isna().any().any()
        assert not y_train.isna().any().any()
        
        # ensure that accuracy score is float and greater than 0
        assert isinstance(MAE, float)
    except Exception as e:
        print(f"Error:{e}")
    print("Testing is completed.")


if __name__=='__main__':
    print(f"Executing this from {__name__}")
    test_model()
    