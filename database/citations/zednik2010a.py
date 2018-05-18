# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import zednik2010a
from ..work.y2011 import adams2011a
from ..work.y2011 import west2011a
from ..work.y2011 import leptoukh2011a
from ..work.y2012 import narock2012b
from ..work.y2012 import narock2012a
from ..work.y2014 import narock2014a
from ..work.y2015 import narock2015a

DB(Citation(
    adams2011a, zednik2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    narock2014a, zednik2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    narock2012b, zednik2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    narock2015a, zednik2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    narock2012a, zednik2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    west2011a, zednik2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    leptoukh2011a, zednik2010a, ref="",
    contexts=[

    ],
))
