# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import missier2012a
from ..work.y2013 import missier2013a
from ..work.y2013 import missier2013b
from ..work.y2013 import paula2013a
from ..work.y2013 import dey2013a
from ..work.y2013 import moore2013a
from ..work.y2013 import paula2013b
from ..work.y2015 import nies2015a

DB(Citation(
    missier2013a, missier2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    missier2013b, missier2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    paula2013a, missier2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dey2013a, missier2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moore2013a, missier2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    paula2013b, missier2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nies2015a, missier2012a, ref="",
    contexts=[

    ],
))
