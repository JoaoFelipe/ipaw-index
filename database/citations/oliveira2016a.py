# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2016 import oliveira2016a
from ..work.y2017 import herschel2017a
from ..work.y2017 import oliveira2017a
from ..work.y2017 import missier2017a
from ..work.y2017 import trillo2017a
from ..work.y2018 import prabhune2018a
from ..work.y2018 import prabhune2018b

DB(Citation(
    herschel2017a, oliveira2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    prabhune2018a, oliveira2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    oliveira2017a, oliveira2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    missier2017a, oliveira2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    trillo2017a, oliveira2016a, ref="",
    contexts=[

    ],
))

DB(Citation(
    prabhune2018b, oliveira2016a, ref="",
    contexts=[

    ],
))
