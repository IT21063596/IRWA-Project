import pickle
import streamlit as st
import requests


# Function to load the custom font
def load_custom_font():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
            body {
                font-family: 'Arial', sans-serif;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Call the function to load the custom font using st.cache_data
st.cache_data(func=load_custom_font)()

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path

    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

# Set the header with an image
st.image('img2.png', use_column_width=True)

st.header("Movie Recommendation")


# Main content
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox(
    'Type or select a movie for us to recommend you similar movies',
    
    movie_list
)
st.sidebar.text("")
st.sidebar.text("")

# Center the "Show recommendations" button
st.write(
    """
    <style>
    .centered-button button {
        display: block;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add an empty space for spacing
st.sidebar.text("")

# Center the "Show recommendation" button
if st.button('Show my recommendations', key='centered-button'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    with col1:
        st.image(recommended_movies_poster[0])
        st.text(recommended_movies_name[0])
        
    with col2:
        st.image(recommended_movies_poster[1])
        st.text(recommended_movies_name[1])
        
    with col3:
        st.image(recommended_movies_poster[2])
        st.text(recommended_movies_name[2])

    with col4:
        st.image(recommended_movies_poster[3])
        st.text(recommended_movies_name[3])
        
    with col5:
        st.image(recommended_movies_poster[4])
        st.text(recommended_movies_name[4])
        
    with col6:
        st.image(recommended_movies_poster[5])
        st.text(recommended_movies_name[5])
        
