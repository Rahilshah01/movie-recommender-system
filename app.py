import streamlit as st
import pickle
import pandas as pd
import requests


# Function to fetch poster from TMDB API
def fetch_poster(movie_id):
    api_key = "cb9d3b51d0eafedc4abe50d7f0a9ef3b"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


# Load the data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_posters


# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox('Type or select a movie to get recommendations:', movies['title'].values)

if st.button('Show Recommendation'):
    names, posters = recommend(selected_movie)

    # Display recommendations in columns
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])