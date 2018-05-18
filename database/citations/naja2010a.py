# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2007 import ringelstein2007a
from ..work.y2010 import naja2010a
from ..work.y2011 import attwood2011a
from ..work.y2012 import nunes2012a
from ..work.y2014 import attwood2014a
from ..work.y2016 import ramchurn2016a
from ..work.y2017 import sirqueira2017a
from ..work.y2017 import sirqueira2017c

DB(Citation(
    attwood2011a, naja2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ramchurn2016a, naja2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nunes2012a, naja2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sirqueira2017a, naja2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    sirqueira2017c, naja2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ringelstein2007a, naja2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    attwood2014a, naja2010a, ref="",
    contexts=[

    ],
))
