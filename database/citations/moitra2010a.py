# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2010 import moitra2010a
from ..work.y2013 import crapo2013a
from ..work.y2016 import crapo2016a

DB(Citation(
    crapo2013a, moitra2010a, ref="",
    contexts=[

    ],
))

DB(Citation(
    crapo2016a, moitra2010a, ref="",
    contexts=[

    ],
))
