# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import mccusker2010a
from ..work.y2010 import zhao2010a
from ..work.y2011 import mccusker2011a
from ..work.y2012 import brandizi2012a
from ..work.y2014 import gonzález2014a
from ..work.y2014 import rodriguez2014a

DB(Citation(
    gonzález2014a, mccusker2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    mccusker2011a, mccusker2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    brandizi2012a, mccusker2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rodriguez2014a, mccusker2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zhao2010a, mccusker2010a, ref="",
    contexts=[

    ],
))
