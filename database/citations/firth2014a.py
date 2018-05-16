# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import firth2014a
from ..work.y2016 import missier2016a
from ..work.y2016 import stamatogiannakis2016a
from ..work.y2016 import lemieux2016a
from ..work.y2017 import firth2017a
from ..work.y2017 import firth2017b
from ..work.y2018 import moreau2018a

DB(Citation(
    moreau2018a, firth2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    missier2016a, firth2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stamatogiannakis2016a, firth2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    firth2017a, firth2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lemieux2016a, firth2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    firth2017b, firth2014a, ref="",
    contexts=[

    ],
))
