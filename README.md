# Movie Recommendation System

A content-based Movie Recommendation System built using Python, Scikit-learn, TF-IDF Vectorization, Cosine Similarity, and Streamlit.

The application allows users to select a movie from a dropdown and receive recommendations based on content similarity.

## Features

- Select a movie from a dropdown list.
- Generate the top 5 similar movie recommendations.
- Use TF-IDF to extract movie content features.
- Calculate similarity between movies using Cosine Similarity.
- Interactive web interface built with Streamlit.

## Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation
- **Scikit-learn** – TF-IDF Vectorization and Cosine Similarity
- **Streamlit** – Web application interface
- **Pickle** – Loading serialized movie data and similarity matrix

## Recommendation Approach

This project uses a Content-Based Filtering approach.

### 1. TF-IDF Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) converts movie textual information into numerical feature vectors.

Configuration:

```python
```

### 2. Cosine Similarity

Cosine Similarity measures the similarity between movie feature vectors.

Movies with higher similarity scores are considered more relevant recommendations.

### 3. Recommendation Generation

The application:
1. Identifies the selected movie.
2. Retrieves its similarity scores against other movies.
3. Sorts movies by similarity score in descending order.
4. Excludes the selected movie itself.
5. Returns the top 5 recommendations.

## Project Structure

```text
MovieRecommendation/
│
├── movie_recommend.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3.9+
- pip

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd MovieRecommendation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Mac/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run movie_recommend.py
```

The application will be available at:

http://localhost:8501

## Requirements

```text
streamlit
pandas
scikit-learn
```

## Deployment

The application can be deployed using Render.

**Render configuration:**

| Configuration | Value |
|---|---|
| Environment | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run movie_recommend.py --server.port $PORT --server.address 0.0.0.0` |

Ensure the required pickle files are available in the deployed application.

## Future Enhancements

- Display movie posters.
- Include movie genres and ratings.
- Display similarity scores.
- Improve recommendations using additional movie metadata.
- Explore hybrid recommendation techniques.

## Author

Developed as a machine learning and recommendation system project using Python and Streamlit.
