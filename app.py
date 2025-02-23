import streamlit as st
import pickle
import requests
from sklearn.metrics.pairwise import cosine_similarity

movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
vectorizer = pickle.load(open('vectorizer.pkl','rb'))
vector = pickle.load(open('vector.pkl','rb'))

#Fetch poster function
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c99861f911415b91de843545bee557d8&language=en-US".format(movie_id)
    response = requests.get(url)
    data = response.json()
    poster_path = data['poster_path']
    return "https://image.tmdb.org/t/p/w500/"+poster_path

#Get movie URL
def get_movie_url(movie_id):
    return f"https://www.themoviedb.org/movie/{movie_id}"

#Recommendation function
def recommend(user_input):
    # Build user input's vector and calculate the similarity
    user_vector = vectorizer.transform([user_input]).toarray()
    user_similarity = cosine_similarity(user_vector,vector).flatten()
   
    # Get top 5 movies that match the user's preferences
    top_indices = user_similarity.argsort()[-5:][::-1]


    recommended_movies = []
    recommend_poster = []
    recommend_links = []

    for index in top_indices:
        movies_id = movies.iloc[index].id # Fetches the entire row at position index and retrieves the movie id
        recommend_poster.append(fetch_poster(movies_id)) 
        recommended_movies.append(movies['title'].iloc[index])
        recommend_links.append(get_movie_url(movies_id))
        print(movies['title'].iloc[index])
    return recommended_movies, recommend_poster, recommend_links


st.header("Movie Recommendation System")
user_input = st.text_input("Enter your movie preference:")
st.write("You entered:", user_input)

if st.button("Show Recommend"):
    movie_names, movie_posters, movie_links = recommend(user_input)
    cols = st.columns(5)
    for i in range(len(movie_names)):
        with cols[i]:
            # Styling movie title using HTML + CSS
            st.markdown(
                 f"""
                    <div style="text-align: center; font-size: 14px; font-weight: bold; margin-bottom: 5px;">
                        <a href="{movie_links[i]}" target="_blank" style="text-decoration: none; color: #3498db;">
                            {movie_names[i]}
                        </a>
                    </div>
                    """,
                unsafe_allow_html=True
            )
            st.image(movie_posters[i], use_column_width=True)