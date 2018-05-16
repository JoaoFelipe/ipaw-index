# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import hoekstra2014a

from ..work.y2014 import wibisono2014a
from ..work.y2016 import fox2016a
from ..work.y2016 import lang2016a
from ..work.y2017 import willoughby2017a

DB(Citation(
    hoekstra2014a, wibisono2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    fox2016a, wibisono2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    willoughby2017a, wibisono2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lang2016a, wibisono2014a, ref="",
    contexts=[

    ],
))
