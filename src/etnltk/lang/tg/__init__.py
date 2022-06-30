from functools import cached_property
from typing import Callable, List, Optional

from etnltk.common.doc import (
    Document,
    Word
)

from .stop_words import STOP_WORDS

from .punctuation import ASSCII_PUNCT, ETHIOPIC_PUNCT, NO_ABBREV_ASSCII_ETHIOPIC_PUNCTS

from .preprocessing import (
    remove_links,
    remove_tags,
    remove_emojis,
    remove_email,
    remove_special_characters,
    remove_digits,
    remove_english_chars,
    remove_arabic_chars,
    remove_chinese_chars,
    remove_whitespaces,
    remove_ethiopic_digits,
    remove_ethiopic_punct,
    remove_non_ethiopic,
    remove_punct,
    remove_stopwords
)
from .normalizer import (
   normalize_punct,
   normalize_shortened,
   normalize_char,
   normalize_labialized
)

DEFAULT_PIPELINE: List[Callable] = [
    remove_links,
    remove_tags,
    remove_emojis,
    remove_email,
    remove_special_characters,
    remove_digits,
    remove_ethiopic_digits,
    # TODO: text = remove_ethiopic_dates(text)
    remove_english_chars,
    remove_arabic_chars,
    remove_chinese_chars
]


def clean_tigrigna(text: str,  abbrev=False, pipeline: Optional[List[Callable]] = None):
    """ Returns a preprocessed copy of *text*,
    by executing a series of data preprocessing steps defined in pipeline.

    Args:
        text (str): _description_
        abbrev (bool, optional): _description_. Defaults to False.
        pipeline (Optional[List[Callable]], optional): _description_. Defaults to None.

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    if text is None:
        raise ValueError("clean_amharic: `text` can't be `None`")

    if pipeline is None:
        pipeline = DEFAULT_PIPELINE

    for pipe_func in pipeline:
        text = pipe_func(text)

    text = normalize_punct(text)
    if not abbrev:
        text = normalize_shortened(text)
    
    text = normalize_char(text)
    
    text = remove_punct(text, abbrev=abbrev)
    
    text = remove_whitespaces(text)

    if isinstance(text, str):
        processed_text = text
    else:
        processed_text = " ".join(text)
    return processed_text

def normalize(text: str) -> str:
    """The function for all default amharic normalization. 
    Nomalizes an input text by executing a series of nomalization functions specified in the argument.
    
    Labialized Character Normalzation such as ሞልቱዋል to ሞልቷል
    Short Form Expansion such as ጠ/ሚ to ጠቅላይ ሚኒስተር.
    Punctuation Normalization such as :: to ።.
    Character Level Normalization such as ጸሀይ and ፀሐይ.
    """
    
    if text is None:
        raise ValueError("normalize: `text` can't be `None`")
   
    normalized_text = normalize_labialized(text)
    normalized_text = normalize_shortened(normalized_text)
    normalized_text = normalize_punct(normalized_text)
    return normalize_char(normalized_text)