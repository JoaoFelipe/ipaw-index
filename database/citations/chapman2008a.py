# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import chapman2008a
from ..work.y2008 import chapman2008b
from ..work.y2009 import chapman2009a
from ..work.y2010 import glavic2010a
from ..work.y2010 import miles2010a
from ..work.y2010 import tilmes2010a
from ..work.y2011 import tilmes2011a
from ..work.y2012 import almeida2012a

DB(Citation(
    chapman2009a, chapman2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    glavic2010a, chapman2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tilmes2011a, chapman2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    miles2010a, chapman2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chapman2008b, chapman2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    tilmes2010a, chapman2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    almeida2012a, chapman2008a, ref="",
    contexts=[

    ],
))
