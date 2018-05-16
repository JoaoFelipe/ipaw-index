# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import lebo2014a
from ..work.y2014 import bettencourt2014a
from ..work.y2016 import leadbetter2016a
from ..work.y2017 import lebo2017a
from ..work.y2017 import atkinson2017a

DB(Citation(
    lebo2017a, lebo2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    leadbetter2016a, lebo2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    atkinson2017a, lebo2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bettencourt2014a, lebo2014a, ref="",
    contexts=[

    ],
))
