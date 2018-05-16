# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import markovic2016b

from ..work.y2016 import markovic2016a
from ..work.y2018 import batlajery2018a

DB(Citation(
    markovic2016b, markovic2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    batlajery2018a, markovic2016a, ref="",
    contexts=[

    ],
))
