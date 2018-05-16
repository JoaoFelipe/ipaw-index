# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import belhajjame2012a
from ..work.y2015 import woodman2015a
from ..work.y2015 import caron2015a

DB(Citation(
    woodman2015a, belhajjame2012a, ref="",
    contexts=[

    ],
))

DB(Citation(
    caron2015a, belhajjame2012a, ref="",
    contexts=[

    ],
))
