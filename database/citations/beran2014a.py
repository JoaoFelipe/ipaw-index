# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import beran2014a
from ..work.y2016 import michaelis2016a

DB(Citation(
    michaelis2016a, beran2014a, ref="",
    contexts=[

    ],
))
