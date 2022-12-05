import os
from src.structure.Movie import Movie
import pandas as pd

from src.utils.log._format import get_today, section_decorator


def _get_meta(ver):
    return pd.read_csv(f'data/meta_{ver}.csv', encoding='utf-8', index_col=0)


def _open_file(dir, encoding):
    with open(dir, encoding=encoding) as f:
        dat = f.readlines()
    f.close()
    return dat


def get_txt(ver=None):
    ver = get_today() if ver is None else ver
    meta = _get_meta(ver)

    res = []
    flist = os.listdir('data/txt/')
    for fname in flist:
        try:
            dat = _open_file(f"data/txt/{fname}", 'utf-8')
        except UnicodeDecodeError as err:
            dat = _open_file(f"data/txt/{fname}", 'cp949')

            meta.loc[fname, 'encoding'] = 'cp949'
        res.append(Movie(fname, dat))

    meta.to_csv(f'data/meta_{get_today()}.csv', encoding='utf-8')
    return res


@section_decorator
def _get_script_to_str_ratio(data):
    print("Scripts over strings \n ")
    for dat in data:
        print(f"{dat.fname} : {len(dat.scripts)} / {len(dat.raw)}")


def sensor_dat(data):
    _get_script_to_str_ratio(data)


if __name__ == '__main__':
    os.chdir('../../../')
