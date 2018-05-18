# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import cuevas2014a
from ..work.y2014 import carvalho2014a
from ..work.y2016 import carvalho2016a
from ..work.y2017 import jabal2017a

DB(Citation(
    carvalho2016a, cuevas2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jabal2017a, cuevas2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    carvalho2014a, cuevas2014a, ref="",
    contexts=[

    ],
))
