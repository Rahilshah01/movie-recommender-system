# 🎬 Movie Recommender System (End-to-End NLP App)

## 📌 Project Overview
This is a content-based recommendation engine that suggests movies based on a user's preferences. By analyzing metadata—genres, keywords, cast, and crew—the system calculates similarity scores to deliver personalized recommendations.

## 🚀 Live Demo
**[Click here to view the live app!]([https://your-app-name.streamlit.app/](https://movie-recommender-system-rahilshah.streamlit.app/))**

## 🛠️ Tech Stack
* **Machine Learning:** NLP, Cosine Similarity, CountVectorizer
* **Frontend:** Streamlit
* **API Integration:** TMDB API (The Movie Database)
* **Data Engineering:** Pandas, Pickle

## 🔍 How it Works
1. **Vectorization:** Movie tags are converted into 5,000-dimensional vectors using `CountVectorizer`.
2. **Similarity Engine:** The app uses **Cosine Similarity** to find the shortest "distance" between movie vectors.
3. **Real-Time API:** When a movie is suggested, the app calls the TMDB API to fetch high-resolution posters for a Netflix-style UI.

## 📊 Deployment
The application is deployed on **Streamlit Community Cloud**, connected directly to this GitHub repository for continuous integration.
