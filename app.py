import streamlit as st
import pickle
import pandas as pd
import requests
movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:6]
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
    'Search for a movie',
    movies['title'].values)

if st.button('Recommend'):
    reccomendations = recommend(selected_movie_name)
    for i in reccomendations:
        st.write(i)
