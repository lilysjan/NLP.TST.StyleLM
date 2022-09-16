import pickle
import pandas as pd


def read_raw(path_script, script_name, extention='txt', encoding="utf-8"):
    """
    Input
        - (str) path_script: 스크립트의 경로
        - (str) script_name: 읽을 대본의 파일 명
        - (str) extention: 파일의 확장자로, 파일 저장시 hwp를 "txt"로 주로 저장.
        - (str) encoding: 파일 읽을 때 필요한 encoding 종류로 한글 대본이기에 utf-8을 기본으로 사용
    
    Output
        - (pd.Series) content: 대본 파일을 읽고 각 문장들을 element로 가지는 Series
    """
    with open(f"{path_script}/{script_name}.{extention}", encoding=encoding) as f:
       contents = f.readlines()
       return pd.Series(contents)


def process_raw(script: pd.Series):
    """
    Input
        - (pd.Series) script: 대본을 문장단위로 저장한 Series
    
    Output
        - (pd.Series) 전처리가 끝난 Series
    """

    # 필요없는 element들 제거
    script = _filter_sentence(script)

    return script


def save_scripts(path_script, file_name, script):
    """
    Input
        - (str) path_script: 스크립트의 경로
        - (str) file_name: 저장할 정리된 대본의 파일명
        - (TBD) scripot: 저장할 대본
    """
    with open(f"{path_script}/{file_name}.pkl", 'wb') as f:
        pickle.dump(script, f)


def _filter_sentence(sen: pd.Series):
    sen = sen.str.replace('\n', '')
    sen = sen.str.replace('\t', '')
    sen[sen==' '] = ''
    sen.drop_duplicates(inplace=True)
    sen.reset_index(drop=True, inplace=True)
    return sen
