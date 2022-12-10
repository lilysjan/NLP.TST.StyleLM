import re
from src.utils.data import data_process as dp
from src.utils.token.tk import TokenHandler

import config


def load_tk(alg, flist):
    return TokenHandler(alg, flist)


def save_strings(dat: dict):
    for k, v in dat.items():
        k = re.sub('\W+', '_', k)
        with open(f'data/processed/tk_input/{k}.txt', 'a', encoding='utf-8') as f:
            f.write(v)


def main():
    movies = dp.get_txt()
    scripts_gen = dp.get_genre_scripts(movies)

    save_strings(scripts_gen)

    tk = load_tk(config.algorithm, config.train_genre)

    tk.train_tokenizer()
    dp.sensor_dat(movies)

    print()


if __name__ == '__main__':
    main()
