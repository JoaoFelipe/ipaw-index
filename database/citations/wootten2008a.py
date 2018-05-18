# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2008 import wootten2008a
from ..work.y2009 import wooten2009a
from ..work.y2013 import yeo2013a

DB(Citation(
    yeo2013a, wootten2008a, ref="",
    contexts=[

    ],
))

DB(Citation(
    wooten2009a, wootten2008a, ref="",
    contexts=[

    ],
))
