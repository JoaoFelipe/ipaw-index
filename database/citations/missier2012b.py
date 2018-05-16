# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import missier2012b
from ..work.y2012 import li2012a
from ..work.y2013 import randell2013a
from ..work.y2017 import li2017b

DB(Citation(
    randell2013a, missier2012b, ref="",
    contexts=[

    ],
))

DB(Citation(
    li2012a, missier2012b, ref="",
    contexts=[

    ],
))

DB(Citation(
    li2017b, missier2012b, ref="",
    contexts=[

    ],
))
