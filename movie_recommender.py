import pandas as pd

def recommend_movies(genre):
    movies_df = pd.read_csv('movies.csv')
    ratings_df = pd.read_csv('ratings.csv')
    # фильтруем фильмы по жанру
    genre_movies = movies_df[movies_df['genres'].str.contains(genre)]
    # соединяем фильмы с рейтингами
    movie_ratings = pd.merge(genre_movies, ratings_df, on='movieId')
    # считаем средний рейтинг для каждого фильма
    avg_ratings = movie_ratings.groupby('title')['rating'].mean().reset_index()
    # сортируем фильмы по среднему рейтингу
    sorted_movies = avg_ratings.sort_values('rating', ascending=False)
    return sorted_movies.head(10)

if __name__ == '__main__':
    genre = input('Enter a movie genre (e.g. Action, Comedy, Drama): ')
    recommended_movies = recommend_movies(genre)
    print(f'Top 10 {genre} movies recommended for you:\n{recommended_movies}')
