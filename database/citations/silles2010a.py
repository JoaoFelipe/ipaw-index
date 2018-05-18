# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import silles2010a
from ..work.y2011 import runnalls2011a
from ..work.y2012 import runnalls2012a
from ..work.y2013 import huq2013a
from ..work.y2013 import runnalls2013a
from ..work.y2013 import nascimento2013a
from ..work.y2013 import huq2013b
from ..work.y2014 import lerner2014b
from ..work.y2014 import lerner2014a
from ..work.y2015 import nascimento2015a
from ..work.y2017 import cruz2017a
from ..work.y2018 import lerner2018a

DB(Citation(
    lerner2014b, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huq2013a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lerner2014a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    runnalls2012a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    runnalls2013a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nascimento2013a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    runnalls2011a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lerner2018a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    cruz2017a, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    huq2013b, silles2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    nascimento2015a, silles2010a, ref="",
    contexts=[

    ],
))
