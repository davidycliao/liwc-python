from .dic import read_dic
from .trie import build_trie, search_trie

try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution("liwc").version
except Exception:
    __version__ = None


def load_token_parser(filepath, encoding = "utf-8"):
    """
    Reads a LIWC lexicon from a file in the .dic format, returning a tuple of
    (parse, category_names), where:
    * `parse` is a function from a token to a list of strings (potentially
      empty) of matching categories
    * `category_names` is a list of strings representing all LIWC categories in
      the lexicon
    * `encoding = "utf-8"` can be overwritten by other encoding such as "EUC-JP" for Janpanese. 
    * `load_token_parser()` now can read multiple dictionaries from the distributor such as Dutch_LIWC2015_Dictionary,
    German_LIWC2001_Dictionary, Italian_LIWC2007_Dictionary, Italian_LIWC2007_Dictionary, LIWC2007_English, LIWC2015_English,
    Spanish_LIWC2007_Dictionary as well as Swedish from the user.
    """
    lexicon, category_names = read_dic(filepath, encoding = encoding)
    trie = build_trie(lexicon)

    def parse_token(token):
        for category_name in search_trie(trie, token):
            yield category_name

    return parse_token, category_names
