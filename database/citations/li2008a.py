# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import li2008a
from ..work.y2010 import sikkens2010a
from ..work.y2013 import li2013a
from ..work.y2013 import savonnet2013a
from ..work.y2014 import bors2014a
from ..work.y2015 import bors2015a

DB(Citation(
    bors2014a, li2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sikkens2010a, li2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    li2013a, li2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    bors2015a, li2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    savonnet2013a, li2008a, ref="",
    contexts=[

    ],
))
