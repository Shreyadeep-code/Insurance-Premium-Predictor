import pickle
import pandas as pd


with open('model/ins.pkl','rb') as f:
    model=pickle.load(f)

MODEL_VERSION='1.0.0'
class_labels=model.classes_.tolist()

def predict_output(user_input : dict):

    input_df=pd.DataFrame([user_input])

    predicted_class=model.predict(input_df)[0]

    probabilities=model.predict_proba(input_df)[0]
    confidence=max(probabilities)

    class_probabilities=dict(zip(class_labels,map(lambda p:round(p,4),probabilities)))
     
    return{
        'predicted_category':predicted_class,
        'confidence_score':confidence,
        'other_probabilities':class_probabilities
        
    }