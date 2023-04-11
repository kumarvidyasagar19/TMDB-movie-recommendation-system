import streamlit as st
import pandas as pd
import pickle

st.title('ML based movie recommender system')

movies_dict=pickle.load(open('df_movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similar.pkl','rb'))
selected_movie_name = st.selectbox('Search movie name',movies['title'].values)

import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=26f9d6065a20d731da9840df481b6c61&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original"+data['poster_path']




def recommend(mov):
    try:
      index = movies[movies['title'] == mov].index[0]
      distances = list(enumerate(similarity[index]))
      distances = sorted(distances,reverse=True,key = lambda x: x[1])
      recommended_movie = []
      recommended_movie_poster = []
      for i in distances[0:5]:
          recommended_movie.append(movies.iloc[i[0]].title)
          movie_id = movies.iloc[i[0]].movie_id
          recommended_movie_poster.append(fetch_poster(movie_id))
      return recommended_movie,recommended_movie_poster
    except:
      return 'movie not found! please try next movie..','not found'




if st.button('Recommended'):
    name,poster = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 =st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])


