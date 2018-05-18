# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import ruda2008a

from ..work.y2008 import k2008a

DB(Citation(
    ruda2008a, k2008a, ref="",
    contexts=[

    ],
))
