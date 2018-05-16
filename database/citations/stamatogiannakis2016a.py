# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import burgess2016a
from ..work.y2016 import stamatogiannakis2016a
from ..work.y2017 import bates2017a
from ..work.y2017 import stamatogiannakis2017a
from ..work.y2018 import pérez2018a
from ..work.y2018 import gehani2018a

DB(Citation(
    burgess2016a, stamatogiannakis2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bates2017a, stamatogiannakis2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pérez2018a, stamatogiannakis2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gehani2018a, stamatogiannakis2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2017a, stamatogiannakis2016a, ref="",
    contexts=[

    ],
))
