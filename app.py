import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle 
from sklearn.preprocessing import RobustScaler as RS
import pandas as pd
scaler = RS()
n=0
app = Flask(__name__)
model = pickle.load(open('modelfin.pkl', 'rb'))
data = pd.read_csv(r'C:\Users\Sarvesh\pop.csv')
X = data.drop(['popularity','ratio','categoryId','Unnamed: 0'],axis=1)
Y=data['popularity'] 
from sklearn.model_selection import train_test_split as tts
X_train, X_test, Y_train, Y_test = tts(X,Y, test_size = 0.20, shuffle=True)
scaler.fit(X_train)
@app.route('/')
def home():
    return render_template('yt.htm')
@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    f=scaler.transform(final_features)
    prediction = model.predict(f)
    if(prediction[0]==0):
        output="High"
    if(prediction[0]==2):
        output="Medium"
    if(prediction[0]==1):
        output="Low"
    return render_template('result.htm', prediction_text='Predicted Popularity: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
