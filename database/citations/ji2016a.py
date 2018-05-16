# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import ji2016a
from ..work.y2017 import ji2017a
from ..work.y2017 import nwafor2017a
from ..work.y2017 import stamatogiannakis2017a

DB(Citation(
    ji2017a, ji2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nwafor2017a, ji2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2017a, ji2016a, ref="",
    contexts=[

    ],
))
