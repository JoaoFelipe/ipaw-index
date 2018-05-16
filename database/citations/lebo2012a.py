# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import lebo2012a
from ..work.y2012 import salayandia2012a
from ..work.y2013 import mccusker2013a
from ..work.y2014 import lang2014a
from ..work.y2014 import ghoshal2014b
from ..work.y2015 import lowry2015a
from ..work.y2016 import ragan2016a
from ..work.y2016 import mendon2016a

DB(Citation(
    ragan2016a, lebo2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mccusker2013a, lebo2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lang2014a, lebo2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    salayandia2012a, lebo2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lowry2015a, lebo2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ghoshal2014b, lebo2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mendon2016a, lebo2012a, ref="",
    contexts=[

    ],
))
