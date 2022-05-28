import pandas as pd
import streamlit as st
import requests
import pickle

from PIL import Image
image = Image.open('movie.jpg')

st.image(image, width=800)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=7a9ff98411ab8e5971f53c22d342c9af&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[0:11]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.markdown("<h1 style='text-align: center; color: black;'>Movie Recommender System</h1>", unsafe_allow_html=True)


movies = pickle.load(open('movie_lst.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


movie_lst = movies['title'].values
select_movie = st.selectbox(
            'Select movie: (Recommendation will be based on this selection)',  movie_lst)

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = recommend(select_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.markdown(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.markdown(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.markdown(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.markdown(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.markdown(recommended_movie_names[4])

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[5])
        st.markdown(recommended_movie_names[5])
    with col2:
        st.image(recommended_movie_posters[6])
        st.markdown(recommended_movie_names[6])
    with col3:
        st.image(recommended_movie_posters[7])
        st.markdown(recommended_movie_names[7])
    with col4:
        st.image(recommended_movie_posters[8])
        st.markdown(recommended_movie_names[8])
    with col5:
        st.image(recommended_movie_posters[9])
        st.markdown(recommended_movie_names[9])

