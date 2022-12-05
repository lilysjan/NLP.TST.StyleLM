import os
import collections
import pandas as pd

from src.structure.Movie import Movie
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
        if len(dat) <= 1:
            continue
        res.append(Movie(fname, dat))

    meta.to_csv(f'data/meta_{get_today()}.csv', encoding='utf-8')
    return res


@section_decorator
def _get_script_to_str_ratio(data):
    print("Scripts over strings \n ")
    for dat in data:
        print(f"{dat.fname} : {len(dat.raw)}/ {len(''.join(dat.raw))}")


@section_decorator
def _get_quality_ratio(data):
    print("TXT 변환 성능 검사")
    availables = [i for i, dat in enumerate(data) if dat.file_qual == 1]
    print(f"{len(availables)} Available data over {len(data)}")


@section_decorator
def _get_prep_type_ratio(data):
    print("전처리 유형 분포")
    res = collections.defaultdict(int)
    for dat in data:
        res[dat.prep_type] += 1

    for k, v in res.items():
        print(f"Type {k} : {v}/{len(data)}")


@section_decorator
def _get_prep_quality_ratio(data):
    _enc = {1: '사용가능', 0: '사용불가능'}
    print("전처리 성능 분포")
    res = collections.defaultdict(int)
    for dat in data:
        res[_enc[dat.prep_qual]] += 1

    for k, v in res.items():
        print(f"{k} : {v}/{len(data)}")


def sensor_dat(data):
    _get_script_to_str_ratio(data)
    _get_quality_ratio(data)
    _get_prep_type_ratio(data)
    _get_prep_quality_ratio(data)


if __name__ == '__main__':
    os.chdir('../../../')
