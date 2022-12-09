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
    txt_names = list(map(lambda x: ''.join(x.split('.')[:-1]), txt_list))
    txts = pd.DataFrame(['Y']*len(txt_names), index=txt_names, columns=['TXT'])

    raw_list = os.listdir('data/raw/')
    raw_names = list(map(lambda x: ''.join(x.split('.')[:-1]), raw_list))
    raws = pd.DataFrame(['Y']*len(raw_names), index=raw_names, columns=['RAW'])

    file_status = raws.join(txts, how='outer')
    file_status.fillna('N', inplace=True)
    file_status.index.name = '원본파일명'
    file_status.reset_index(inplace=True)

    tab = pd.read_csv('data/processed/movie_df.csv', encoding='utf-8', index_col=0)
    tab['Extension'] = tab['원본파일명'].apply(lambda x: ''.join(x.split('.')[-1]))
    tab['원본파일명'] = tab['원본파일명'].apply(lambda x: ''.join(x.split('.')[:-1]))

    tab = tab.join(file_status.set_index('원본파일명'), on='원본파일명', how='outer')
    tab.reset_index(inplace=True, drop=True)
    tab['encoding'] = ['utf-8'] * len(tab)

    tab.to_csv(f'data/meta_{get_today()}.csv', encoding='utf-8')
    tab_pr = tabulate(tab, headers='keys', tablefmt='psql', showindex=True)
    print('# of txt: ', len(tab)-tab['TXT'].isna().sum())
    print('# of all:', len(tab))
    # print(tab_pr)


def run():
    _get_raw_list()
    _get_txt_list()
    _export_summary()


if __name__ == '__main__':
    os.chdir('../../../')
    _export_summary()
