# https://huggingface.co/course/chapter6/8?fw=pt#acquiring-a-corpus
# https://www.freecodecamp.org/news/train-algorithms-from-scratch-with-hugging-face/
""""
1. Normalizeation
2. Pre-tokenization
3. Model
4. Post-processing
"""
from tokenizers import Tokenizer
from tokenizers.models import BPE, Unigram, WordLevel, WordPiece
from tokenizers.trainers import BpeTrainer, WordLevelTrainer, WordPieceTrainer, UnigramTrainer

from tokenizers.pre_tokenizers import Whitespace
from tokenizers import pre_tokenizers

from config import spl_tokens, unk_token


class TokenHandler(object):
    def __init__(self, alg, flist, pret='default'):
        self.tokenizer, self.trainer = prepare_tokenizer_trainer(alg)
        self.flist = flist
        self._make_inp()
        self.raw = 'data/processed/tk_input/tmp.txt'
        # Step 1 : Normalization

        # Step 2 : Pre-tokenization
        self.prepare_pret(pret=pret)

    def prepare_pret(self, pret):
        if pret == 'bert':
            self.tokenizer.pre_tokenizer = pre_tokenizers.BertPreTokenizer()
        else:
            self.tokenizer.pre_tokenizer = Whitespace()

    def train_tokenizer(self):
        self.tokenizer.train(self.raw, self.trainer)

    def _make_inp(self):
        tmp = ''
        for fname in self.flist:
            with open(f'data/processed/tk_input/{fname}.txt', 'a', encoding='utf-8') as f:
                dat = f.readlines()
            if type(dat) == str:
                tmp += dat
            elif type(dat) == list:
                tmp += ''.join(dat)
            else:
                assert False

        with open(f'data/processed/tk_input/tmp.txt', 'a', encoding='utf-8') as f:
            f.write(tmp)


def prepare_tokenizer_trainer(alg):
    """
    Prepares the tokenizer and trainer with unknown & special tokens.
    """
    if alg == 'BPE':
        tokenizer = Tokenizer(BPE(unk_token=unk_token))
        trainer = BpeTrainer(special_tokens=spl_tokens)
    elif alg == 'UNI':
        tokenizer = Tokenizer(Unigram())
        trainer = UnigramTrainer(unk_token=unk_token, special_tokens=spl_tokens)
    elif alg == 'WPC':
        tokenizer = Tokenizer(WordPiece(unk_token=unk_token))
        trainer = WordPieceTrainer(special_tokens=spl_tokens)
    else:
        tokenizer = Tokenizer(WordLevel(unk_token=unk_token))
        trainer = WordLevelTrainer(special_tokens=spl_tokens)
    return tokenizer, trainer


