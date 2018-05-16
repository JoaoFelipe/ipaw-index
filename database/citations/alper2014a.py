# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import alper2014a
from ..work.y2015 import dey2015a
from ..work.y2016 import gaignard2016a
from ..work.y2016 import daga2016a
from ..work.y2016 import leipzig2016a
from ..work.y2017 import gaignard2017a
from ..work.y2017 import gaignard2017b
from ..work.y2018 import scheider2018a
from ..work.y2018 import alper2018a

DB(Citation(
    dey2015a, alper2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gaignard2016a, alper2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    scheider2018a, alper2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    daga2016a, alper2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gaignard2017a, alper2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    alper2018a, alper2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    gaignard2017b, alper2014a, ref="",
    contexts=[

    ],
))

DB(Citation(
    leipzig2016a, alper2014a, ref="",
    contexts=[

    ],
))
