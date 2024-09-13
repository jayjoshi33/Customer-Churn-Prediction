from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Load the entire pipeline
pipeline = joblib.load('rf_model.pkl')  # Ensure this points to the correct pipeline file

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get input data from POST request
    # Convert the input data to a DataFrame
    input_df = pd.DataFrame(data['input'])
    # Make a prediction using the pipeline
    prediction = pipeline.predict(input_df)  # Ensure you're calling predict on the pipeline
    
    return jsonify({'prediction': int(prediction[0])})  # Return the prediction as JSON

if __name__ == '__main__':
    app.run(debug=True)
