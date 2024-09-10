
# Popularity Prediction of YouTube Videos

This project focuses on predicting the popularity of YouTube videos using a machine learning approach. It is based on the research paper [Popularity Prediction of YouTube Videos](https://ieeexplore.ieee.org/document/9734220), which analyzes factors affecting the popularity of YouTube content.

## Project Overview

The aim of the project is to develop a model that can predict the popularity of YouTube videos based on various attributes, such as views, likes, comments, and other metadata available in the `popularity.csv` dataset.

Key features of this project include:
- Data cleaning and preprocessing.
- Feature extraction and selection.
- Model training using machine learning techniques.
- Model evaluation and prediction accuracy.
- Web application interface using `Flask`.

## Project Structure

- **popularity.csv**: Dataset containing YouTube video statistics and attributes.
- **YT_Final.ipynb**: Jupyter notebook with the main code for data analysis, model training, and evaluation.
- **app.py**: A Flask-based web application that provides a user interface to predict YouTube video popularity based on input attributes.
- **static/**: Folder containing static resources (e.g., CSS, JavaScript).
- **templates/**: Folder containing HTML templates for rendering the web application's frontend.
- **README.md**: This file, providing an overview of the project and usage instructions.

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/harshitha0923/PopularityPredictionOfYouTubeVideos.git
   cd PopularityPredictionOfYouTubeVideos
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have Jupyter Notebook installed to run the notebook file (`YT_Final.ipynb`):
   ```bash
   pip install notebook
   ```

4. To run the web application, install Flask if you haven't already:
   ```bash
   pip install Flask
   ```

## Usage

### Running the Jupyter Notebook

1. Open `YT_Final.ipynb` using Jupyter Notebook:
   ```bash
   jupyter notebook YT_Final.ipynb
   ```

2. Run the notebook cells to see the data preprocessing steps, model training, and evaluation.

### Running the Web Application

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to access the interface for predicting YouTube video popularity.

## Data

The dataset `popularity.csv` contains YouTube video statistics that were collected and used for model training. This data includes:
- Video metadata such as views, likes, and comments.
- Other attributes affecting video popularity, as analyzed in the research paper.

## Model

The project uses machine learning algorithms such as Random Forest and XGBoost to predict the popularity of YouTube videos. The Jupyter notebook contains details on model selection, hyperparameter tuning, and evaluation metrics.

## Contributors

This project was developed as part of the research work published in the paper ["Popularity Prediction of YouTube Videos"](https://ieeexplore.ieee.org/document/9734220).
