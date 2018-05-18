# coding: utf-8
from snowballing.models import *
from snowballing import dbindex
dbindex.last_citation_file = dbindex.this_file(__file__)

from ..work.y2014 import nies2014a
from ..work.y2016 import sansrimahachai2016a

DB(Citation(
    sansrimahachai2016a, nies2014a, ref="",
    contexts=[

    ],
))
