import os
import pickle
import numpy as np
import pandas as pd
from tabulate import tabulate


from src.utils.log._format import section_decorator, get_today


@section_decorator
def _get_raw_list(*args, **kwargs):
    print("Raw file Stats")
    print("- Extension")
    flist = os.listdir('data/raw/')
    exts = list(map(lambda x: x.split('.')[-1], flist))
    exts_type, exts_cnt = np.unique(exts, return_counts=True)
    for ext_type, ext_cnt in zip(exts_type, exts_cnt):
        print(f"{ext_type} : {ext_cnt}")


@section_decorator
def _get_txt_list(*args, **kwargs):
    print("Txt file Stats")
    flist = os.listdir('data/txt/')
    exts = list(map(lambda x: ''.join(x.split('.')[:-1]), flist))
    print("# of files : ", len(exts))


@section_decorator
def _export_summary(*args, **kwargs):
    print("Current DB Stats")
    print("See more details at exported files")
    txt_list = os.listdir('data/txt/')
    txts = list(map(lambda x: ''.join(x.split('.')[:-1]), txt_list))
    # txts = pd.DataFrame(['Y']*len(txts), index=txts, columns=['Txt'])

    flist = os.listdir('data/raw/')
    # fname = list(map(lambda x: ''.join(x.split('.')[:-1]), flist))
    # raws = list(map(lambda x: ''.join(x.split('.')[:-1]), raw_list))
    # raws = pd.DataFrame(['Y']*len(raws), index=raws, columns=['Raw'])

    tab = pd.read_csv('data/processed/movie_df.csv', encoding='utf-8', index_col=0)

    # tab = raws.join(txts, how='outer')
    tab.loc[tab['원본파일명'].isin(flist), 'Raw'] = 'Y'
    tab.loc[tab['원본파일명'].apply(lambda x: ''.join(x.split('.')[:-1])).isin(txts), 'Txt'] = 'Y'
    tab['Raw'].fillna('N', inplace=True)
    tab['Txt'].fillna('N', inplace=True)
    tab['encoding'] = ['utf-8'] * len(tab)

    tab.to_csv(f'data/meta_{get_today()}.csv', encoding='utf-8')
    tab_pr = tabulate(tab, headers='keys', tablefmt='psql', showindex=True)
    print('# of txt: ', len(tab)-tab['Txt'].isna().sum())
    print('# of all:', len(tab))
    # print(tab_pr)


def run():
    _get_raw_list()
    _get_txt_list()
    _export_summary()


if __name__ == '__main__':
    os.chdir('../../../')
    _export_summary()
