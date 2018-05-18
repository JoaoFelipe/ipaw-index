# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import martin2008a
from ..work.y2009 import martin2009a
from ..work.y2009 import martin2009b
from ..work.y2011 import zaki2011a
from ..work.y2011 import martin2011a
from ..work.y2013 import zaki2013a
from ..work.y2014 import farooq2014a

DB(Citation(
    zaki2013a, martin2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zaki2011a, martin2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    martin2009a, martin2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    farooq2014a, martin2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    martin2011a, martin2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    martin2009b, martin2008a, ref="",
    contexts=[

    ],
))
