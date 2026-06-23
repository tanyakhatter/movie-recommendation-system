import pickle
import streamlit as st
import requests
import time

st.set_page_config(page_title="Movie Recommender", layout="wide")


@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    # 3 baar try karega
    for _ in range(3):
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()

            data = response.json()
            poster_path = data.get("poster_path")

            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path

        except Exception:
            time.sleep(1)

    # Agar poster na mile
    return "https://via.placeholder.com/300x450?text=No+Poster"


def recommend(movie):
    index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_names.append(
            movies.iloc[i[0]].title
        )

        recommended_movie_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movie_names, recommended_movie_posters


# ---------------- UI ---------------- #

st.title("🎬 Movie Recommender System")

movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button("Show Recommendation"):

    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])