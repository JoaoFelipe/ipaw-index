# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import wendel2010a

from ..work.y2010 import miles2010a
from ..work.y2012 import huq2012a
from ..work.y2013 import huq2013a
from ..work.y2013 import huq2013b
from ..work.y2013 import rezwanul2013a
from ..work.y2014 import chittimalli2014a

DB(Citation(
    wendel2010a, miles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huq2013a, miles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huq2012a, miles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huq2013b, miles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    rezwanul2013a, miles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chittimalli2014a, miles2010a, ref="",
    contexts=[

    ],
))
