# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import pimentel2016c

from ..work.y2016 import pimentel2016a
from ..work.y2017 import neves2017a
from ..work.y2017 import herschel2017a
from ..work.y2017 import pimentel2017a
from ..work.y2018 import freire2018a

DB(Citation(
    pimentel2016c, pimentel2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    neves2017a, pimentel2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    herschel2017a, pimentel2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pimentel2017a, pimentel2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    freire2018a, pimentel2016a, ref="",
    contexts=[

    ],
))
