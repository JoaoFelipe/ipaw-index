# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import richardson2016a
from ..work.y2017 import schreiber2017a
from ..work.y2017 import schreiber2017b
from ..work.y2017 import willoughby2017a
from ..work.y2017 import dividino2017a
from ..work.y2017 import stamatogiannakis2017a
from ..work.y2018 import schreiber2018a

DB(Citation(
    schreiber2017a, richardson2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    schreiber2017b, richardson2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    willoughby2017a, richardson2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dividino2017a, richardson2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2017a, richardson2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    schreiber2018a, richardson2016a, ref="",
    contexts=[

    ],
))
