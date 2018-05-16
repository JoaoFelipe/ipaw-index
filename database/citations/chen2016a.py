# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import chen2016a
from ..work.y2017 import davis2017a
from ..work.y2017 import davis2017b
from ..work.y2018 import pasquier2018a
from ..work.y2018 import davis2018a

DB(Citation(
    pasquier2018a, chen2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2018a, chen2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2017a, chen2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    davis2017b, chen2016a, ref="",
    contexts=[

    ],
))
