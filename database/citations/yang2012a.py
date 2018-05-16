# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import yang2012a
from ..work.y2013 import missier2013a
from ..work.y2014 import wibisono2014a
from ..work.y2014 import ghoshal2014a
from ..work.y2014 import ghoshal2014b
from ..work.y2016 import michaelides2016a
from ..work.y2016 import he2016a

DB(Citation(
    missier2013a, yang2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    wibisono2014a, yang2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    michaelides2016a, yang2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ghoshal2014a, yang2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ghoshal2014b, yang2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    he2016a, yang2012a, ref="",
    contexts=[

    ],
))
