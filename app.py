import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=bd51fe3d80b7fce6825f401cd4863905&language=en-US'.format(movie_id))
    data=response.json()
    #st.text(data)
    #st.text('https://api.themoviedb.org/3/movie/{}?api_key=bd51fe3d80b7fce6825f401cd4863905&language=en-US'.format(movie_id))
    return "https://image.tmdb.org/t/p/original"+data['poster_path']

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies=[]
    recommended_movies_posters=[]

    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        #Fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
    'Which movie would you like to search?',
    movies['title'].values)

if st.button('Recommend'):
    names, posters=recommend(selected_movie_name)
    col1, col2, col3,col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])