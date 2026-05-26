from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Load dataset
df = pd.read_csv('Zomato_reduced.csv')

# Data Preprocessing
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')
df.dropna(subset=['rate'], inplace=True)
df = df.groupby(['name', 'location', 'cuisines', 'url']).agg({'rate': 'mean', 'votes': 'sum'}).reset_index()

# Encode cuisines for ML
label_encoder = LabelEncoder()
df['cuisine_encoded'] = label_encoder.fit_transform(df['cuisines'])

# Train KNN Model
knn = NearestNeighbors(n_neighbors=5, metric='euclidean')
knn.fit(df[['cuisine_encoded', 'rate', 'votes']])

def recommend_restaurant(preferred_cuisine, top_n=5):
    if preferred_cuisine not in label_encoder.classes_:
        return [{"name": "No recommendations available", "location": "-", "rate": "-", "url": "#"}]
    
    cuisine_code = label_encoder.transform([preferred_cuisine])[0]
    distances, indices = knn.kneighbors([[cuisine_code, df['rate'].mean(), df['votes'].mean()]])

    recommendations = df.iloc[indices[0]][['name', 'location', 'rate', 'url']].to_dict(orient='records')
    return recommendations if recommendations else [{"name": "No recommendations available", "location": "-", "rate": "-", "url": "#"}]

@app.route(
def home():
    return render_template('index.html')

@app.route('/get_cuisines', methods=['GET'])
def get_cuisines():
    cuisines = sorted(df['cuisines'].unique().tolist())
    return jsonify(cuisines)

@app.route('/recommend', methods=['POST'])
def recommend():
    preferred_cuisine = request.form['cuisine']
    recommendations = recommend_restaurant(preferred_cuisine)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
