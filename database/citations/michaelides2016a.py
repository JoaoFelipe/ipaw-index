# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import michaelides2016a
from ..work.y2016 import correndo2016a
from ..work.y2017 import correndo2017a
from ..work.y2018 import moreau2018a
from ..work.y2018 import lerner2018a
from ..work.y2018 import moreau2018b

DB(Citation(
    moreau2018a, michaelides2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    correndo2017a, michaelides2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    lerner2018a, michaelides2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    correndo2016a, michaelides2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    moreau2018b, michaelides2016a, ref="",
    contexts=[

    ],
))
