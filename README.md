# 🎬 Movie Recommendation System

A machine learning-powered movie recommendation system that suggests similar movies using content-based filtering and cosine similarity on movie metadata from the TMDB dataset.
## 🌟 Features

- Recommend Top 5 Similar Movies
- Content-Based Filtering
- Cosine Similarity-Based Recommendation Engine
- Interactive Streamlit Web Application
- Movie Poster Integration using TMDB API
- Fast and User-Friendly Interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- TMDB API
- Pickle

---

## 📊 Dataset

This project uses the TMDB 5000 Movies Dataset containing:

- Movie Titles
- Genres
- Keywords
- Cast Information
- Crew Information
- Movie Overviews

---

## ⚙️ How It Works

1. Movie metadata is collected from the TMDB dataset.
2. Genres, keywords, cast, directors, and overviews are combined into a single feature.
3. Text data is transformed into vectors using CountVectorizer.
4. Cosine Similarity is calculated between movie vectors.
5. The system recommends the most similar movies based on similarity scores.

---

## 📁 Project Structure

```text
movie-recommendation-system/
│
├── .gitignore
├── Screenshot 2026-06-23 011213.png
├── main.py
├── movie_list.pkl
├── requirements.txt
├── similarity.pkl
└── README.md
```

---

## 📸 Application Screenshot



![Movie Recommender App](Screenshot%202026-06-23%20011213.png)
---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/tanyakhatter/movie-recommendation-system.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd movie-recommendation-system
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run main.py
```

### 5️⃣ Open in Browser

```text
http://localhost:8501
```

---

## 🎯 Example

**Selected Movie**

```text
Avatar
```

**Recommended Movies**

```text
John Carter
Guardians of the Galaxy
Aliens
Titan A.E.
Star Trek
```

---

## 🔮 Future Improvements

- Hybrid Recommendation System
- User Authentication
- Search Autocomplete
- Movie Ratings & Reviews
- Streamlit Cloud Deployment

---

## 🌐 Live Demo

https://movie-recommendation-system-trseyvdettjkkyq8v3bybd.streamlit.app/



## 👩‍💻 Author

**Tanya Khatter**

GitHub: https://github.com/tanyakhatter

LinkedIn: https://www.linkedin.com/in/tanya-khatter-26989733b

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
