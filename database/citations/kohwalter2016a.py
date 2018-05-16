# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import kohwalter2016a
from ..work.y2017 import jacob2017a
from ..work.y2017 import kohwalter2017a
from ..work.y2017 import stamatogiannakis2017a

DB(Citation(
    jacob2017a, kohwalter2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kohwalter2017a, kohwalter2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2017a, kohwalter2016a, ref="",
    contexts=[

    ],
))
