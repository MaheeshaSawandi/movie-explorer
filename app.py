import pandas as pd
import streamlit as st

movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

movie_ratings = pd.merge(movies_df, ratings_df, on='movieId')
movie_stats = movie_ratings.groupby('movieId')[['rating']].mean()
movie_stats = movie_stats.merge(movies_df, on='movieId')

# Sidebar
genre_list = movies_df['genres'].str.split('|').explode('genres').unique()
selected_genre = st.sidebar.selectbox('Choose a genre', genre_list)

# Filter & sort
selected_movies = movie_stats[movie_stats['genres'].str.contains(selected_genre)].sort_values(by='rating',
                                                                                              ascending=False)

# Main content
st.title(f"Top Movies in {selected_genre}")

for row in selected_movies.itertuples():
    st.subheader(row.title)
    st.caption(f"Rating: {row.rating:.2f} ({row.count} reviews)")
    st.text(row.genres)