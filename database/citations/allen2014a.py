# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import coe2014a

from ..work.y2014 import allen2014a
from ..work.y2014 import coe2014b

DB(Citation(
    coe2014a, allen2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    coe2014b, allen2014a, ref="",
    contexts=[

    ],
))
