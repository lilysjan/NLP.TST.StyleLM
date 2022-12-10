import re
from src.utils.data import data_process as dp


def save_strings(dat: dict):
    for k, v in dat.items():
        k = re.sub('\W+', '_', k)
        with open(f'data/processed/tk_input/{k}.txt', 'a', encoding='utf-8') as f:
            f.write(v)


def main():
    movies = dp.get_txt()
    scripts_gen = dp.get_genre_scripts(movies)
    save_strings(scripts_gen)
    dp.sensor_dat(movies)
    print()


if __name__ == '__main__':
    main()
