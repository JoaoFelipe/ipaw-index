# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import graves2010a
from ..work.y2011 import wang2011a
from ..work.y2011 import cruz2011b
from ..work.y2011 import altınta2011a

DB(Citation(
    wang2011a, graves2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cruz2011b, graves2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    altınta2011a, graves2010a, ref="",
    contexts=[

    ],
))
