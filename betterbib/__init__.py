# -*- coding: utf-8 -*-
#
from betterbib.bibtex import pybtex_to_dict, \
        pybtex_to_bibtex_string, read_bibtex
from betterbib.crossref import Crossref
from betterbib.dictdiffer import adds_info
from betterbib.mathscinet import MathSciNet
from betterbib.progress_bar import ProgressBar
from betterbib.source import Source
from betterbib.zb_mref import ZentralblattMref

__all__ = [
    'bibtex',
    'crossref',
    'dictdiffer',
    'mathscinet',
    'progress_bar',
    'source',
    'zb_mref'
    ]

__name__ = 'betterbib'
__version__ = '0.4.0'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/betterbib'
