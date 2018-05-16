# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import pham2014a
from ..work.y2014 import pham2014b
from ..work.y2015 import meng2015a
from ..work.y2015 import pham2015a
from ..work.y2015 import meng2015b

DB(Citation(
    meng2015a, pham2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pham2015a, pham2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pham2014b, pham2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    meng2015b, pham2014a, ref="",
    contexts=[

    ],
))
