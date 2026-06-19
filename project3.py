# ==========================================================
# PROJECT 3 : AI RECOMMENDATION SYSTEM
# DecodeLabs Internship
#
# Features:
# - User preferences input
# - Cosine Similarity
# - Movie recommendations
# - Top 5 recommendations
# - Score visualization
# - CSV export
# ==========================================================

# ==========================================================
# IMPORT LIBRARIES
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================================
# MOVIE DATABASE
# ==========================================================

movies = {
    "Movie": [
        "Interstellar",
        "The Matrix",
        "Avengers Endgame",
        "Titanic",
        "John Wick",
        "Inception",
        "The Notebook",
        "Avatar",
        "The Dark Knight",
        "Doctor Strange"
    ],

    "Action": [0,1,1,0,1,1,0,1,1,1],

    "Science Fiction": [1,1,1,0,0,1,0,1,0,1],

    "Adventure": [1,0,1,0,0,0,0,1,0,1],

    "Drama": [1,0,0,1,0,0,1,0,1,0],

    "Romance": [0,0,0,1,0,0,1,0,0,0],

    "Thriller": [0,0,0,0,1,1,0,0,1,0]
}

# Create DataFrame
df = pd.DataFrame(movies)

# ==========================================================
# AVAILABLE GENRES
# ==========================================================

genres = [
    "Action",
    "Science Fiction",
    "Adventure",
    "Drama",
    "Romance",
    "Thriller"
]

print("\n===================================")
print("MOVIE RECOMMENDATION SYSTEM")
print("===================================\n")

print("Available Genres:\n")

for genre in genres:
    print("-", genre)

# ==========================================================
# USER INPUT
# ==========================================================

user_input = input(
    "\nEnter your favorite genres separated by commas:\n"
)

selected_genres = [
    genre.strip()
    for genre in user_input.split(",")
]

print("\nYour Preferences:")
print(selected_genres)

# ==========================================================
# CREATE USER VECTOR
# ==========================================================

user_vector = []

for genre in genres:

    if genre in selected_genres:
        user_vector.append(1)

    else:
        user_vector.append(0)

print("\nUser Vector:")
print(user_vector)

# ==========================================================
# MOVIE FEATURE MATRIX
# ==========================================================

movie_matrix = df[genres]

# ==========================================================
# COSINE SIMILARITY
# ==========================================================

similarity_scores = cosine_similarity(
    [user_vector],
    movie_matrix
)

# Add scores to dataframe
df["Similarity Score"] = similarity_scores[0]

# ==========================================================
# SORT MOVIES
# ==========================================================

recommendations = df.sort_values(
    by="Similarity Score",
    ascending=False
)

# ==========================================================
# DISPLAY RECOMMENDATIONS
# ==========================================================

print("\n===================================")
print("TOP MOVIE RECOMMENDATIONS")
print("===================================\n")

top5 = recommendations.head(5)

rank = 1

for index, row in top5.iterrows():

    print(
        f"{rank}. {row['Movie']} "
        f"(Score = {row['Similarity Score']:.3f})"
    )

    rank += 1

# ==========================================================
# SAVE RESULTS
# ==========================================================

recommendations.to_csv(
    "recommendations.csv",
    index=False
)

print(
    "\nRecommendations saved to recommendations.csv"
)

# ==========================================================
# VISUALIZATION
# ==========================================================

plt.figure(figsize=(10, 5))

plt.bar(
    top5["Movie"],
    top5["Similarity Score"]
)

plt.title(
    "Top 5 Recommended Movies"
)

plt.xlabel(
    "Movies"
)

plt.ylabel(
    "Similarity Score"
)

plt.xticks(rotation=20)

plt.tight_layout()

plt.show()

# ==========================================================
# END
# ==========================================================

print("\nSystem Finished Successfully.")