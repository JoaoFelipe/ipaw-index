# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import michaelis2010a
from ..work.y2011 import ding2011a
from ..work.y2011 import lebo2011a
from ..work.y2012 import gessiou2012a
from ..work.y2013 import gloria2013a

DB(Citation(
    ding2011a, michaelis2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lebo2011a, michaelis2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gessiou2012a, michaelis2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gloria2013a, michaelis2010a, ref="",
    contexts=[

    ],
))
