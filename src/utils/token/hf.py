from transformers import PreTrainedTokenizerFast
from transformers import PreTrainedTokenizer

from transformers import AutoModel, AutoTokenizer


def get_pretrained(tname: str, **kwargs):
    return AutoTokenizer.from_pretrained(tname, kwargs)
