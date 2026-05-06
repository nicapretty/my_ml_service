import joblib
import pandas as pd
from pathlib import Path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
MODEL_DIR = BASE_DIR / "research"

train_mode = joblib.load(MODEL_DIR / "train_mode.joblib")
encoders = joblib.load(MODEL_DIR / "encoders.joblib")
rf_model = joblib.load(MODEL_DIR / "random_forest.joblib")
et_model = joblib.load(MODEL_DIR / "extra_trees.joblib")


@api_view(["POST"])
def predict_income(request):
    try:
        data = request.data
        
        input_data = pd.DataFrame([data])
        
        input_data = input_data.fillna(train_mode)
        
        for column in ['workclass', 'education', 'marital-status',
                      'occupation', 'relationship', 'race',
                      'sex', 'native-country']:
            if column in input_data.columns:
                input_data[column] = encoders[column].transform(input_data[column])
        
        rf_prediction = rf_model.predict(input_data)[0]
        et_prediction = et_model.predict(input_data)[0]
        
        return Response({
            "random_forest_prediction": rf_prediction,
            "extra_trees_prediction": et_prediction
        }, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_400_BAD_REQUEST)
