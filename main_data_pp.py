from src.utils.data import data_process as dp


def main():
    movies = dp.get_txt()
    movies_gen = dp.get_genre_movies(movies)
    dp.sensor_dat(movies)
    print()


if __name__ == '__main__':
    main()
