# **Movie Recommendation System**

This is a **content-based recommendation system** that suggests movies based on a user's input preferences. The system uses **TF-IDF vectorization** and **cosine similarity** to compare the user's description with a dataset of movies and returns the most relevant matches.

---

## **1. Dataset**
- The dataset (`data.csv`) contains a list of movies along with their descriptions.
- Ensure the dataset is available in the same directory as the script.
- The dataset can be downloaded from Kaggle TMDB 5000 Movie Dataset

---

## **2. Setup Instructions**
### **Prerequisites**
Make sure you have Python installed on your system. You can install dependencies using:

```bash
pip install -r requirements.txt
```

### **Creating a Virtual Environment (Optional)**
For best practice, you may want to run this project in a virtual environment:
```bash
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
pip install -r requirements.txt
```

---

## **3. Running the Application**
You can run the application in two ways:

### **Option 1: Using Streamlit**
Launch the web-based interface:
```bash
streamlit run app.py
```

### **Option 2: Using Command Line**
If you prefer running the recommendation system from the terminal, you can use:

```bash
python recommend.py "I love thrilling action movies set in space, with a comedic twist."
```

---

## **4. How It Works**
- The user inputs a movie preference.
- The system converts the text input into a vector using **TF-IDF**.
- It compares the user input to movie descriptions using **cosine similarity**.
- The top **5 most similar** movies are displayed along with their posters and links.

---

## **5. Sample Query & Output**
### **User Input:**
```plaintext
"I like action movies set in space with some comedy."
```

### **Expected Output:**
| Movie Title            | Poster | Link |
|------------------------|--------|------|
| Guardians of the Galaxy | ![Poster](https://image.tmdb.org/t/p/w500/sample1.jpg) | [View](https://www.themoviedb.org/movie/118340) |
| Star Wars: A New Hope  | ![Poster](https://image.tmdb.org/t/p/w500/sample2.jpg) | [View](https://www.themoviedb.org/movie/11) |
| Thor: Ragnarok        | ![Poster](https://image.tmdb.org/t/p/w500/sample3.jpg) | [View](https://www.themoviedb.org/movie/284053) |

---

## **6. Dependencies**
All dependencies are listed in `requirements.txt`. Ensure you install them before running the project.

```plaintext
streamlit
scikit-learn
pandas
numpy
requests
pickle
```

---

## **7. Credits**
This project utilizes **The Movie Database (TMDb) API** to fetch movie posters and links.
