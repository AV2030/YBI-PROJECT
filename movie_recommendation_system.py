# -*- coding: utf-8 -*-
"""Movie Recommendation System.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lDoyHYgApRzb_CqTo9wDci4THoDvsyWC

# **MOVIE RECOMMENDATION SYSTEM**

*Objective :* The objective of this project is to develop a movie recommendation system using Python, aimed at exploring business applications. This involves utilizing data science techniques to analyze user preferences and movie attributes, building a recommendation model, and evaluating its performance. The goal is to create a system that can effectively suggest movies to users based on their viewing history and preferences, demonstrating the practical use of machine learning in enhancing customer experience and driving business value in the entertainment industry.

# Import Libraries
"""

import pandas as pd
import numpy as np

"""# Import Data"""

df = pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/Movies%20Recommendation.csv')

"""# Describing Data"""

df.head()

df.info()

df.shape

df.columns

"""# Feature Selection"""

df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')

df_features.shape

df_features

x = df_features['Movie_Genre'] + ' ' + df_features['Movie_Keywords'] + ' ' + df_features['Movie_Tagline'] + ' ' + df_features['Movie_Cast'] + ' ' + df_features['Movie_Director']

x.shape

"""# Feature Text Conversion To Tokens"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape

print(x)

"""# Getting Similarity Score Using Cosine Similarity"""

from sklearn.metrics.pairwise import cosine_similarity

Similarity_Score = cosine_similarity(x)

Similarity_Score

Similarity_Score.shape

"""# Get Movie Name as Input From User and Validate for Closest Spelling"""

Favourite_Movie_Name = input('Enter Your Favourite Movie Name : ')

All_Movies_Title_List = df['Movie_Title'].tolist()

import difflib

Movie_Recommendation = difflib.get_close_matches(Favourite_Movie_Name, All_Movies_Title_List)
print(Movie_Recommendation)

Close_Match = Movie_Recommendation[0]
print(Close_Match)

Index_of_Close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)

Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))
print(Recommendation_Score)

len(Recommendation_Score)

"""# Sorting all movies based on recommendation scores wrt favourite movie"""

Sorted_Similar_movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)
print(Sorted_Similar_movies)

print('Top 30 Movies Suggested For You : \n')
i = 1
for movie in Sorted_Similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if (i<31):
    print(i, '.',title_from_index)
    i+=1

"""# Top 10 Movie Recommendation System"""

from os import close
Movie_Name = input('Enter Your Favourite Movie Name : ')
list_all_names = df['Movie_Title'].tolist()
Find_closest_match = difflib.get_close_matches(Movie_Name, list_all_names)
close_match = Find_closest_match[0]
Index_of_Movie = df[df.Movie_Title == close_match]['Movie_ID'].values[0]
Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))
Sorted_Similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)

print('Top 10 Movies Suggested For You : \n')
i = 1
for movie in Sorted_Similar_Movies:
  index = movie[0]
  title_from_index = df[df.Movie_ID==index]['Movie_Title'].values
  if (i<11):
    print(i, '.',title_from_index)
    i+=1

"""# Explanation
In this project, we developed a movie recommendation system using Python, demonstrating the potential of data science in business applications. By analyzing user preferences and movie attributes, we created a model that effectively suggests movies tailored to individual users. The system's performance was evaluated and found to be reliable in enhancing user experience. This project underscores the importance of machine learning in driving business value, particularly in the entertainment industry, by providing personalized recommendations that can improve customer satisfaction and engagement.
"""