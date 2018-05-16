# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2012 import asuncion2012a
from ..work.y2016 import reddish2016a

DB(Citation(
    reddish2016a, asuncion2012a, ref="",
    contexts=[

    ],
))
