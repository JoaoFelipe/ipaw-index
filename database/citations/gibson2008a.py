# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import gibson2008a
from ..work.y2008 import groth2008a
from ..work.y2010 import stephan2010a
from ..work.y2013 import adler2013a
from ..work.y2015 import adler2015a

DB(Citation(
    adler2015a, gibson2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    adler2013a, gibson2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    groth2008a, gibson2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    stephan2010a, gibson2008a, ref="",
    contexts=[

    ],
))
