# Task-3-NourNebli
#  AI Movie Recommendation System

##  Project Overview

This project is a simple Artificial Intelligence Recommendation System developed as part of the DecodeLabs Artificial Intelligence Internship (Project 3).

The system recommends movies based on user preferences using **Cosine Similarity**, a common technique used in recommendation systems.

Instead of randomly suggesting movies, the system analyzes the similarity between a user's favorite genres and the genres associated with each movie.

---

## Objectives

* Collect user preferences.
* Represent movies using feature vectors.
* Calculate similarity scores.
* Recommend the most relevant movies.
* Visualize recommendation results.
* Export recommendations to a CSV file.

---

## 🛠 Technologies Used

* Python 3
* Pandas
* Scikit-Learn
* Matplotlib

---

##  Dataset

A small movie dataset is created manually inside the program.

Each movie contains one or more genres:

| Movie            | Genres                             |
| ---------------- | ---------------------------------- |
| Interstellar     | Science Fiction, Adventure, Drama  |
| The Matrix       | Action, Science Fiction            |
| Avengers Endgame | Action, Adventure, Science Fiction |
| Titanic          | Romance, Drama                     |
| John Wick        | Action, Thriller                   |
| Inception        | Action, Science Fiction, Thriller  |
| Avatar           | Action, Science Fiction, Adventure |
| The Dark Knight  | Action, Drama, Thriller            |
| Doctor Strange   | Action, Science Fiction, Adventure |

---

##  How It Works

### Step 1: User Input

The user enters preferred genres.

Example:

```text
Action, Science Fiction
```

---

### Step 2: User Vector Creation

The system converts the preferences into a binary vector.

Example:

```text
[1, 1, 0, 0, 0, 0]
```

Where:

* Action = 1
* Science Fiction = 1
* Adventure = 0
* Drama = 0
* Romance = 0
* Thriller = 0

---

### Step 3: Movie Feature Matrix

Each movie is represented using binary values.

Example:

| Movie  | Action | Science Fiction | Adventure | Drama | Romance | Thriller |
| ------ | ------ | --------------- | --------- | ----- | ------- | -------- |
| Matrix | 1      | 1               | 0         | 0     | 0       | 0        |

---

### Step 4: Cosine Similarity

The similarity between the user vector and each movie vector is calculated using:

Cosine Similarity = (A · B) / (||A|| × ||B||)

A higher score means the movie better matches the user's interests.

---

### Step 5: Ranking

Movies are sorted from highest similarity score to lowest similarity score.

The Top 5 movies are displayed.

---

### Step 6: Visualization

A bar chart is generated to visualize the recommendation scores.

---

### Step 7: Export Results

All recommendations are saved into:

```text
recommendations.csv
```

---

##  Installation

Install the required libraries:

```bash
pip install pandas scikit-learn matplotlib
```

---

##  Running the Project

Execute:

```bash
python project3.py
```

---

## 📊 Example Output

User Input:

```text
Action, Science Fiction
```

Output:

```text
TOP MOVIE RECOMMENDATIONS

1. The Matrix (Score = 1.000)
2. Doctor Strange (Score = 0.816)
3. Avengers Endgame (Score = 0.816)
4. Inception (Score = 0.816)
5. Avatar (Score = 0.816)
```

---

## 🧠 AI Concepts Used

* Recommendation Systems
* Content-Based Filtering
* Feature Engineering
* Similarity Measurement
* Cosine Similarity
* Data Representation

---

##  Future Improvements

* Add thousands of movies from a real dataset.
* Allow users to rate movies.
* Implement collaborative filtering.
* Build a graphical user interface (GUI).
* Create a web version using Flask or Django.
* Store movie data in a database.

---

##  Conclusion

This project demonstrates the fundamentals of recommendation systems in Artificial Intelligence. By using Cosine Similarity, the system successfully identifies movies that match user preferences and provides personalized recommendations.

The project serves as an introduction to content-based recommendation techniques used by modern platforms such as streaming and e-commerce services.
