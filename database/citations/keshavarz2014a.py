# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import keshavarz2014a
from ..work.y2016 import huynh2016b
from ..work.y2016 import lang2016a
from ..work.y2017 import dividino2017a

DB(Citation(
    dividino2017a, keshavarz2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huynh2016b, keshavarz2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lang2016a, keshavarz2014a, ref="",
    contexts=[

    ],
))
