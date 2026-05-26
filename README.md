## Project Structure

```bash id="mz7qfx"
ML-Flask-project-Recommendation-systems/
│
├── templates/
│   └── index.html             # Frontend webpage
│
├── app.py                     # Flask backend application
├── File_recommender.ipynb     # Jupyter Notebook for ML model training
├── Zomato_reduced.csv         # Dataset used for recommendations
└── README.md                  # Project documentation
```

---

## Development Workflow

### Jupyter Notebook

The Machine Learning model was developed and tested inside Jupyter Notebook using:

* Data preprocessing
* Feature engineering
* Feature scaling
* KNN model training
* Recommendation testing

### Flask Application

The trained recommendation logic was integrated into a Flask web application to provide recommendations through a web interface.

---

## Technologies Used

* Python
* Flask
* Jupyter Notebook
* Pandas
* NumPy
* Scikit-Learn
* HTML/CSS
