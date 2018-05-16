# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import frew2010a
from ..work.y2011 import belhajjame2011a
from ..work.y2011 import plale2011a
from ..work.y2011 import cruz2011b
from ..work.y2013 import aktas2013a
from ..work.y2013 import liu2013a
from ..work.y2014 import eltabakh2014a
from ..work.y2014 import lagoze2014a

DB(Citation(
    belhajjame2011a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    aktas2013a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    plale2011a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    eltabakh2014a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cruz2011b, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    liu2013a, frew2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lagoze2014a, frew2010a, ref="",
    contexts=[

    ],
))
