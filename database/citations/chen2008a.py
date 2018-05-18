# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import chen2008a
from ..work.y2009 import muniswamy2009a
from ..work.y2009 import chen2009b
from ..work.y2010 import muniswamy2010a
from ..work.y2011 import jung2011c
from ..work.y2011 import lang2011a
from ..work.y2012 import zhao2012f

DB(Citation(
    muniswamy2010a, chen2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zhao2012f, chen2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    muniswamy2009a, chen2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jung2011c, chen2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lang2011a, chen2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    chen2009b, chen2008a, ref="",
    contexts=[

    ],
))
