import operator
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pandas as pd
import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
tf=TfidfVectorizer(max_features=5000,ngram_range=(2,2))
df_recommendation = pickle.load(open("movies.pkl", "rb"))
tf = TfidfVectorizer(max_features=5000, ngram_range=(2,2))
tf_idf_transform = tf.fit_transform(
    df_recommendation['clean_text']
)

similarity = cosine_similarity(tf_idf_transform)

st.title("Movie recommendation system")

options = [d for d in df_recommendation['original_title']]

selected_option = st.selectbox(
    "Select a movie for recommendation",
    options
)

def recommend(item_name, top_n=5):
    ls=[]
    index = df_recommendation[
        df_recommendation['original_title'].str.lower() == item_name.lower()
    ].index[0]

    scores = list(enumerate(similarity[index]))

    scores.sort(key=operator.itemgetter(1), reverse=True)

    top_movies = scores[1:top_n+1]

    for movie_index, score in top_movies:
        print(
            df_recommendation.iloc[movie_index]['original_title'],
            score
        )

        ls.append(df_recommendation.iloc[movie_index]['original_title'])
    return(ls)

if st.button("Recommend"):
    recommendations = recommend(selected_option)

    for movie in recommendations:
        st.write(movie)
