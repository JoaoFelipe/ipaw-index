# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import stephan2010a
from ..work.y2010 import stephan2010b
from ..work.y2012 import lebo2012a
from ..work.y2012 import dogan2012a
from ..work.y2012 import dogan2012b
from ..work.y2012 import lebo2012b
from ..work.y2013 import feng2013a
from ..work.y2013 import dogan2013a
from ..work.y2013 import liu2013a
from ..work.y2014 import dogan2014a
from ..work.y2016 import dogan2016a
from ..work.y2016 import dogan2016b
from ..work.y2016 import liu2016a

DB(Citation(
    lebo2012a, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    feng2013a, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stephan2010b, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dogan2013a, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dogan2012a, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dogan2012b, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    liu2013a, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dogan2014a, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dogan2016a, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    dogan2016b, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    liu2016a, stephan2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lebo2012b, stephan2010a, ref="",
    contexts=[

    ],
))
