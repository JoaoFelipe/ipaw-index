# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import gadelha2014a
from ..work.y2015 import benabdelkader2015a
from ..work.y2016 import lang2016a
from ..work.y2017 import sánchez2017a

DB(Citation(
    benabdelkader2015a, gadelha2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sánchez2017a, gadelha2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lang2016a, gadelha2014a, ref="",
    contexts=[

    ],
))
