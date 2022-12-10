import os
import collections
import numpy as np
import pandas as pd

from src.structure.Movie import Movie
from src.utils.log._format import get_today, section_decorator


def _get_meta(ver):
    res = pd.read_csv(f'data/meta_{ver}.csv', encoding='utf-8', index_col=0)
    res['배역'] = res['배역'].astype(str).apply(lambda x: x.split('#'))
    return res


def _open_file(dir, encoding):
    with open(dir, encoding=encoding) as f:
        dat = f.readlines()
    f.close()
    return dat


def get_txt(ver=None):
    ver = get_today() if ver is None else ver
    meta = _get_meta(ver)
    # meta = meta.fillna('#NAN')

    res = []
    flist = os.listdir('data/txt/')
    for fname in flist:
        try:
            dat = _open_file(f"data/txt/{fname}", 'utf-8')
        except UnicodeDecodeError as err:
            dat = _open_file(f"data/txt/{fname}", 'cp949')
            meta.loc[meta['원본파일명']==fname, 'encoding'] = 'cp949'
        if len(dat) <= 1:
            continue
        raw_name = ''.join(fname.split('.')[:-1])
        meta_f = meta.loc[meta['원본파일명'] == raw_name].reset_index(drop=True).to_dict()
        meta_f = collections.defaultdict(None, **{k: v[0] for k, v in meta_f.items()})
        res.append(Movie(meta_f, dat))

    meta.to_csv(f'data/meta_{get_today()}.csv', encoding='utf-8')
    return res


@section_decorator
def _get_script_to_str_ratio(data):
    print("Scripts over strings \n ")
    for dat in data:
        print(f"{dat.fname} : {len(dat.scripts)}/ {len(dat.raw)}")


@section_decorator
def _get_script_component_ratio(data):
    print("대사, 행동지문, 인물명 비율")
    for dat in data:
        print(f"{dat.fname} : 대사 {dat.get_line_num()} / 행동지문 {dat.get_act_num()} / 인물명 {dat.get_char_num()}")


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


def get_genre_scripts(movies, ver=None):
    ver = get_today() if ver is None else ver
    meta = _get_meta(ver)
    meta['장르'] = meta['장르'].fillna('미상')
    gens = np.unique(meta['장르'])
    res = collections.defaultdict(str)

    for gen in gens:
        movie_gen = ['.'.join(i.get_lines()) for i in movies if i.genre == gen]
        res[gen] = '.'.join(movie_gen)
    return res


def _get_genre_len(data):
    gen = get_genre_scripts(data)

    for k, v in gen.items():
        print(k, len(v))


def sensor_dat(data):
    _get_script_to_str_ratio(data)
    _get_script_component_ratio(data)
    _get_quality_ratio(data)
    _get_prep_type_ratio(data)
    _get_prep_quality_ratio(data)
    _get_genre_len(data)


if __name__ == '__main__':
    os.chdir('../../../')
