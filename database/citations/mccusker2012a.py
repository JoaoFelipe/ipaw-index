# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import mccusker2012a
from ..work.y2014 import kuhn2014a
from ..work.y2014 import kuhn2014b
from ..work.y2015 import kuhn2015a
from ..work.y2015 import mccusker2015a
from ..work.y2016 import lebo2016a
from ..work.y2016 import nandini2016a
from ..work.y2016 import sri2016a
from ..work.y2016 import shubhangi2016a

DB(Citation(
    kuhn2014a, mccusker2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kuhn2015a, mccusker2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mccusker2015a, mccusker2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lebo2016a, mccusker2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nandini2016a, mccusker2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    kuhn2014b, mccusker2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sri2016a, mccusker2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    shubhangi2016a, mccusker2012a, ref="",
    contexts=[

    ],
))
