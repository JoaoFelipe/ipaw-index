# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import nunes2012a
from ..work.y2015 import cuzzocrea2015a
from ..work.y2016 import cuzzocrea2016a
from ..work.y2017 import sirqueira2017a
from ..work.y2017 import nunes2017a
from ..work.y2017 import sirqueira2017b

DB(Citation(
    cuzzocrea2015a, nunes2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cuzzocrea2016a, nunes2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sirqueira2017a, nunes2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nunes2017a, nunes2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sirqueira2017b, nunes2012a, ref="",
    contexts=[

    ],
))
