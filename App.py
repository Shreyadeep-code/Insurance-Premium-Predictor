from fastapi import FastAPI

from fastapi.responses import JSONResponse

from model.predict import predict_output,MODEL_VERSION,model
from schema.prediction_response import PredictionResponse

from schema.user_input import UserInput

app=FastAPI()









# human readable
@app.get('/')
def home():
    return ({'message':'Insurance Premium Prediction API'})

# Machine readable
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version':MODEL_VERSION,
        'model_loaded':'true'
    }


@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data:UserInput):
    
    input_df={
        'bmi':data.bmi,
        'Age_group':data.Age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'occupation':data.occupation,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation,
        'city_tier':data.city_tier
    }


    try:
        prediction=predict_output(input_df)

        return JSONResponse(status_code=200,content={'predicted_category':prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
