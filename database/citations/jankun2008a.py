# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2007 import jankun2007a
from ..work.y2008 import jankun2008a
from ..work.y2009 import huang2009a
from ..work.y2010 import moreau2010a
from ..work.y2010 import graves2010b
from ..work.y2011 import jankun2011a
from ..work.y2012 import boyd2012a
from ..work.y2015 import xu2015a
from ..work.y2015 import ko2015a
from ..work.y2016 import pohl2016a
from ..work.y2017 import zhao2017a

DB(Citation(
    moreau2010a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jankun2007a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huang2009a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    xu2015a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    ko2015a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    zhao2017a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    jankun2011a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    pohl2016a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    boyd2012a, jankun2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    graves2010b, jankun2008a, ref="",
    contexts=[

    ],
))
