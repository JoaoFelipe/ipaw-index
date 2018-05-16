# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import gammack2016a
from ..work.y2018 import pérez2018a

DB(Citation(
    pérez2018a, gammack2016a, ref="",
    contexts=[

    ],
))
