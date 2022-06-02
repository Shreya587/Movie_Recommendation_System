# Movie_Recommendation_System 
A simple content based movie recommendation system using sorting techniques and ML algorithms to recommend users the type of movie they want to see. 
This project was built for Microsoft Engage'22 Program in which we have to Demonstrate through their app the different kinds of algorithms that a web-streaming app (like Netflix) or an audio-streaming app (like Spotify) may use for their Recommendation Engine within a span of 4 weeks.


# Features Implemented 

- Simple UI using streamlit
- Recommend top 10 movies 
- Sorted movies based on cosine similarity
- Checking similarity based on overview, cast, crew, keywords and genre
- Fetching poster from TMDB API

# How to run the project?

1. Clone this repository to your local machine and download this [similarity.pkl](https://drive.google.com/file/d/1kmjXkx1jekDu1UgOaoeoK8y4jB5o2RjW/view?usp=sharing)  file after cloning(This is a large file that's why it is not uploaded in the repository.).

2. Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt

3. Get your API key from https://www.themoviedb.org/. OR It is provieded not need(if you want you can create it)
   Do not worry my api key is given so no need to install it.
   
4. `Data_preprocessing.ipynb` is the notebook of data processing.

5. `main.py` is the main Python file of Streamlit Web-Application. To run app, write following command in CMD or use any IDE.
  ```
  streamlit run main.py
  ```
6. Yayy!! That's it.

# Tech Stack Used
- Jupyter Notebook
- Python
- TMDB API
- Streamlit
- Pandas

# Description of this project is given in this Presentation
(https://docs.google.com/presentation/d/1hvRSaBnXB4jHpSS6kYKoYczK0oHRgEJb/edit?usp=sharing&ouid=104082539040410466551&rtpof=true&sd=true)

# Dataset Sources

[The Movie Dataset from kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)
