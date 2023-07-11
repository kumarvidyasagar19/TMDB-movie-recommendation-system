# ML Vectorization-Based Movie Recommender System
This repository contains a movie recommender system that utilizes vectorization techniques to suggest related movies based on user input. The system is trained on a dataset of 5000 movies and provides 5 movie recommendations for a given movie name. The recommender system is implemented as a web application using Streamlit.

## Project Overview
The goal of this project is to create a movie recommender system that leverages vectorization techniques to analyze movie features and provide personalized recommendations to users. The system is trained on a dataset of 5000 movies, which includes information such as movie titles, genres, and user ratings. By inputting a movie name, users can receive recommendations for similar movies based on the vectorized features.

## Key Features
* Data preprocessing: The dataset of 5000 movies is cleaned and processed to handle missing values, outliers, and inconsistencies.
* Feature extraction: Relevant features such as movie genres, actors, and directors are extracted from the dataset to capture important movie attributes.
* Vectorization: The textual features of movies are transformed into numerical vectors using vectorization techniques such as TF-IDF (Term Frequency-Inverse Document Frequency) and Word2Vec.
* Similarity calculation: The cosine similarity measure is used to calculate the similarity between the vectorized features of movies, enabling the system to recommend similar movies based on user input.
* Streamlit web app: The recommender system is deployed as a web application using Streamlit, allowing users to interactively input a movie name and receive 5 related movie recommendations.

## Installation
To run the movie recommender system locally, follow these steps:

1. Clone the repository:
```sh
# Copy code git clone
https://github.com/kumarvidyasagar19/TMDB-movie-recommendation-system
```

2. Install the required dependencies:
```sh
# Copy code
pip install -r requirements.txt
```

3. Run the Streamlit app:
```sh
# Copy code
streamlit run app.py
```

5. Access the web app in your browser at-  http://localhost:8501.

![web app desktop](https://github.com/kumarvidyasagar19/TMDB-movie-recommendation-system/assets/107400026/9db51774-4b70-4668-9774-74b02628112b)

## Usage
Once the Streamlit app is running, you can input the name of a movie in the provided text box. The system will generate 5 movie recommendations based on the input movie's features and similarities to other movies in the dataset. The recommendations will be displayed on the web app along with their respective details such as title, genre, and rating.

### Contributors
* Vidyasagar Kumar: kvidya.ece@email.com
