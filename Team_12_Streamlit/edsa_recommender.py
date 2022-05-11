"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model
from pathlib import Path

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')


# Read Markdown files
def read_markdown(file):
		return Path(file).read_text()

# Navigation
BROWSE_PAGES = {
		'Home Page': "Home",
		'Data Insights': "Data insights",
		"Recommender System": "Recommender System",
        "Model": "Model",
        "Solution Overview": "Solution Overview",
	}

# App declaration
def main():
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Home","Data Insights","Recommender System","Model","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.radio("Choose Option", page_options)
    
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                    ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('First Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                    
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                            We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                #try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                        top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                #except:
                    #st.error("Oops! Looks like this algorithm does't work.\
                           # We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    
    if page_selection == 'Home':
        st.title("WAZE! RECOMMENDER")
        st.write("#### Developed by Weza Analytics")
        st.markdown("----")
        st.write("## Welcome to WAZE!")
        col1, col2 = st.columns([2,3])
        with col1:
            st.image("resources/imgs/lionheart-poster.jpg")
        with col2:
            st.markdown(read_markdown('resources/markdowns/intro.md'))
    
    if page_selection == "Data Insights":
        st.title('Exploratory Data Analysis')
        st.markdown("---")
        st.markdown(read_markdown('resources/markdowns/eda.md'))
        st.image('resources/imgs/ratings_chart.png',use_column_width=True)
        st.markdown(
            """
            The distributions above shows ratings of a movie per category, ratings from 0.5 stars to 5.0 stars, the ratings were distributed in this way:

            Movies rated 0.5 stars made up 1.6%, followed by low ratings of 1.0 to 2.5 stars which received less than 7%.

            Ratings between 3 and 5 stars, excluding the 4 star rating, have a percentage between 8.8% - 19.6%

            The rating with the highest percentage was 4 stars with 26.6%.
            """
        )
        st.image('resources/imgs/trends_chart.png',use_column_width=True)
        st.write("From the image above, it can be observed that the two most popular movie categories are Comedy and Drama.")
        st.image('resources/imgs/word_cloud.png',use_column_width=True)
        st.markdown(
            """
            The wordcloud above indicates a number of popular movie directions based on the number of movies they have directed. We can observe that the most popular movie director as Woody Allen, Luc Paul Maurice Besson and Stephen King.

            Woody Allen is known as one of the most famous figures in modern cinema, the father of the intellectual comedy. Woody Allen has been nominated 24 times and won four Academy Awards : three for Best Original Screenplay and one for Best Director (Annie Hall).

            Luc Paul Maurice Besson is a French film director, screenwriter, and producer. He directed or produced the films Subway, The Big Blue, and La Femme Nikita. Besson is associated with the Cinéma du look.

            Stephen Edwin King is an American novelist and short-story writer whose books were credited with reviving the genre of horror fiction in the late 20th century He also directed his own movie in 1986 called Maximum Overdrive. Also as an author, there has been atleast 60 films made thus far from Stephen King's books
            """
        )
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Describe your winning approach on this page")


    if page_selection == "Model":
        st.title("Modelling our Data")
        st.write("## Content based Filtering")
        st.markdown(
            """
            The content-based approach uses additional information about users and/or items. 
            This filtering method uses item features to recommend other items similar to what the user likes and also based on their previous actions or explicit feedback. 
            The main idea of content-based methods is to try to build a model, based on the available “features”, that explain the observed user-item interactions. 
            Such a model helps us in making new predictions for a user pretty easily, with just a look at the profile of this user and based on its information, to determine relevant movies to suggest.
            """
        )

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


if __name__ == '__main__':
    main()
